import nbformat
from nbconvert import MarkdownExporter
import sys
import os


def ipynb_to_md(input_file, output_file):
    """Convert a Jupyter notebook to Markdown format."""
    if not input_file.endswith(".ipynb"):
        print("Error: Input file must be a .ipynb notebook file.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    exporter = MarkdownExporter()
    body, _ = exporter.from_notebook_node(nb)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(body)

    print(f"Notebook {input_file} converted to Markdown and saved as {output_file}")


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print(
            "Usage: python convert_notebook_to_md.py input_notebook.ipynb output_markdown.md"
        )
        sys.exit(1)

    # Extract input and output file paths from command-line arguments
    input_notebook = sys.argv[1]
    output_markdown = sys.argv[2]

    # Call function to convert notebook to Markdown
    ipynb_to_md(input_notebook, output_markdown)
