from ..molecular_term_symbol import (MolecularTermSymbol,
                                           orbital_irrep_labels)

def html_out():
    message_chunks = ['<html>','<head></head>','<body>']
    for label in orbital_irrep_labels:
        temp_symbol = MolecularTermSymbol('1{:s}'.format(label))
        message_chunks.append('<p>{:s}</p>'.format(temp_symbol.html))
    message_chunks.append('</body>')
    message_chunks.append('</html>')
    print('\n'.join(message_chunks))

html_out()
