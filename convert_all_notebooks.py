import os
import sys
from nbconvert import MarkdownExporter
import nbformat


def convert_notebook_to_markdown(input_notebook, output_markdown):
    """Convert a Jupyter notebook to Markdown format."""
    with open(input_notebook, "r", encoding="utf-8") as nb_file:
        notebook = nbformat.read(nb_file, as_version=4)

    exporter = MarkdownExporter()
    body, _ = exporter.from_notebook_node(notebook)

    with open(output_markdown, "w", encoding="utf-8") as md_file:
        md_file.write(body)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python convert_all_notebooks.py folder_path")
        sys.exit(1)

    folder_path = sys.argv[1]

    # Iterate through all .ipynb files in the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ipynb"):
                # Construct full paths
                notebook_path = os.path.join(root, file)
                md_path = os.path.splitext(notebook_path)[0] + ".md"

                # Convert notebook to markdown
                convert_notebook_to_markdown(notebook_path, md_path)

                print(f"Converted {notebook_path} to {md_path}")
