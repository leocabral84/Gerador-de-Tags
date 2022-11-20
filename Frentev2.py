import PySimpleGUI as sg
import pyperclip
from Biblioteca import *


descricao = ''
aspas = '"'
chaves1 = '{'
chaves2 = '}'
def make_win1():

    use_custom_titlebar = False
    sg.theme('Dark')



    cores = ['Black', 'grey11', 'grey21', 'grey31', 'DimGray', 'Gray', 'DarkGray', 'Silver', 'LightGrey', 'Gainsboro',
             'SlateBlue', 'SlateBlue1', 'SlateBlue3', 'DarkSlateBlue', 'MidnightBlue', 'Navy',
             'DarkBlue', 'MidnightBlue', 'Navy', 'DarkBlue', 'MediumBlue', 'Blue', 'CornflowerBlue',
             'RoyalBlue', 'DodgerBlue', 'DeepSkyBlue', 'LightSkyBlue', 'SkyBlue',
             'LightBlue', 'SteelBlue', 'LightSteelBlue', 'SlateGray', 'LightSlateGray',
             'Aqua / Cyan', 'DarkTurquoise', 'Turquoise', 'MediumTurquoise',
             'LightSeaGreen', 'DarkCyan', 'Teal', 'Aquamarine', 'MediumAquamarine', 'CadetBlue',
             'DarkSlateGray', 'MediumSpringGreen', 'SpringGreen', 'PaleGreen',
             'LightGreen', 'DarkSeaGreen', 'MediumSeaGreen', 'SeaGreen', 'DarkGreen', 'Green',
             'ForestGreen', 'LimeGreen', 'Lime', 'LawnGreen', 'Chartreuse',
             'GreenYellow', 'YellowGreen', 'OliveDrab', 'DarkOliveGreen',
             'Olive', 'DarkKhaki', 'Goldenrod', 'DarkGoldenrod',
             'SaddleBrown', 'Sienna', 'RosyBrown', 'Peru', 'Chocolate',
             'SandyBrown', 'NavajoWhite', 'Wheat', 'BurlyWood', 'Tan',
             'MediumSlateBlue', 'MediumPurple', 'BlueViolet', 'Indigo', 'DarkViolet',
             'DarkOrchid', 'MediumOrchid', 'Purple', 'DarkMagenta',
             'Fuchsia / Magenta', 'Violet', 'Orchid', 'Plum', 'MediumVioletRed', 'DeepPink',
             'HotPink', 'PaleVioletRed', 'LightPink', 'Pink', 'LightCoral', 'IndianRed',
             'Crimson', 'Maroon', 'DarkRed', 'FireBrick', 'Brown', 'Salmon',
             'DarkSalmon', 'LightSalmon', 'Coral', 'Tomato', 'Red', 'OrangeRed',
             'DarkOrange', 'Orange', 'Gold', 'Yellow', 'Khaki', 'AliceBlue',
             'GhostWhite', 'Snow', 'Seashell', 'FloralWhite', 'WhiteSmoke', 'Beige', 'OldLace',
             'Ivory', 'Linen', 'Cornsilk', 'AntiqueWhite', 'BlanchedAlmond',
             'Bisque', 'LightYellow', 'LemonChiffon', 'LightGoldenrodYellow', 'PapayaWhip', 'PeachPuff',
             'Moccasin', 'PaleGoldenrod', 'MistyRose', 'LavenderBlush',
             'Lavender', 'Thistle', 'Azure', 'LightCyan', 'PowderBlue', 'PaleTurquoise', 'Honeydew', 'MintCream']

    fonte = ['Arial1', 'Helvetica2', 'Verdana3', 'Trebuchet MS4', 'Gill Sans5', 'Noto Sans6', 'Avantgarde7',
    'Optima8', 'Arial Narrow9', 'sans-serif10', 'Times11', 'Didot12', 'Georgia13', 'Palatino14', 'Bookman15',
    'New Century Schoolbook16', 'American Typewriter17', 'serif18', 'Andale Mono19', 'Courier New20', 'Courier21',
    'FreeMono22', 'OCR A Std23', 'DejaVu Sans Mono24', 'monospace25', 'Comic Sans MS26', 'Apple Chancery27', 'Bradley Hand28',
    'Brush Script MT', 'Snell Roundhand30', 'URW Chancery L31', 'cursive32', 'Impact33', 'Luminari34', 'Chalkduster35',
    'Jazz LET36', 'Blippo37', 'Times New Roman38', 'Stencil Std39', 'Marker Felt40', 'Trattatello41']

    fsize = [' ','1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    fsize2 = [' ', 'small','big']
    titulosize = ['  ','1', '2', '3', '4', '5', '6']
    listas = [' ', 'circle', 'square', 'lista ordenada', 'lista ordenada A', 'lista ordenada a', 'lista ordenada I',
              'lista ordenada i', 'lista descritiva']
    links = [' ', 'Link mesma aba', 'Link nova aba']
    layout = [

        [sg.MenubarCustom([['Linguagem', ['HTML', 'CSS']]], k='-CUST MENUBAR-', p=0)] if use_custom_titlebar else [
        sg.Menu([['Linguagem', ['HTML', 'CSS']]], k='-CUST MENUBAR-', p=0)],
        [sg.Text("TAGS HTML - ESCOLHA ENTRE AS OPÇÕES A BAIXO", pad=(380, 0))],
        [sg.Text("                                                                      *O objetivo é reunir o máximo da sintaxe utilizada em diversas linguagens da programação.",
                 pad=(10, 0))],
        [sg.Button("Código HTML"), sg.Button("Comentários"), sg.Button("Negrito"), sg.Button("Itálico"), sg.Button("Sublinhado")
         , sg.Button("Quebra de Linha"), sg.Button("Espaço entre linhas"), sg.Button("Linha Horizontal"),
         sg.Button("Cor da fonte"), sg.Button("Tipo de fonte"), sg.Combo(fonte, k='-COMBOB-', default_value='Arial1')],
        [sg.Text("ESCOLHA A COR", pad=(5, 0)), sg.Text("ESCOLHA UMA OPÇÃO TAM. SIZE E DESABILITE A OUTRA", pad=(65, 0)), sg.Text("TITULOS", pad=(0, 0)),
         sg.Text("OPÇÕES DE LISTAS", pad=(90, 0))],
        [sg.Combo(cores, k='-COMBO-', default_value='MintCream'), sg.Button("Font Size", pad=(45, 0)), sg.Combo(fsize, k='-COMBOC-', default_value=' ', pad=(30, 0)),
         sg.Combo(fsize2, k='-COMBOD-', default_value=' ', pad=(30, 0)), sg.Button("Titulo", pad=(40, 0)), sg.Combo(titulosize, k='-COMBOE-', default_value='  ',
        pad=(0, 0)), sg.Combo(listas, k='-COMBOF-', default_value=' ', pad=(40, 0)), sg.Button("     Lista     "), sg.Button("Título do site na aba", pad=(0, 0))],
        [sg.Button("Cor da Página"), sg.Button("Cor do texto"), sg.Button("    Link    ", pad=(25, 0)), sg.Combo(links, k='-COMBOG-', default_value=' ', pad=(0, 0)),
         sg.Button("Cor dos Links Visitados", pad=(25, 0)), sg.Combo(cores, k='-COMBOH-', default_value='MintCream'), sg.Button("Receber E-mail", pad=(40, 0)),
         sg.Button("Lincar HTML à CSS", pad=(0, 0))],
        [sg.Button("Tag CSS no HTML", pad=(5, 0)), sg.Button("Imagem", pad=(5, 0))],
        [sg.Text("", key="texto_informacao", size=(140, 13), pad=(10, 40), background_color='Gray')],
        [sg.Text("", key="texto_exemplo", pad=(10, 0), background_color='Dark Orange'), sg.Button("Copiar Código"), sg.Button("Limpar")],



    ]
    return sg.Window("Dicionário do Programador by LeoCabral", layout, finalize=True, resizable = True, enable_close_attempted_event=True)


def make_win2():
    use_custom_titlebar = False
    sg.theme('Dark')

    palhetargb = ['Tons de Preto', 'Black', 'grey11', 'grey21', 'grey31', 'DimGray', 'Gray', 'DarkGray',
                  'Silver', 'LightGrey', 'Gainsboro', 'Tons de Azul', 'SlateBlue', 'SlateBlue1', 'SlateBlue3',
                  'DarkSlateBlue',
                  'MidnightBlue', 'Navy', 'DarkBlue', 'MediumBlue', 'Blue', 'CornflowerBlue', 'RoyalBlue', 'DodgerBlue',
                  'DeepSkyBlue', 'LightSkyBlue', 'SkyBlue', 'LightBlue', 'SteelBlue', 'LightSteelBlue', 'SlateGray',
                  'LightSlateGray',
                  'Tons de Ciano', 'Aqua / Cyan', 'DarkTurquoise', 'Turquoise', 'MediumTurquoise', 'LightSeaGreen',
                  'DarkCyan', 'Teal',
                  'Aquamarine', 'MediumAquamarine', 'CadetBlue', 'Tons de Verde', 'DarkSlateGray', 'MediumSpringGreen',
                  'SpringGreen', 'PaleGreen',
                  'LightGreen', 'DarkSeaGreen', 'MediumSeaGreen', 'SeaGreen', 'DarkGreen', 'Green', 'ForestGreen',
                  'LimeGreen',
                  'Lime', 'LawnGreen', 'Chartreuse', 'GreenYellow', 'YellowGreen', 'OliveDrab', 'DarkOliveGreen',
                  'Olive',
                  'Tons de Marrom', 'DarkKhaki', 'Goldenrod', 'DarkGoldenrod', 'SaddleBrown', 'Sienna', 'RosyBrown',
                  'Peru',
                  'Chocolate', 'SandyBrown', 'NavajoWhite', 'Wheat', 'BurlyWood', 'Tan', 'Tons de Roxo',
                  'MediumSlateBlue',
                  'MediumPurple', 'BlueViolet', 'Indigo', 'DarkViolet', 'DarkOrchid', 'MediumOrchid', 'Purple',
                  'DarkMagenta',
                  'Fuchsia / Magenta', 'Violet', 'Orchid', 'Plum', 'Tons de Rosa', 'MediumVioletRed', 'DeepPink',
                  'HotPink',
                  'PaleVioletRed', 'LightPink', 'Pink', 'LightCoral', 'IndianRed', 'Crimson', 'Tons de Vermelho',
                  'Maroon',
                  'DarkRed', 'FireBrick', 'Brown', 'Salmon', 'DarkSalmon', 'LightSalmon', 'Coral', 'Tomato',
                  'Red', 'Tons de Laranja', 'OrangeRed', 'DarkOrange', 'Orange', 'Tons de Amarelo', 'Gold', 'Yellow',
                  'Khaki', 'Tons Pastel', 'AliceBlue', 'GhostWhite', 'Snow', 'Seashell', 'FloralWhite', 'WhiteSmoke',
                  'Beige', 'OldLace', 'Ivory', 'Linen', 'Cornsilk', 'AntiqueWhite', 'BlanchedAlmond', 'Bisque',
                  'LightYellow', 'LemonChiffon', 'LightGoldenrodYellow', 'PapayaWhip', 'PeachPuff', 'Moccasin',
                  'PaleGoldenrod', 'MistyRose',
                  'LavenderBlush', 'Lavender', 'Thistle', 'Azure', 'LightCyan', 'PowderBlue', 'PaleTurquoise',
                  'Honeydew', 'MintCream']




    layout = [

              [sg.MenubarCustom([['Linguagem', ['HTML', 'CSS']]], k='-CUST MENUBAR-', p=0)] if use_custom_titlebar else [
              sg.Menu([['Linguagem', ['HTML', 'CSS']]], k='-CUST MENUBAR-', p=0)],
              [sg.Text('Janela CSS')],
              [sg.Combo(palhetargb, k='-COMBOI-', default_value='Black')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text(size=(100, 10), k='-OUTPUT-')],
              [sg.Button('Erase'), sg.Button('Popup')]]
    return sg.Window('Dicionário do Programador by LeoCabral', layout, finalize=True, enable_close_attempted_event=True)

window1, window2 = make_win1(), None        # start off with 1 window open




palheta = {'Black': '#000000', 'grey11': '#1C1C1C', 'grey21': '#363636', 'grey31': '#4F4F4F', 'DimGray': '#696969',
               'Gray': '#808080', 'DarkGray': '#A9A9A9', 'Silver': '#C0C0C0', 'LightGrey': '#D3D3D3',
               'Gainsboro': '#DCDCDC',
               'SlateBlue': '#6A5ACD', 'SlateBlue1': '#836FFF', 'SlateBlue3': '#6959CD', 'DarkSlateBlue': '#483D8B',
               'MidnightBlue': '#191970', 'Navy': '#000080', 'DarkBlue': '#00008B', 'MediumBlue': '#0000CD',
               'Blue': '#0000FF', 'CornflowerBlue': '#6495ED', 'RoyalBlue': '#4169E1', 'DodgerBlue': '#1E90FF',
               'DeepSkyBlue': '#00BFFF', 'LightSkyBlue': '#87CEFA', 'SkyBlue': '#87CEEB',
               'LightBlue': '#ADD8E6', 'SteelBlue': '#4682B4', 'LightSteelBlue': '#B0C4DE',
               'SlateGray': '#708090', 'LightSlateGray': '#778899', 'Aqua / Cyan': '#00FFFF',
               'DarkTurquoise': '#00CED1', 'Turquoise': '#40E0D0', 'MediumTurquoise': '#48D1CC',
               'LightSeaGreen': '#20B2AA',
               'DarkCyan': '#008B8B', 'Teal': '#008080', 'Aquamarine': '#7FFFD4', 'MediumAquamarine': '#66CDAA',
               'CadetBlue': '#5F9EA0', 'DarkSlateGray': '#2F4F4F', 'MediumSpringGreen': '#00FA9A',
               'SpringGreen': '#00FF7F',
               'PaleGreen': '#98FB98', 'LightGreen': '#90EE90', 'DarkSeaGreen': '#8FBC8F', 'MediumSeaGreen': '#3CB371',
               'SeaGreen': '#2E8B57', 'DarkGreen': '#006400', 'Green': '#008000', 'ForestGreen': '#228B22',
               'LimeGreen': '#32CD32', 'Lime': '#00FF00', 'LawnGreen': '#7CFC00', 'Chartreuse': '#7FFF00',
               'GreenYellow': '#ADFF2F', 'YellowGreen': '#9ACD32', 'OliveDrab': '6B8E23', 'DarkOliveGreen': '#556B2F',
               'Olive': '#808000', 'DarkKhaki': '#BDB76B', 'Goldenrod': '#DAA520', 'DarkGoldenrod': '#B8860B',
               'SaddleBrown': '#8B4513', 'Sienna': '#A0522D', 'RosyBrown': '#BC8F8F', 'Peru': '#CD853F',
               'Chocolate': '#D2691E', 'SandyBrown': '#F4A460', 'NavajoWhite': '#FFDEAD', 'Wheat': '#F5DEB3',
               'BurlyWood': '#DEB887', 'Tan': '#D2B48C', 'MediumSlateBlue': '#7B68EE', 'MediumPurple': '#9370DB',
               'BlueViolet': '#8A2BE2', 'Indigo': '#4B0082', 'DarkViolet': '#9400D3', 'DarkOrchid': '#9932CC',
               'MediumOrchid': '#BA55D3', 'Purple': '#A020F0', 'DarkMagenta': '#8B008B', 'Fuchsia / Magenta': '#FF00FF',
               'Violet': '#EE82EE', 'Orchid': '#DA70D6', 'Plum': '#DDA0DD', 'MediumVioletRed': '#C71585',
               'DeepPink': '#FF1493', 'HotPink': '#FF69B4', 'PaleVioletRed': '#DB7093', 'LightPink': '#FFB6C1',
               'Pink': '#FFC0CB', 'LightCoral': '#F08080', 'IndianRed': '#CD5C5C', 'Crimson': '#DC143C',
               'Maroon': '#800000', 'DarkRed': '#8B0000', 'FireBrick': '#B22222', 'Brown': '#A52A2A',
               'Salmon': '#FA8072', 'DarkSalmon': '#E9967A', 'LightSalmon': '#FFA07A', 'Coral': '#FF7F50',
               'Tomato': '#FF6347', 'Red': '#FF0000', 'OrangeRed': '#FF4500', 'DarkOrange': '#FF8C00',
               'Orange': '#FFA500', 'Gold': '#FFD700', 'Yellow': '#FFFF00', 'Khaki': '#F0E68C',
               'AliceBlue': '#F0F8FF', 'GhostWhite': '#F8F8FF', 'Snow': '#FFFAFA',
               'Seashell': '#FFF5EE', 'FloralWhite': '#FFFAF0', 'WhiteSmoke': '#F5F5F5', 'Beige': '#F5F5DC',
               'OldLace': '#FDF5E6', 'Ivory': '#FFFFF0', 'Linen': '#FAF0E6', 'Cornsilk': '#FFF8DC',
               'AntiqueWhite': '#FAEBD7', 'BlanchedAlmond': '#FFEBCD', 'Bisque': '#FFE4C4', 'LightYellow': '#FFFFE0',
               'LemonChiffon': '#FFFACD', 'LightGoldenrodYellow': '#FAFAD2',
               'PapayaWhip': '#FFEFD5', 'PeachPuff': '#FFDAB9', 'Moccasin': '#FFE4B5',
               'PaleGoldenrod': '#EEE8AA', 'MistyRose': '#FFE4E1', 'LavenderBlush': '#FFF0F5',
               'Lavender': '#E6E6FA', 'Thistle': '#D8BFD8', 'Azure': '#F0FFFF', 'LightCyan': '#E0FFFF',
               'PowderBlue': '#B0E0E6', 'PaleTurquoise': '#E0FFFF', 'Honeydew': '#F0FFF0', 'MintCream': '#F5FFFA'}




fontes = {'Arial1': 'Arial', 'Helvetica2': 'Helvetica', 'Verdana3': 'Verdana', 'Trebuchet MS4': 'Trebuchet MS',
        'Gill Sans5': 'Gill Sans', 'Noto Sans6': 'Noto Sans', 'Avantgarde7': 'Avantgarde',
        'Optima8': 'Optima', 'Arial Narrow9': 'Arial Narrow', 'sans-serif10': 'sans-serif',
        'Times11': 'Times', 'Didot12': 'Didot', 'Georgia13': 'Georgia',  'Palatino14': 'Palatino',
        'Bookman15': 'Bookman', 'New Century Schoolbook16': 'New Century Schoolbook',
        'American Typewriter17': 'American Typewriter', 'serif18': 'serif', 'Andale Mono19': 'Andale Mono',
        'Courier New20': 'Courier New', 'Courier21': 'Courier', 'FreeMono22': 'FreeMono', 'OCR A Std23': 'OCR A Std',
        'DejaVu Sans Mono24': 'DejaVu Sans Mono', 'monospace25': 'monospace', 'Comic Sans MS26': 'Comic Sans MS',
        'Apple Chancery27': 'Apple Chancery', 'Bradley Hand28': 'Bradley Hand', 'Brush Script MT29': 'Brush Script MT',
        'Snell Roundhand30': 'Snell Roundhand', 'URW Chancery L31': 'URW Chancery L',
        'cursive32': 'cursive', 'Impact33': 'Impact', 'Luminari34': 'Luminari', 'Chalkduster35': 'Chalkduster',
        'Jazz LET36': 'Jazz LET', 'Blippo37': 'Blippo', 'Times New Roman38': 'Times New Roman',
        'Stencil Std39': 'Stencil Std', 'Marker Felt40': 'Marker Felt', 'Trattatello41': 'Trattatello'}



while True:             # Event Loop
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:

        window.close()
        if window == window2:  # if closing win 2, mark as closed
            window2 = None
            window1 = make_win1()
        elif event == sg.WIN_CLOSED:
            if window == window1:  # if closing win 1, exit program
                break

    # ABRIR JANELA 2
    elif values ['-CUST MENUBAR-'] == 'CSS' and not window2:
        window2 = make_win2()
        window1 = window1.close()
    elif values ['-CUST MENUBAR-'] == 'HTML' and not window1:
        window1 = make_win1()
        window2 = window2.close()




    if event == "Código HTML":
        descricao = codigoHtml()
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'')

    elif event == "Comentários":
        descricao = Comentarios()
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'')
    elif event == "Negrito":
        descricao = negrito()
        texto = 'Texto em negrito'
        window['texto_exemplo'].update(f'')
        window['texto_informacao'].update(f'{descricao}')
    elif event == "Itálico":
        descricao = italico()
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'')
    elif event == "Sublinhado":
        descricao = sublinhado()
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'')
    elif event == "Quebra de Linha":
        descricao = quebralinha()
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'Esta linha está<br>quebrada. \n\n=> Esta linha está\nquebrada.')

    elif event == "Espaço entre linhas":
        descricao = espacolinhas()
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'Esta linha está <p> com um espaço a mais. \n\n=> Esta linha está \n\n com um espaço a mais.')

    elif event == "Linha Horizontal":
        descricao = linhahoriz()
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'Para que a frase fique sublinhada coloque no final <hr>. \n\nOu no inicio se quiser que a linha fique em cima da frase.')

    elif values['-COMBOF-'] == 'circle' and event == "     Lista     ":
        descricao = '{}'.format('<ul>\n    <li>São Paulo\n    <li>Rio de Janeiro\n    <li>Mato Grosso\n </ul>')
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'')

    elif values['-COMBOF-'] == 'square' and event == "     Lista     ":
        descricao = '{}'.format('{}{}{}{}{}\n     {}\n     {}\n     {}\n{}'.format('<ul type=', aspas,'square', aspas, '>','<li>São Paulo',
         '<li>Rio de Janeiro', '<li>Mato Grosso', '</ul>'))
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'')

    elif values['-COMBOF-'] == 'lista ordenada' and event == "     Lista     ":
        descricao = '{}'.format('<ol>\n    <li>Laranjas\n    <li>Maçãs\n    <li>Bananas\n </ol>')
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'1. Laranjas\n2. Maçãs\n3. Bananas\n\n É possivel iniciar a lista por um numero especifico dessa forma:'
                                       f'\n<ol start=5>\n   <li value=6> São Paulo\n   <li>Rio de Janeiro\n   <li>Mato Grosso\n</ol>')

    elif values['-COMBOF-'] == 'lista ordenada A' and event == "     Lista     ":
        descricao = '{}'.format('{}{}{}{}{}\n     {}\n     {}\n     {}\n{}'.format('<ol type=', aspas, 'A', aspas, '>',
        '<li>São Paulo', '<li>Rio de Janeiro', '<li>Mato Grosso', '</ol>'))
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'A. Laranjas\nB. Maçãs\nC. Bananas')

    elif values['-COMBOF-'] == 'lista ordenada a' and event == "     Lista     ":
        descricao = '{}'.format('{}{}{}{}{}\n     {}\n     {}\n     {}\n{}'.format('<ol type=', aspas, 'a', aspas, '>',
        '<li>São Paulo', '<li>Rio de Janeiro', '<li>Mato Grosso', '</ol>'))
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'a. Laranjas\nb. Maçãs\nc. Bananas')

    elif values['-COMBOF-'] == 'lista ordenada I' and event == "     Lista     ":
        descricao = '{}'.format('{}{}{}{}{}\n     {}\n     {}\n     {}\n{}'.format('<ol type=', aspas, 'I', aspas, '>',
        '<li>São Paulo', '<li>Rio de Janeiro', '<li>Mato Grosso', '</ol>'))
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'I. Laranjas\nII. Maçãs\nIII. Bananas')

    elif values['-COMBOF-'] == 'lista ordenada i' and event == "     Lista     ":
        descricao = '{}'.format('{}{}{}{}{}\n     {}\n     {}\n     {}\n{}'.format('<ol type=', aspas, 'i', aspas, '>',
        '<li>São Paulo', '<li>Rio de Janeiro', '<li>Mato Grosso', '</ol>'))
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'i. Laranjas\nii. Maçãs\niii. Bananas')

    elif values['-COMBOF-'] == 'lista descritiva' and event == "     Lista     ":
        descricao = '{}'.format('<dl>\n    <dt>Marshall Brain\n    <dd>Fundador da HowStuffWorks\n </dl>')
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'Marshall Brain\n        Fundador da HowStuffWorks')

    elif values['-COMBOG-'] == 'Link mesma aba' and event == "    Link    ":
        descricao = '{}{}{}{}{}{}{}'.format('<a href=', aspas, 'Link aqui', aspas, '>','Texto aqui','</a>')
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'Exemplo:' f'<a href='f'"' f'https://www.google.com/'f'"'f'>'f'Clique aqui para acessar o Google</a>')

    elif values['-COMBOG-'] == 'Link nova aba'  and event == "    Link    ":
        descricao = '{}{}{}{} {}{}{}{}{}{}{}'.format('<a href=', aspas, 'Link aqui', aspas, 'target=', aspas, '_blank', aspas,'>', 'Texto aqui', '</a>')
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(
            f'Exemplo:' f'<a href='f'"' f'https://www.google.com/'f'"'f' target='f'"'f'_blank'f'"'f'>'f'Clique aqui para acessar o Google</a>')

    elif event == "Receber E-mail":
        descricao = '{}{}{}{}{}'.format('<a href=', aspas, 'mailto:exemplo@howstuffworks.com', aspas, '> Envie-me um e-mail </a>')
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'')

    elif event == "Título do site na aba":
        descricao = '{}'.format('<title>Titulo aqui </title>')
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'Este código deve ser colocado entre <HEAD>::Aqui::</HEAD>: \n<head>\n    <title>Titulo aqui </title>\n</head>')

    elif event == "Lincar HTML à CSS":
        descricao = '{}{}{}{}{}{}{}'.format('<link rel="stylesheet', aspas, 'href=', aspas,'/style.css', aspas,'/>')
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(
            f'Este código deve ser colocado entre <HEAD>::Aqui::</HEAD>: \n<head>\n    <link rel="stylesheet'f'"'f'href='f'"'f'/style.css'f'"'f'/>\n</head>\n\nCria uma'
            f'relação entre um documento HTML e um arquivo CSS.\nrel -> Define o tipo de arquivo\nhref -> Define o caminho do arquivo.')

    elif event == "Tag CSS no HTML":
        descricao = '{}'.format('<style>\n</style>')
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update('{}{}{}{}{}'.format('<head>\n<style>\np', chaves1,'\n   color: blue;\n   background-color: yellow;\n', chaves2,'\n</style>\n</head>'))

    elif event == "Imagem":
        descricao = '{}{}{}{}{}{}{}{}{}'.format('<img src=', aspas, 'endereço imagem.jpeg', aspas,' alt=', aspas, 'Texto alternativo da imagem', aspas, '>')
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update('')

        #"Imagem" "



        # TROCA ENTRE FUNÇÕES DE COLORIR FUNDO DA PÁGINA, TEXTO...
    fsz = ''
    corx = ''
    fontex = ''

    escolha = False
    if event == "Cor da Página":
        corx = Corfundo()
        escolha = True
    elif event == "Cor do texto":
        corx = Cortexto()
        escolha = True
    elif event == "Cor da fonte":
        corx = fontetexto()
        escolha = True
    elif event == "Tipo de fonte":
        corx = fonte2texto()
        escolha = True
    elif event == "Font Size":
        corx = fontsize()
        escolha = True
    elif event == "Titulo":
        corx = titulo()
        escolha = True




    if values['-COMBOC-'] == '1':
         fsz = '1'
         values['-COMBOD-'] = ' '
    elif values['-COMBOC-'] == '2':
        fsz = '2'
        values['-COMBOD-'] = ' '
    elif values['-COMBOC-'] == '3':
        fsz = '3'
        values['-COMBOD-'] = ' '
    elif values['-COMBOC-'] == '4':
        fsz = '4'
        values['-COMBOD-'] = ' '
    elif values['-COMBOC-'] == '5':
        fsz = '5'
        values['-COMBOD-'] = ' '
    elif values['-COMBOC-'] == '6':
        fsz = '6'
        values['-COMBOD-'] = ' '
    elif values['-COMBOC-'] == '7':
        fsz = '7'
        values['-COMBOD-'] = ' '
    elif values['-COMBOC-'] == '8':
        fsz = '8'
        values['-COMBOD-'] = ' '
    elif values['-COMBOC-'] == '9':
        fsz = '9'
        values['-COMBOD-'] = ' '
    elif values['-COMBOC-'] == '10':
        fsz = '10'
        values['-COMBOD-'] = ' '
    if values['-COMBOD-'] == 'small':
        fsz = fsmall()
        values['-COMBOC-'] = ' '
    elif values['-COMBOD-'] == 'big':
        fsz = fbig()
        values['-COMBOC-'] = ' '

    elif values['-COMBOE-'] == '1':
        fsz = '1'

    elif values['-COMBOE-'] == '2':
        fsz = '2'

    elif values['-COMBOE-'] == '3':
        fsz = '3'

    elif values['-COMBOE-'] == '4':
        fsz = '4'

    elif values['-COMBOE-'] == '5':
        fsz = '5'

    elif values['-COMBOE-'] == '6':
        fsz = '6'



    # "Titulo" / '-COMBOE-' / titulo()




    ########### CORES ################
    palhetax = ''
    palhetay = ''


    try:
        if values['-COMBO-'] == 'Black':
            palhetax = 'Black'
            palhetay = palheta['Black']
        elif values['-COMBO-'] == 'grey11':
            palhetax = 'grey11'
            palhetay = palheta['grey11']
        elif values['-COMBO-'] == 'grey21':
            palhetax = 'grey21'
            palhetay = palheta['grey21']
        elif values['-COMBO-'] == 'grey31':
            palhetax = 'grey31'
            palhetay = palheta['grey31']
        elif values['-COMBO-'] == 'DimGray':
            palhetax = 'DimGray'
            palhetay = palheta['DimGray']
        elif values['-COMBO-'] == 'Gray':
            palhetax = 'Gray'
            palhetay = palheta['Gray']
        elif values['-COMBO-'] == 'DarkGray':
            palhetax = 'DarkGray'
            palhetay = palheta['DarkGray']
        elif values['-COMBO-'] == 'Silver':
            palhetax = 'Silver'
            palhetay = palheta['Silver']
        elif values['-COMBO-'] == 'LightGrey':
            palhetax = 'LightGrey'
            palhetay = palheta['LightGrey']
        elif values['-COMBO-'] == 'Gainsboro':
            palhetax = 'Gainsboro'
            palhetay = palheta['Gainsboro']
        elif values['-COMBO-'] == 'SlateBlue':
            palhetax = 'SlateBlue'
            palhetay = palheta['SlateBlue']
        elif values['-COMBO-'] == 'SlateBlue1':
            palhetax = 'SlateBlue1'
            palhetay = palheta['SlateBlue1']
        elif values['-COMBO-'] == 'SlateBlue3':
            palhetax = 'SlateBlue3'
            palhetay = palheta['SlateBlue3']
        elif values['-COMBO-'] == 'DarkSlateBlue':
            palhetax = 'DarkSlateBlue'
            palhetay = palheta['DarkSlateBlue']
        elif values['-COMBO-'] == 'MidnightBlue':
            palhetax = 'MidnightBlue'
            palhetay = palheta['MidnightBlue']
        elif values['-COMBO-'] == 'Navy':
            palhetax = 'Navy'
            palhetay = palheta['Navy']
        elif values['-COMBO-'] == 'DarkBlue':
            palhetax = 'DarkBlue'
            palhetay = palheta['DarkBlue']
        elif values['-COMBO-'] == 'MidnightBlue':
            palhetax = 'MidnightBlue'
            palhetay = palheta['MidnightBlue']
        elif values['-COMBO-'] == 'Navy':
            palhetax = 'Navy'
            palhetay = palheta['Navy']
        elif values['-COMBO-'] == 'DarkBlue':
            palhetax = 'DarkBlue'
            palhetay = palheta['DarkBlue']
        elif values['-COMBO-'] == 'MediumBlue':
            palhetax = 'MediumBlue'
            palhetay = palheta['MediumBlue']
        elif values['-COMBO-'] == 'Blue':
            palhetax = 'Blue'
            palhetay = palheta['Blue']
        elif values['-COMBO-'] == 'CornflowerBlue':
            palhetax = 'CornflowerBlue'
            palhetay = palheta['CornflowerBlue']
        elif values['-COMBO-'] == 'RoyalBlue':
            palhetax = 'RoyalBlue'
            palhetay = palheta['RoyalBlue']
        elif values['-COMBO-'] == 'DodgerBlue':
            palhetax = 'DodgerBlue'
            palhetay = palheta['DodgerBlue']
        elif values['-COMBO-'] == 'DeepSkyBlue':
            palhetax = 'DeepSkyBlue'
            palhetay = palheta['DeepSkyBlue']
        elif values['-COMBO-'] == 'LightSkyBlue':
            palhetax = 'LightSkyBlue'
            palhetay = palheta['LightSkyBlue']
        elif values['-COMBO-'] == 'SkyBlue':
            palhetax = 'SkyBlue'
            palhetay = palheta['SkyBlue']
        elif values['-COMBO-'] == 'LightBlue':
            palhetax = 'LightBlue'
            palhetay = palheta['LightBlue']
        elif values['-COMBO-'] == 'SteelBlue':
            palhetax = 'SteelBlue'
            palhetay = palheta['SteelBlue']
        elif values['-COMBO-'] == 'LightSteelBlue':
            palhetax = 'LightSteelBlue'
            palhetay = palheta['LightSteelBlue']
        elif values['-COMBO-'] == 'SlateGray':
            palhetax = 'SlateGray'
            palhetay = palheta['SlateGray']
        elif values['-COMBO-'] == 'LightSlateGray':
            palhetax = 'LightSlateGray'
            palhetay = palheta['LightSlateGray']
        elif values['-COMBO-'] == 'Aqua / Cyan':
            palhetax = 'Aqua / Cyan'
            palhetay = palheta['Aqua / Cyan']
        elif values['-COMBO-'] == 'DarkTurquoise':
            palhetax = 'DarkTurquoise'
            palhetay = palheta['DarkTurquoise']
        elif values['-COMBO-'] == 'Turquoise':
            palhetax = 'Turquoise'
            palhetay = palheta['Turquoise']
        elif values['-COMBO-'] == 'MediumTurquoise':
            palhetax = 'MediumTurquoise'
            palhetay = palheta['MediumTurquoise']
        elif values['-COMBO-'] == 'LightSeaGreen':
            palhetax = 'LightSeaGreen'
            palhetay = palheta['LightSeaGreen']
        elif values['-COMBO-'] == 'DarkCyan':
            palhetax = 'DarkCyan'
            palhetay = palheta['DarkCyan']
        elif values['-COMBO-'] == 'Teal':
            palhetax = 'Teal'
            palhetay = palheta['Teal']
        elif values['-COMBO-'] == 'Aquamarine':
            palhetax = 'Aquamarine'
            palhetay = palheta['Aquamarine']
        elif values['-COMBO-'] == 'MediumAquamarine':
            palhetax = 'MediumAquamarine'
            palhetay = palheta['MediumAquamarine']
        elif values['-COMBO-'] == 'CadetBlue':
            palhetax = 'CadetBlue'
            palhetay = palheta['CadetBlue']
        elif values['-COMBO-'] == 'DarkSlateGray':
            palhetax = 'DarkSlateGray'
            palhetay = palheta['DarkSlateGray']
        elif values['-COMBO-'] == 'MediumSpringGreen':
            palhetax = 'MediumSpringGreen'
            palhetay = palheta['MediumSpringGreen']
        elif values['-COMBO-'] == 'SpringGreen':
            palhetax = 'SpringGreen'
            palhetay = palheta['SpringGreen']
        elif values['-COMBO-'] == 'PaleGreen':
            palhetax = 'PaleGreen'
            palhetay = palheta['PaleGreen']
        elif values['-COMBO-'] == 'LightGreen':
            palhetax = 'LightGreen'
            palhetay = palheta['LightGreen']
        elif values['-COMBO-'] == 'DarkSeaGreen':
            palhetax = 'DarkSeaGreen'
            palhetay = palheta['DarkSeaGreen']
        elif values['-COMBO-'] == 'MediumSeaGreen':
            palhetax = 'MediumSeaGreen'
            palhetay = palheta['MediumSeaGreen']
        elif values['-COMBO-'] == 'SeaGreen':
            palhetax = 'SeaGreen'
            palhetay = palheta['SeaGreen']
        elif values['-COMBO-'] == 'DarkGreen':
            palhetax = 'DarkGreen'
            palhetay = palheta['DarkGreen']
        elif values['-COMBO-'] == 'Green':
            palhetax = 'Green'
            palhetay = palheta['Green']
        elif values['-COMBO-'] == 'ForestGreen':
            palhetax = 'ForestGreen'
            palhetay = palheta['ForestGreen']
        elif values['-COMBO-'] == 'LimeGreen':
            palhetax = 'LimeGreen'
            palhetay = palheta['LimeGreen']
        elif values['-COMBO-'] == 'Lime':
            palhetax = 'Lime'
            palhetay = palheta['Lime']
        elif values['-COMBO-'] == 'LawnGreen':
            palhetax = 'LawnGreen'
            palhetay = palheta['LawnGreen']
        elif values['-COMBO-'] == 'Chartreuse':
            palhetax = 'Chartreuse'
            palhetay = palheta['Chartreuse']
        elif values['-COMBO-'] == 'GreenYellow':
            palhetax = 'GreenYellow'
            palhetay = palheta['GreenYellow']
        elif values['-COMBO-'] == 'YellowGreen':
            palhetax = 'YellowGreen'
            palhetay = palheta['YellowGreen']
        elif values['-COMBO-'] == 'OliveDrab':
            palhetax = 'OliveDrab'
            palhetay = palheta['OliveDrab']
        elif values['-COMBO-'] == 'DarkOliveGreen':
            palhetax = 'DarkOliveGreen'
            palhetay = palheta['DarkOliveGreen']
        elif values['-COMBO-'] == 'Olive':
            palhetax = 'Olive'
            palhetay = palheta['Olive']
        elif values['-COMBO-'] == 'DarkKhaki':
            palhetax = 'DarkKhaki'
            palhetay = palheta['DarkKhaki']
        elif values['-COMBO-'] == 'Goldenrod':
            palhetax = 'Goldenrod'
            palhetay = palheta['Goldenrod']
        elif values['-COMBO-'] == 'DarkGoldenrod':
            palhetax = 'DarkGoldenrod'
            palhetay = palheta['DarkGoldenrod']
        elif values['-COMBO-'] == 'SaddleBrown':
            palhetax = 'SaddleBrown'
            palhetay = palheta['SaddleBrown']
        elif values['-COMBO-'] == 'Sienna':
            palhetax = 'Sienna'
            palhetay = palheta['Sienna']
        elif values['-COMBO-'] == 'RosyBrown':
            palhetax = 'RosyBrown'
            palhetay = palheta['RosyBrown']
        elif values['-COMBO-'] == 'Peru':
            palhetax = 'Peru'
            palhetay = palheta['Peru']
        elif values['-COMBO-'] == 'Chocolate':
            palhetax = 'Chocolate'
            palhetay = palheta['Chocolate']
        elif values['-COMBO-'] == 'SandyBrown':
            palhetax = 'SandyBrown'
            palhetay = palheta['SandyBrown']
        elif values['-COMBO-'] == 'NavajoWhite':
            palhetax = 'NavajoWhite'
            palhetay = palheta['NavajoWhite']
        elif values['-COMBO-'] == 'Wheat':
            palhetax = 'Wheat'
            palhetay = palheta['Wheat']
        elif values['-COMBO-'] == 'BurlyWood':
            palhetax = 'BurlyWood'
            palhetay = palheta['BurlyWood']
        elif values['-COMBO-'] == 'Tan':
            palhetax = 'Tan'
            palhetay = palheta['Tan']
        elif values['-COMBO-'] == 'MediumSlateBlue':
            palhetax = 'MediumSlateBlue'
            palhetay = palheta['MediumSlateBlue']
        elif values['-COMBO-'] == 'MediumPurple':
            palhetax = 'MediumPurple'
            palhetay = palheta['MediumPurple']
        elif values['-COMBO-'] == 'BlueViolet':
            palhetax = 'BlueViolet'
            palhetay = palheta['BlueViolet']
        elif values['-COMBO-'] == 'Indigo':
            palhetax = 'Indigo'
            palhetay = palheta['Indigo']
        elif values['-COMBO-'] == 'DarkViolet':
            palhetax = 'DarkViolet'
            palhetay = palheta['DarkViolet']
        elif values['-COMBO-'] == 'DarkOrchid':
            palhetax = 'DarkOrchid'
            palhetay = palheta['DarkOrchid']
        elif values['-COMBO-'] == 'MediumOrchid':
            palhetax = 'MediumOrchid'
            palhetay = palheta['MediumOrchid']
        elif values['-COMBO-'] == 'Purple':
            palhetax = 'Purple'
            palhetay = palheta['Purple']
        elif values['-COMBO-'] == 'DarkMagenta':
            palhetax = 'DarkMagenta'
            palhetay = palheta['DarkMagenta']
        elif values['-COMBO-'] == 'Fuchsia / Magenta':
            palhetax = 'Fuchsia / Magenta'
            palhetay = palheta['Fuchsia / Magenta']
        elif values['-COMBO-'] == 'Violet':
            palhetax = 'Violet'
            palhetay = palheta['Violet']
        elif values['-COMBO-'] == 'Orchid':
            palhetax = 'Orchid'
            palhetay = palheta['Orchid']
        elif values['-COMBO-'] == 'Plum':
            palhetax = 'Plum'
            palhetay = palheta['Plum']
        elif values['-COMBO-'] == 'MediumVioletRed':
            palhetax = 'MediumVioletRed'
            palhetay = palheta['MediumVioletRed']
        elif values['-COMBO-'] == 'DeepPink':
            palhetax = 'DeepPink'
            palhetay = palheta['DeepPink']
        elif values['-COMBO-'] == 'HotPink':
            palhetax = 'HotPink'
            palhetay = palheta['HotPink']
        elif values['-COMBO-'] == 'PaleVioletRed':
            palhetax = 'PaleVioletRed'
            palhetay = palheta['PaleVioletRed']
        elif values['-COMBO-'] == 'LightPink':
            palhetax = 'LightPink'
            palhetay = palheta['LightPink']
        elif values['-COMBO-'] == 'Pink':
            palhetax = 'Pink'
            palhetay = palheta['Pink']
        elif values['-COMBO-'] == 'LightCoral':
            palhetax = 'LightCoral'
            palhetay = palheta['LightCoral']
        elif values['-COMBO-'] == 'IndianRed':
            palhetax = 'IndianRed'
            palhetay = palheta['IndianRed']
        elif values['-COMBO-'] == 'Crimson':
            palhetax = 'Crimson'
            palhetay = palheta['Crimson']
        elif values['-COMBO-'] == 'Maroon':
            palhetax = 'Maroon'
            palhetay = palheta['Maroon']
        elif values['-COMBO-'] == 'DarkRed':
            palhetax = 'DarkRed'
            palhetay = palheta['DarkRed']
        elif values['-COMBO-'] == 'FireBrick':
            palhetax = 'FireBrick'
            palhetay = palheta['FireBrick']
        elif values['-COMBO-'] == 'Brown':
            palhetax = 'Brown'
            palhetay = palheta['Brown']
        elif values['-COMBO-'] == 'Salmon':
            palhetax = 'Salmon'
            palhetay = palheta['Salmon']
        elif values['-COMBO-'] == 'DarkSalmon':
            palhetax = 'DarkSalmon'
            palhetay = palheta['DarkSalmon']
        elif values['-COMBO-'] == 'LightSalmon':
            palhetax = 'LightSalmon'
            palhetay = palheta['LightSalmon']
        elif values['-COMBO-'] == 'Coral':
            palhetax = 'Coral'
            palhetay = palheta['Coral']
        elif values['-COMBO-'] == 'Tomato':
            palhetax = 'Tomato'
            palhetay = palheta['Tomato']
        elif values['-COMBO-'] == 'Red':
            palhetax = 'Red'
            palhetay = palheta['Red']
        elif values['-COMBO-'] == 'OrangeRed':
            palhetax = 'OrangeRed'
            palhetay = palheta['OrangeRed']
        elif values['-COMBO-'] == 'DarkOrange':
            palhetax = 'DarkOrange'
            palhetay = palheta['DarkOrange']
        elif values['-COMBO-'] == 'Orange':
            palhetax = 'Orange'
            palhetay = palheta['Orange']
        elif values['-COMBO-'] == 'Gold':
            palhetax = 'Gold'
            palhetay = palheta['Gold']
        elif values['-COMBO-'] == 'Yellow':
            palhetax = 'Yellow'
            palhetay = palheta['Yellow']
        elif values['-COMBO-'] == 'Khaki':
            palhetax = 'Khaki'
            palhetay = palheta['Khaki']
        elif values['-COMBO-'] == 'AliceBlue':
            palhetax = 'AliceBlue'
            palhetay = palheta['AliceBlue']
        elif values['-COMBO-'] == 'GhostWhite':
            palhetax = 'GhostWhite'
            palhetay = palheta['GhostWhite']
        elif values['-COMBO-'] == 'Snow':
            palhetax = 'Snow'
            palhetay = palheta['Snow']
        elif values['-COMBO-'] == 'Seashell':
            palhetax = 'Seashell'
            palhetay = palheta['Seashell']
        elif values['-COMBO-'] == 'FloralWhite':
            palhetax = 'FloralWhite'
            palhetay = palheta['FloralWhite']
        elif values['-COMBO-'] == 'WhiteSmoke':
            palhetax = 'WhiteSmoke'
            palhetay = palheta['WhiteSmoke']
        elif values['-COMBO-'] == 'Beige':
            palhetax = 'Beige'
            palhetay = palheta['Beige']
        elif values['-COMBO-'] == 'OldLace':
            palhetax = 'OldLace'
            palhetay = palheta['OldLace']
        elif values['-COMBO-'] == 'Ivory':
            palhetax = 'Ivory'
            palhetay = palheta['Ivory']
        elif values['-COMBO-'] == 'Linen':
            palhetax = 'Linen'
            palhetay = palheta['Linen']
        elif values['-COMBO-'] == 'Cornsilk':
            palhetax = 'Cornsilk'
            palhetay = palheta['Cornsilk']
        elif values['-COMBO-'] == 'AntiqueWhite':
            palhetax = 'AntiqueWhite'
            palhetay = palheta['AntiqueWhite']
        elif values['-COMBO-'] == 'BlanchedAlmond':
            palhetax = 'BlanchedAlmond'
            palhetay = palheta['BlanchedAlmond']
        elif values['-COMBO-'] == 'Bisque':
            palhetax = 'Bisque'
            palhetay = palheta['Bisque']
        elif values['-COMBO-'] == 'LightYellow':
            palhetax = 'LightYellow'
            palhetay = palheta['LightYellow']
        elif values['-COMBO-'] == 'LemonChiffon':
            palhetax = 'LemonChiffon'
            palhetay = palheta['LemonChiffon']
        elif values['-COMBO-'] == 'LightGoldenrodYellow':
            palhetax = 'LightGoldenrodYellow'
            palhetay = palheta['LightGoldenrodYellow']
        elif values['-COMBO-'] == 'PapayaWhip':
            palhetax = 'PapayaWhip'
            palhetay = palheta['PapayaWhip']
        elif values['-COMBO-'] == 'PeachPuff':
            palhetax = 'PeachPuff'
            palhetay = palheta['PeachPuff']
        elif values['-COMBO-'] == 'Moccasin':
            palhetax = 'Moccasin'
            palhetay = palheta['Moccasin']
        elif values['-COMBO-'] == 'PaleGoldenrod':
            palhetax = 'PaleGoldenrod'
            palhetay = palheta['PaleGoldenrod']
        elif values['-COMBO-'] == 'MistyRose':
            palhetax = 'MistyRose'
            palhetay = palheta['MistyRose']
        elif values['-COMBO-'] == 'LavenderBlush':
            palhetax = 'LavenderBlush'
            palhetay = palheta['LavenderBlush']
        elif values['-COMBO-'] == 'Lavender':
            palhetax = 'Lavender'
            palhetay = palheta['Lavender']
        elif values['-COMBO-'] == 'Thistle':
            palhetax = 'Thistle'
            palhetay = palheta['Thistle']
        elif values['-COMBO-'] == 'Azure':
            palhetax = 'Azure'
            palhetay = palheta['Azure']
        elif values['-COMBO-'] == 'LightCyan':
            palhetax = 'LightCyan'
            palhetay = palheta['LightCyan']
        elif values['-COMBO-'] == 'PowderBlue':
            palhetax = 'PowderBlue'
            palhetay = palheta['PowderBlue']
        elif values['-COMBO-'] == 'PaleTurquoise':
            palhetax = 'PaleTurquoise'
            palhetay = palheta['PaleTurquoise']
        elif values['-COMBO-'] == 'Honeydew':
            palhetax = 'Honeydew'
            palhetay = palheta['Honeydew']
        elif values['-COMBO-'] == 'MintCream':
            palhetax = 'MintCream'
            palhetay = palheta['MintCream']

    except:
        while True:  # Event Loop
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED:
                #window.close()
                if window == window2:  # if closing win 2, mark as closed
                    window2 = None
                    window1 = make_win1()
                elif event == sg.WIN_CLOSED:
                    if window == window1:  # if closing win 1, exit program
                        break

            # ABRIR JANELA 2
            elif values['-CUST MENUBAR-'] == 'CSS' and not window2:
                window2 = make_win2()
                window1 = window1.close()
            elif values['-CUST MENUBAR-'] == 'HTML' and not window1:
                window1 = make_win1()
                window2 = window2.close()



    ########### FONTES ################

    try:
        if values['-COMBOB-'] == 'Arial1':
            fontex = 'Arial'

        elif values['-COMBOB-'] == 'Helvetica2':
            fontex = 'Helvetica'

        elif values['-COMBOB-'] == 'Verdana3':
            fontex = 'Verdana'

        elif values['-COMBOB-'] == 'Trebuchet MS4':
            fontex = 'Trebuchet MS'

        elif values['-COMBOB-'] == 'Gill Sans5':
            fontex = 'Gill Sans'

        elif values['-COMBOB-'] == 'Noto Sans6':
            fontex = 'Noto Sans'

        elif values['-COMBOB-'] == 'Avantgarde7':
            fontex = 'Avantgarde'

        elif values['-COMBOB-'] == 'Optima8':
            fontex = 'Optima'

        elif values['-COMBOB-'] == 'Arial Narrow9':
            fontex = 'Arial Narrow'

        elif values['-COMBOB-'] == 'sans-serif10':
            fontex = 'sans-serif'

        elif values['-COMBOB-'] == 'Times11':
            fontex = 'Times'

        elif values['-COMBOB-'] == 'Didot12':
            fontex = 'Didot'

        elif values['-COMBOB-'] == 'Georgia13':
            fontex = 'Georgia'

        elif values['-COMBOB-'] == 'Palatino14':
            fontex = 'Palatino'

        elif values['-COMBOB-'] == 'Bookman15':
            fontex = 'Bookman'

        elif values['-COMBOB-'] == 'New Century Schoolbook16':
            fontex = 'New Century Schoolbook'

        elif values['-COMBOB-'] == 'American Typewriter17':
            fontex = 'American Typewriter'

        elif values['-COMBOB-'] == 'serif18':
            fontex = 'serif'

        elif values['-COMBOB-'] == 'Andale Mono19':
            fontex = 'Andale Mono'

        elif values['-COMBOB-'] == 'Courier New20':
            fontex = 'Courier New'

        elif values['-COMBOB-'] == 'Courier21':
            fontex = 'Courier'

        elif values['-COMBOB-'] == 'FreeMono22':
            fontex = 'FreeMono'

        elif values['-COMBOB-'] == 'OCR A Std23':
            fontex = 'OCR A Std'

        elif values['-COMBOB-'] == 'DejaVu Sans Mono24':
            fontex = 'DejaVu Sans Mono'

        elif values['-COMBOB-'] == 'monospace25':
            fontex = 'monospace'

        elif values['-COMBOB-'] == 'Comic Sans MS26':
            fontex = 'Comic Sans MS'

        elif values['-COMBOB-'] == 'Apple Chancery27':
            fontex = 'Apple Chancery'

        elif values['-COMBOB-'] == 'Bradley Hand28':
            fontex = 'Bradley Hand'

        elif values['-COMBOB-'] == 'Brush Script MT29':
            fontex = 'Brush Script MT'

        elif values['-COMBOB-'] == 'Snell Roundhand30':
            fontex = 'Snell Roundhand'

        elif values['-COMBOB-'] == 'URW Chancery L31':
            fontex = 'URW Chancery L'

        elif values['-COMBOB-'] == 'cursive32':
            fontex = 'cursive'

        elif values['-COMBOB-'] == 'Impact33':
            fontex = 'Impact'

        elif values['-COMBOB-'] == 'Luminari34':
            fontex = 'Luminari'

        elif values['-COMBOB-'] == 'Chalkduster35':
            fontex = 'Chalkduster'

        elif values['-COMBOB-'] == 'Jazz LET36':
            fontex = 'Jazz LET'

        elif values['-COMBOB-'] == 'Blippo37':
            fontex = 'Blippo'

        elif values['-COMBOB-'] == 'Times New Roman38':
            fontex = 'Times New Roman'

        elif values['-COMBOB-'] == 'Stencil Std39':
            fontex = 'Stencil Std'

        elif values['-COMBOB-'] == 'Marker Felt40':
            fontex = 'Marker Felt'

        elif values['-COMBOB-'] == 'Trattatello41':
            fontex = 'Trattatello'
    except:
        while True:  # Event Loop
            window, event, values = sg.read_all_windows()

            if event == sg.WIN_CLOSED:
                #window.close()

                if window == window2:  # if closing win 2, mark as closed
                    window2 = None
                    window1 = make_win1()

                elif event == sg.WIN_CLOSED:
                    if window == window1:  # if closing win 1, exit program
                        break

            # ABRIR JANELA 2
            elif values['-CUST MENUBAR-'] == 'CSS' and not window2:
                window2 = make_win2()
                window1 = window1.close()
            elif values['-CUST MENUBAR-'] == 'HTML' and not window1:
                window1 = make_win1()
                window2 = window2.close()



    if escolha == True and values['-COMBO-']  != None or values['-COMBOB-'] != None or values['-COMBOC-'] != None or values['-COMBOE-'] != None:
        aspas = '"'

        if corx == fontetexto() and values['-COMBO-']  != None:

            descricao = ('{}{}{}{}{}{}'.format(corx, palhetay, aspas,'>','Texto aqui','</font>'))
            window['texto_informacao'].update(f'{descricao}')

        elif corx == Corfundo() and values['-COMBO-'] != None:
            descricao = ('{}{}{}'.format(corx, palhetay, '>'))
            window['texto_informacao'].update(f'{descricao}')

        elif corx == Cortexto() and values['-COMBO-'] != None:
            descricao = ('{}{}{}'.format(corx, palhetay, '>'))
            window['texto_informacao'].update(f'{descricao}')

        elif corx == fonte2texto() and values['-COMBOB-'] != None:
            descricao = ('{}{}{}{}{}{}'.format(corx, fontex, aspas, '>', 'Texto aqui', '</font>'))
            window['texto_informacao'].update(f'{descricao}')    # "Font Size" / '-COMBOC-'

        elif corx == fontsize() and values['-COMBOC-'] != None:

            descricao = ('{}{}{}{}{}'.format(corx, fsz, '>', 'Texto aqui', '</font>'))
            window['texto_informacao'].update(f'{descricao}')

        if fsz == fsmall() and values['-COMBOD-'] == 'small':
            descricao = ('{}'.format(fsz))
            window['texto_informacao'].update(f'{descricao}')

        elif fsz == fbig() and values['-COMBOD-'] == 'big':
            descricao = ('{}'.format(fsz))
            window['texto_informacao'].update(f'{descricao}')

        if corx == titulo() and values['-COMBOE-'] != None:
            descricao = ('{}{}{}{}{}{}{}{}'.format(corx, fsz, '>','Este é um título H', fsz,'.</h', fsz,'>'))
            window['texto_informacao'].update(f'{descricao}')

        if values['-COMBOH-'] != None and event == "Cor dos Links Visitados":
            descricao = ('{}{}{}{}{}{}{}{}{}'.format('<body link=', aspas, values['-COMBOH-'], aspas, 'vlink=', aspas, values['-COMBOH-'], aspas,'>'))
            window['texto_informacao'].update(f'{descricao}')


    #"Cor dos Links Visitados"



    if event == 'Limpar':
        descricao = ''
        window['texto_informacao'].update(f'{descricao}')
        window['texto_exemplo'].update(f'')

    if event == 'Copiar Código':
        pyperclip.copy(descricao)




    #elif event == 'Popup':
        #sg.popup('This is a BLOCKING popup','all windows remain inactive while popup active')


    #elif event == '-IN-':
       # window['-OUTPUT-'].update(f'You enetered {values["-IN-"]}')
    #elif event == 'Erase':
        #window['-OUTPUT-'].update('')
        #window['-IN-'].update('')


window.close()