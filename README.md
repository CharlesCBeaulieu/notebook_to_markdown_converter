# Notebook to Markdown Converter

This script converts Jupyter notebooks (.ipynb) to Markdown (.md) format using Python.

### Prerequisites

- Python 3.x installed
- Required Python packages (nbformat, nbconvert)

Install dependencies:

```bash
pip install nbformat nbconvert
```

### Usage

```bash
git clone https://github.com/CharlesCBeaulieu/notebook_to_markdown_converter.git
cd notebook_to_markdown_converter
```

Single Notebook Conversion : 

To convert a single Jupyter notebook file (input_notebook.ipynb) to Markdown format (output_markdown.md), run the following command:

```bash
python ipynb_to_md.py input_notebook.ipynb output_markdown.md
```
Replace input_notebook.ipynb with the path to your specific Jupyter notebook file and output_markdown.md with the desired path to save the Markdown output.

Folder Conversion : 

To convert all Jupyter notebook files within a folder (folder_path) and its subfolders to Markdown format, use the following steps:

```bash
python convert_notebook_to_md.py input_notebook_folder
```