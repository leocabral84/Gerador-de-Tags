import PySimpleGUI as sg
import pyperclip
from Biblioteca import *


palheta = {'Black' : '#000000', 'grey11' : '#1C1C1C', 'grey21': '#363636', 'grey31': '#4F4F4F', 'DimGray': '#696969',
             'Gray': '#808080', 'DarkGray': '#A9A9A9', 'Silver': '#C0C0C0', 'LightGrey': '#D3D3D3', 'Gainsboro': '#DCDCDC',
             'SlateBlue': '#6A5ACD', 'SlateBlue1': '#836FFF', 'SlateBlue3': '#6959CD', 'DarkSlateBlue': '#483D8B',
           'MidnightBlue':	'#191970', 'Navy': '#000080', 'DarkBlue': '#00008B', 'MediumBlue':'#0000CD',
           'Blue':	'#0000FF', 'CornflowerBlue':'#6495ED', 'RoyalBlue': '#4169E1', 'DodgerBlue': '#1E90FF',
           'DeepSkyBlue': '#00BFFF', 'LightSkyBlue': '#87CEFA', 'SkyBlue':	'#87CEEB',
           'LightBlue':	'#ADD8E6', 'SteelBlue':	'#4682B4', 'LightSteelBlue': '#B0C4DE',
           'SlateGray': '#708090', 'LightSlateGray': '#778899', 'Aqua / Cyan':	'#00FFFF',
           'DarkTurquoise': '#00CED1', 'Turquoise':	'#40E0D0', 'MediumTurquoise': '#48D1CC', 'LightSeaGreen': '#20B2AA',
           'DarkCyan': '#008B8B', 'Teal':	'#008080', 'Aquamarine': '#7FFFD4', 'MediumAquamarine': '#66CDAA',
           'CadetBlue':'#5F9EA0', 'DarkSlateGray': '#2F4F4F', 'MediumSpringGreen': '#00FA9A', 'SpringGreen': '#00FF7F',
           'PaleGreen': '#98FB98', 'LightGreen': '#90EE90', 'DarkSeaGreen':	'#8FBC8F', 'MediumSeaGreen':'#3CB371',
           'SeaGreen': '#2E8B57', 'DarkGreen': '#006400', 'Green': '#008000', 'ForestGreen': '#228B22',
           'LimeGreen': '#32CD32', 'Lime':	'#00FF00', 'LawnGreen': '#7CFC00', 'Chartreuse': '#7FFF00',
           'GreenYellow': '#ADFF2F', 'YellowGreen': '#9ACD32', 'OliveDrab': '6B8E23', 'DarkOliveGreen': '#556B2F',
           'Olive': '#808000', 'DarkKhaki': '#BDB76B', 'Goldenrod': '#DAA520', 'DarkGoldenrod': '#B8860B',
           'SaddleBrown': '#8B4513', 'Sienna': '#A0522D', 'RosyBrown': '#BC8F8F', 'Peru':	'#CD853F',
           'Chocolate': '#D2691E', 'SandyBrown': '#F4A460', 'NavajoWhite': '#FFDEAD', 'Wheat': '#F5DEB3',
           'BurlyWood': '#DEB887', 'Tan': '#D2B48C', 'MediumSlateBlue': '#7B68EE', 'MediumPurple':	'#9370DB',
           'BlueViolet': '#8A2BE2', 'Indigo': '#4B0082', 'DarkViolet': '#9400D3', 'DarkOrchid': '#9932CC',
           'MediumOrchid':	'#BA55D3', 'Purple': '#A020F0', 'DarkMagenta': '#8B008B', 'Fuchsia / Magenta': '#FF00FF',
           'Violet': '#EE82EE', 'Orchid': '#DA70D6', 'Plum': '#DDA0DD', 'MediumVioletRed': '#C71585',
           'DeepPink': '#FF1493', 'HotPink': '#FF69B4', 'PaleVioletRed': '#DB7093', 'LightPink': '#FFB6C1',
           'Pink':	'#FFC0CB', 'LightCoral': '#F08080', 'IndianRed': '#CD5C5C', 'Crimson': '#DC143C',
           'Maroon': '#800000', 'DarkRed': '#8B0000', 'FireBrick': '#B22222', 'Brown': '#A52A2A',
           'Salmon': '#FA8072', 'DarkSalmon': '#E9967A', 'LightSalmon': '#FFA07A', 'Coral': '#FF7F50',
           'Tomato': '#FF6347', 'Red': '#FF0000', 'OrangeRed': '#FF4500', 'DarkOrange': '#FF8C00',
           'Orange': '#FFA500', 'Gold':	'#FFD700', 'Yellow': '#FFFF00', 'Khaki': '#F0E68C',
           'AliceBlue': '#F0F8FF', 'GhostWhite': '#F8F8FF', 'Snow': '#FFFAFA',
           'Seashell': '#FFF5EE', 'FloralWhite': '#FFFAF0', 'WhiteSmoke': '#F5F5F5', 'Beige': '#F5F5DC',
           'OldLace': '#FDF5E6', 'Ivory': '#FFFFF0', 'Linen': '#FAF0E6', 'Cornsilk': '#FFF8DC',
           'AntiqueWhite':	'#FAEBD7', 'BlanchedAlmond': '#FFEBCD', 'Bisque': '#FFE4C4', 'LightYellow': '#FFFFE0',
           'LemonChiffon':	'#FFFACD', 'LightGoldenrodYellow': '#FAFAD2',
           'PapayaWhip': '#FFEFD5', 'PeachPuff': '#FFDAB9', 'Moccasin': '#FFE4B5',
           'PaleGoldenrod': '#EEE8AA', 'MistyRose': '#FFE4E1', 'LavenderBlush': '#FFF0F5',
           'Lavender': '#E6E6FA', 'Thistle': '#D8BFD8', 'Azure': '#F0FFFF', 'LightCyan': '#E0FFFF',
           'PowderBlue': '#B0E0E6', 'PaleTurquoise': '#E0FFFF', 'Honeydew': '#F0FFF0', 'MintCream': '#F5FFFA'}



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
def make_win1():

    layout = [
    [sg.MenubarCustom([['Linguagem', ['HTML', ]]],  k='-CUST MENUBAR-',p=0)] if use_custom_titlebar else [sg.Menu([['Linguagem', ['HTML', ]]],  k='-CUST MENUBAR-',p=0)],
    [sg.Text("ESCOLHA A OPÇÃO DE TAG A BAIXO", pad=(300, 0))],
    [sg.Button("Código HTML"), sg.Button("Comentários"), sg.Button("Negrito"), sg.Button("Itálico")],
    [sg.Text("ESCOLHA A COR", pad=(5, 0))],
    [sg.Combo(cores, k='-COMBO-', default_value= 'MintCream')],
    [sg.Button("Cor da Página"), sg.Button("Cor do texto")],
    [sg.Text("", key="texto_informacao", size=(100,10), pad=(0, 40))],
    [sg.Button("Copiar Código"), sg.Button("Limpar"), sg.Button("Cancelar")],

]
    return sg.Window("Dicionário do Programador by LeoCabral", layout, resizable = True)


