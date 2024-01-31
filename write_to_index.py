import os
from urllib.parse import quote

# Define the root directory and the docs directory
root_directory = os.getcwd()
docs_directory = os.path.join(root_directory, 'docs')

# Function to create HTML link list items
def create_link_list(directory, relative_path=''):
    html_list = '<ul>\n'
    for item in sorted(os.listdir(directory)):
        path = os.path.join(directory, item)
        rel_path = os.path.join(relative_path, item)
        # Skip the index file itself and .ipynb_checkpoints
        if item == 'index.html' or '.ipynb_checkpoints' in path:
            continue
        if os.path.isdir(path):
            # Create a collapsible section for directories
            html_list += f'<li><details><summary>{item}</summary>\n'
            html_list += create_link_list(path, rel_path)
            html_list += '</details></li>\n'
        elif item.endswith('.html'):
            # Create a link for HTML files
            link = quote(rel_path)  # Ensure the URL is correctly encoded
            html_list += f'<li><a href="{link}">{item.replace(".html", "")}</a></li>\n'
    html_list += '</ul>\n'
    return html_list

# Create the HTML content for the index file
index_html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index of HTML Files</title>
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <style>
        body {{
            font-family: 'Roboto', sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 40px;
            color: #333;
        }}
        h1 {{
            color: #222;
            text-align: center;
            margin-bottom: 40px;
        }}
        .container {{
            max-width: 960px;
            margin: auto;
            background: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }}
        details summary {{
            cursor: pointer;
            font-weight: 500;
            padding: 10px;
            margin: 5px;
            background-color: #e9ecef;
            border-radius: 5px;
        }}
        details[open] summary {{
            border-bottom: 1px solid #ddd;
        }}
        a {{
            text-decoration: none;
            color: #007bff;
            display: block;
            padding: 5px 10px;
            margin: 5px;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }}
        a:hover {{
            background-color: #e9ecef;
        }}
        ul {{
            list-style-type: none;
            padding-left: 20px;
        }}
        li {{
            margin-bottom: 10px;
        }}
        /* Button Styling */
        .toggle-icon {{
            font-size: 24px;
            color: #28a745; /* Green color */
            cursor: pointer;
            transition: color 0.3s ease;
        }}
        .toggle-icon:hover {{
            color: #218838; /* Darker green */
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Study Notes</h1>
        <i id="toggle" class="fas fa-angle-double-down toggle-icon"></i>
        {create_link_list(docs_directory)}
    </div>
    <script>
        document.getElementById('toggle').addEventListener('click', function() {{
            var details = document.querySelectorAll('details');
            var icon = this;
            var isOpen = icon.classList.contains('fa-angle-double-up');
            for (var i = 0; i < details.length; i++) {{
                details[i].open = !isOpen;
            }}
            // Toggle the icon class
            if (isOpen) {{
                icon.classList.remove('fa-angle-double-up');
                icon.classList.add('fa-angle-double-down');
            }} else {{
                icon.classList.remove('fa-angle-double-down');
                icon.classList.add('fa-angle-double-up');
            }}
        }});
    </script>
</body>
</html>
'''


# Write the new index.html file
with open(os.path.join(docs_directory, 'index.html'), 'w', encoding='utf-8') as file:
    file.write(index_html_content)

