import os
import subprocess

# Define the root directory where the notebooks are located and the docs directory
root_dir = os.getcwd()
docs_dir = os.path.join(root_dir, 'docs')

# Function to convert notebooks to HTML
def convert_notebook_to_html(notebook_path, output_dir):
    subprocess.run(['jupyter', 'nbconvert', '--to', 'html', notebook_path, '--output-dir', output_dir], check=True)

# Function to create the docs directory structure and convert notebooks
def process_notebooks(current_dir):
    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        if os.path.isdir(item_path):
            if '.ipynb_checkpoints' in item_path:
                continue
            # Recursively process subdirectories
            process_notebooks(item_path)
        elif item_path.endswith('.ipynb'):
            # Convert the notebook to HTML
            relative_path = os.path.relpath(item_path, root_dir)
            output_dir = os.path.join(docs_dir, os.path.dirname(relative_path))
            os.makedirs(output_dir, exist_ok=True)
            convert_notebook_to_html(item_path, output_dir)

# Create the docs directory if it doesn't exist
os.makedirs(docs_dir, exist_ok=True)

# Start processing the notebooks from the root directory
process_notebooks(root_dir)
