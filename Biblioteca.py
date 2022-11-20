

def Comentarios():
    comentario = f'<!--Comentário HTML aqui-->'
    return comentario

def codigoHtml():
    dic = { 'l1': '<!DOCTYPE html>', 'l2' : '<html lang="en">', 'l3' : '<head>', 'l4' : '<meta charset="UTF-8">',
            'l5' : '<meta http-equiv="X-UA-Compatible" content="IE=edge">',
            'l6' : '<meta name="viewport" content="width=device-width, initial-scale=1.0">', 'l7' : '<title>Document</title>',
            'l8' : '</head>', 'l9' : '<body>', 'l10' : '</body>', 'l11' : '</html>'}

    codigo = ('{}\n{}\n{}\n    {}\n    {}\n    {}\n    {}\n{}\n{}\n\n{}\n{}'.format(dic['l1'], dic['l2'], dic['l3'],
                                                                                    dic['l4'],dic['l5'], dic['l6'],
                                                                                    dic['l7'], dic['l8'], dic['l9'],
                                                                                    dic['l10'], dic['l11']))

    return codigo

def negrito():
    neg = f'<b>texto aqui</b>'
    return neg


def italico():
    ital = f'<i>texto aqui</i>'
    return ital

def sublinhado():
    subl = f'<u>texto aqui</u>'
    return subl

def quebralinha():
    quebral = f'<br>'
    return quebral


def Corfundo():
    Corf = f'<body bgcolor='
    return Corf

def Cortexto():
    Cort = f'<body text='
    return Cort

def espacolinhas():
    espacol = f'<p>'
    return espacol

def linhahoriz():
    linhah = f'<hr>'
    return linhah

def fontetexto():
    fontet = f'<font color="'
    return fontet

def fonte2texto():
    fontet2 = f'<font face="'
    return fontet2

def fontsize():
    fontsz = f'<font size='
    return fontsz

def fsmall():
    fs = ('{}'.format('<small>Pequeno</small>'))
    return fs

def fbig():
    big = ('{}'.format('<big>Grande</big>'))
    return big

def titulo():
    tit = ('{}'.format('<h'))
    return tit
