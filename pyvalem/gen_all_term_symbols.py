import webbrowser
from .molecular_term_symbol import MolecularTermSymbol, orbital_irrep_labels

def html_out():
    f = open('html_labels.html','w')
    message_chunks = ['<html>','<head></head>','<body>']
    for label in orbital_irrep_labels:
        temp_symbol = MolecularTermSymbol('1{:s}'.format(label))
        message_chunks.append('<p>{:s}</p>'.format(temp_symbol.html))
    message_chunks.append('</body>')
    message_chunks.append('</html>')
    f.write(''.join(message_chunks))
    f.close()
    webbrowser.open_new_tab('html_labels.html')