def make_win2():
    layout = [[sg.Text('Segunda Janela')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text(size=(25,1), k='-OUTPUT-')],
              [sg.Button('Erase'), sg.Button('Popup'), sg.Button('Exit')]]
    return sg.Window('Second Window', layout, finalize=True)

window1, window2 = make_win1(), None





descricao = ''

while True:
    windows, evento, valores = sg.read_all_windows()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        window.close()
        if window == window2:  # if closing win 2, mark as closed
            window2 = None
        elif window == window1:  # if closing win 1, exit program
            break



    if evento == "Código HTML":
        descricao = codigoHtml()
        window['texto_informacao'].update(f'{descricao}')
    if evento == "Comentários":
        descricao = Comentarios()
        window['texto_informacao'].update(f'{descricao}')
    if evento == "Negrito":
        descricao = negrito()
        window['texto_informacao'].update(f'{descricao}')
    if evento == "Itálico":
        descricao = italico()
        window['texto_informacao'].update(f'{descricao}')

    # TROCA ENTRE FUNÇÕES DE COLORIR FUNDO DA PÁGINA, TEXTO...

    corx = ''
    escolha = False
    if evento == "Cor da Página":
        corx = Corfundo()
        escolha = True
    elif evento == "Cor do texto":
        corx = Cortexto()
        escolha = True

    # ESCOLHA DE CORES

    if escolha == True and valores['-COMBO-'] == 'Black':
        descricao = ('{}{}{}'.format(corx, palheta['Black'],'>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'grey11':
        descricao = ('{}{}{}'.format(corx, palheta['grey11'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'grey21':
        descricao = ('{}{}{}'.format(corx, palheta['grey21'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'grey31':
        descricao = ('{}{}{}'.format(corx, palheta['grey31'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DimGray':
        descricao = ('{}{}{}'.format(corx, palheta['DimGray'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Gray':
        descricao = ('{}{}{}'.format(corx, palheta['Gray'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkGray':
        descricao = ('{}{}{}'.format(corx, palheta['DarkGray'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Silver':
        descricao = ('{}{}{}'.format(corx, palheta['Silver'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LightGrey':
        descricao = ('{}{}{}'.format(corx, palheta['LightGrey'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Gainsboro':
        descricao = ('{}{}{}'.format(corx, palheta['Gainsboro'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'SlateBlue':
        descricao = ('{}{}{}'.format(corx, palheta['SlateBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'SlateBlue1':
        descricao = ('{}{}{}'.format(corx, palheta['SlateBlue1'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'SlateBlue3':
        descricao = ('{}{}{}'.format(corx, palheta['SlateBlue3'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkSlateBlue':
        descricao = ('{}{}{}'.format(corx, palheta['DarkSlateBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'MidnightBlue':
        descricao = ('{}{}{}'.format(corx, palheta['MidnightBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkBlue':
        descricao = ('{}{}{}'.format(corx, palheta['DarkBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'MidnightBlue':
        descricao = ('{}{}{}'.format(corx, palheta['MidnightBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Navy':
        descricao = ('{}{}{}'.format(corx, palheta['Navy'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkBlue':
        descricao = ('{}{}{}'.format(corx, palheta['DarkBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'MediumBlue':
        descricao = ('{}{}{}'.format(corx, palheta['MediumBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Blue':
        descricao = ('{}{}{}'.format(corx, palheta['Blue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'CornflowerBlue':
        descricao = ('{}{}{}'.format(corx, palheta['CornflowerBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'RoyalBlue':
        descricao = ('{}{}{}'.format(corx, palheta['RoyalBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DodgerBlue':
        descricao = ('{}{}{}'.format(corx, palheta['DodgerBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DeepSkyBlue':
        descricao = ('{}{}{}'.format(corx, palheta['DeepSkyBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LightSkyBlue':
        descricao = ('{}{}{}'.format(corx, palheta['LightSkyBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'SkyBlue':
        descricao = ('{}{}{}'.format(corx, palheta['SkyBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LightBlue':
        descricao = ('{}{}{}'.format(corx, palheta['LightBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'SteelBlue':
        descricao = ('{}{}{}'.format(corx, palheta['SteelBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LightSteelBlue':
        descricao = ('{}{}{}'.format(corx, palheta['LightSteelBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'SlateGray':
        descricao = ('{}{}{}'.format(corx, palheta['SlateGray'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LightSlateGray':
        descricao = ('{}{}{}'.format(corx, palheta['LightSlateGray'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Aqua / Cyan':
        descricao = ('{}{}{}'.format(corx, palheta['Aqua / Cyan'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkTurquoise':
        descricao = ('{}{}{}'.format(corx, palheta['DarkTurquoise'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Turquoise':
        descricao = ('{}{}{}'.format(corx, palheta['Turquoise'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'MediumTurquoise':
        descricao = ('{}{}{}'.format(corx, palheta['MediumTurquoise'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LightSeaGreen':
        descricao = ('{}{}{}'.format(corx, palheta['LightSeaGreen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkCyan':
        descricao = ('{}{}{}'.format(corx, palheta['DarkCyan'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Teal':
        descricao = ('{}{}{}'.format(corx, palheta['Teal'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Aquamarine':
        descricao = ('{}{}{}'.format(corx, palheta['Aquamarine'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'MediumAquamarine':
        descricao = ('{}{}{}'.format(corx, palheta['MediumAquamarine'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'CadetBlue':
        descricao = ('{}{}{}'.format(corx, palheta['CadetBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkSlateGray':
        descricao = ('{}{}{}'.format(corx, palheta['DarkSlateGray'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'MediumSpringGreen':
        descricao = ('{}{}{}'.format(corx, palheta['MediumSpringGreen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'SpringGreen':
        descricao = ('{}{}{}'.format(corx, palheta['SpringGreen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'PaleGreen':
        descricao = ('{}{}{}'.format(corx, palheta['PaleGreen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LightGreen':
        descricao = ('{}{}{}'.format(corx, palheta['LightGreen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkSeaGreen':
        descricao = ('{}{}{}'.format(corx, palheta['DarkSeaGreen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'MediumSeaGreen':
        descricao = ('{}{}{}'.format(corx, palheta['MediumSeaGreen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'SeaGreen':
        descricao = ('{}{}{}'.format(corx, palheta['SeaGreen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkGreen':
        descricao = ('{}{}{}'.format(corx, palheta['DarkGreen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Green':
        descricao = ('{}{}{}'.format(corx, palheta['Green'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'ForestGreen':
        descricao = ('{}{}{}'.format(corx, palheta['ForestGreen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LimeGreen':
        descricao = ('{}{}{}'.format(corx, palheta['LimeGreen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Lime':
        descricao = ('{}{}{}'.format(corx, palheta['Lime'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LawnGreen':
        descricao = ('{}{}{}'.format(corx, palheta['LawnGreen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Chartreuse':
        descricao = ('{}{}{}'.format(corx, palheta['Chartreuse'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'GreenYellow':
        descricao = ('{}{}{}'.format(corx, palheta['GreenYellow'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'YellowGreen':
        descricao = ('{}{}{}'.format(corx, palheta['YellowGreen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'OliveDrab':
        descricao = ('{}{}{}'.format(corx, palheta['OliveDrab'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkOliveGreen':
        descricao = ('{}{}{}'.format(corx, palheta['DarkOliveGreen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Olive':
        descricao = ('{}{}{}'.format(corx, palheta['Olive'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkKhaki':
        descricao = ('{}{}{}'.format(corx, palheta['DarkKhaki'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Goldenrod':
        descricao = ('{}{}{}'.format(corx, palheta['Goldenrod'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkGoldenrod':
        descricao = ('{}{}{}'.format(corx, palheta['DarkGoldenrod'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'SaddleBrown':
        descricao = ('{}{}{}'.format(corx, palheta['SaddleBrown'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Sienna':
        descricao = ('{}{}{}'.format(corx, palheta['Sienna'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'RosyBrown':
        descricao = ('{}{}{}'.format(corx, palheta['RosyBrown'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Peru':
        descricao = ('{}{}{}'.format(corx, palheta['Peru'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Chocolate':
        descricao = ('{}{}{}'.format(corx, palheta['Chocolate'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'SandyBrown':
        descricao = ('{}{}{}'.format(corx, palheta['SandyBrown'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'NavajoWhite':
        descricao = ('{}{}{}'.format(corx, palheta['NavajoWhite'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Wheat':
        descricao = ('{}{}{}'.format(corx, palheta['Wheat'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'BurlyWood':
        descricao = ('{}{}{}'.format(corx, palheta['BurlyWood'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Tan':
        descricao = ('{}{}{}'.format(corx, palheta['Tan'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'MediumSlateBlue':
        descricao = ('{}{}{}'.format(corx, palheta['MediumSlateBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'MediumPurple':
        descricao = ('{}{}{}'.format(corx, palheta['MediumPurple'],'>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'BlueViolet':
        descricao = ('{}{}{}'.format(corx, palheta['BlueViolet'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Indigo':
        descricao = ('{}{}{}'.format(corx, palheta['Indigo'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkViolet':
        descricao = ('{}{}{}'.format(corx, palheta['DarkViolet'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkOrchid':
        descricao = ('{}{}{}'.format(corx, palheta['DarkOrchid'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'MediumOrchid':
        descricao = ('{}{}{}'.format(corx, palheta['MediumOrchid'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Purple':
        descricao = ('{}{}{}'.format(corx, palheta['Purple'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkMagenta':
        descricao = ('{}{}{}'.format(corx, palheta['DarkMagenta'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Fuchsia / Magenta':
        descricao = ('{}{}{}'.format(corx, palheta['Fuchsia / Magenta'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Violet':
        descricao = ('{}{}{}'.format(corx, palheta['Violet'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Orchid':
        descricao = ('{}{}{}'.format(corx, palheta['Orchid'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Plum':
        descricao = ('{}{}{}'.format(corx, palheta['Plum'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'MediumVioletRed':
        descricao = ('{}{}{}'.format(corx, palheta['MediumVioletRed'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DeepPink':
        descricao = ('{}{}{}'.format(corx, palheta['DeepPink'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'HotPink':
        descricao = ('{}{}{}'.format(corx, palheta['HotPink'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'PaleVioletRed':
        descricao = ('{}{}{}'.format(corx, palheta['PaleVioletRed'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LightPink':
        descricao = ('{}{}{}'.format(corx, palheta['LightPink'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Pink':
        descricao = ('{}{}{}'.format(corx, palheta['Pink'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LightCoral':
        descricao = ('{}{}{}'.format(corx, palheta['LightCoral'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'IndianRed':
        descricao = ('{}{}{}'.format(corx, palheta['IndianRed'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Crimson':
        descricao = ('{}{}{}'.format(corx, palheta['Crimson'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Maroon':
        descricao = ('{}{}{}'.format(corx, palheta['Maroon'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkRed':
        descricao = ('{}{}{}'.format(corx, palheta['DarkRed'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'FireBrick':
        descricao = ('{}{}{}'.format(corx, palheta['FireBrick'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Brown':
        descricao = ('{}{}{}'.format(corx, palheta['Brown'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Salmon':
        descricao = ('{}{}{}'.format(corx, palheta['Salmon'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkSalmon':
        descricao = ('{}{}{}'.format(corx, palheta['DarkSalmon'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LightSalmon':
        descricao = ('{}{}{}'.format(corx, palheta['LightSalmon'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Coral':
        descricao = ('{}{}{}'.format(corx, palheta['Coral'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Tomato':
        descricao = ('{}{}{}'.format(corx, palheta['Tomato'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Red':
        descricao = ('{}{}{}'.format(corx, palheta['Red'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'OrangeRed':
        descricao = ('{}{}{}'.format(corx, palheta['OrangeRed'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'DarkOrange':
        descricao = ('{}{}{}'.format(corx, palheta['DarkOrange'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Orange':
        descricao = ('{}{}{}'.format(corx, palheta['Orange'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Gold':
        descricao = ('{}{}{}'.format(corx, palheta['Gold'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Yellow':
        descricao = ('{}{}{}'.format(corx, palheta['Yellow'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Khaki':
        descricao = ('{}{}{}'.format(corx, palheta['Khaki'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'AliceBlue':
        descricao = ('{}{}{}'.format(corx, palheta['AliceBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'GhostWhite':
        descricao = ('{}{}{}'.format(corx, palheta['GhostWhite'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Snow':
        descricao = ('{}{}{}'.format(corx, palheta['Snowa'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Seashell':
        descricao = ('{}{}{}'.format(corx, palheta['Seashell'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'FloralWhite':
        descricao = ('{}{}{}'.format(corx, palheta['FloralWhite'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'WhiteSmoke':
        descricao = ('{}{}{}'.format(corx, palheta['WhiteSmoke'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Beige':
        descricao = ('{}{}{}'.format(corx, palheta['Beige'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'OldLace':
        descricao = ('{}{}{}'.format(corx, palheta['OldLace'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Ivory':
        descricao = ('{}{}{}'.format(corx, palheta['Ivory'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Linen':
        descricao = ('{}{}{}'.format(corx, palheta['Linen'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Cornsilk':
        descricao = ('{}{}{}'.format(corx, palheta['Cornsilk'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'AntiqueWhite':
        descricao = ('{}{}{}'.format(corx, palheta['AntiqueWhite'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'BlanchedAlmond':
        descricao = ('{}{}{}'.format(corx, palheta['BlanchedAlmond'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Bisque':
        descricao = ('{}{}{}'.format(corx, palheta['Bisque'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LightYellow':
        descricao = ('{}{}{}'.format(corx, palheta['LightYellow'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LemonChiffon':
        descricao = ('{}{}{}'.format(corx, palheta['LemonChiffon'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LightGoldenrodYellow':
        descricao = ('{}{}{}'.format(corx, palheta['LightGoldenrodYellow'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'PapayaWhip':
        descricao = ('{}{}{}'.format(corx, palheta['PapayaWhip'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'PeachPuff':
        descricao = ('{}{}{}'.format(corx, palheta['PeachPuff'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Moccasin':
        descricao = ('{}{}{}'.format(corx, palheta['Moccasin'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'PaleGoldenrod':
        descricao = ('{}{}{}'.format(corx, palheta['PaleGoldenrod'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'MistyRose':
        descricao = ('{}{}{}'.format(corx, palheta['MistyRose'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LavenderBlush':
        descricao = ('{}{}{}'.format(corx, palheta['LavenderBlush'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Lavender':
        descricao = ('{}{}{}'.format(corx, palheta['Lavender'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Thistle':
        descricao = ('{}{}{}'.format(corx, palheta['Thistle'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Azure':
        descricao = ('{}{}{}'.format(corx, palheta['Azure'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'LightCyan':
        descricao = ('{}{}{}'.format(corx, palheta['LightCyan'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'PowderBlue':
        descricao = ('{}{}{}'.format(corx, palheta['PowderBlue'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'PaleTurquoise':
        descricao = ('{}{}{}'.format(corx, palheta['PaleTurquoise'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'Honeydew':
        descricao = ('{}{}{}'.format(corx, palheta['Honeydew'], '>'))
        window['texto_informacao'].update(f'{descricao}')

    elif escolha == True and valores['-COMBO-'] == 'MintCream':
        descricao = ('{}{}{}'.format(corx, palheta['MintCream'], '>'))
        window['texto_informacao'].update(f'{descricao}')



    if evento == 'Limpar':
        descricao = ''
        window['texto_informacao'].update(f'{descricao}')

    if evento == 'Copiar Código':
        pyperclip.copy(descricao)


windows.close()


