import nbconvert

def convert_to_html(notebook_file):
    exporter = nbconvert.HTMLExporter()
    output, _ = exporter.from_filename(notebook_file)
    html_file = notebook_file.replace('.ipynb', '.html')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(output)
    print(f"Conversion successful. HTML file saved as {html_file}")

filenames = ['/Users/lendlab/Box Sync/willdecker/GitHub/hidden-markov-model/Introduction.ipynb', '/Users/lendlab/Box Sync/willdecker/GitHub/hidden-markov-model/Transition-Matrices.ipynb', '/Users/lendlab/Box Sync/willdecker/GitHub/hidden-markov-model/Real-World-Markov-Chains-and-Transition-Matrices.ipynb']

for i in filenames:
    convert_to_html(i)

convert_to_html('/Users/lendlab/Box Sync/willdecker/GitHub/hidden-markov-model/docs/intro.ipynb')