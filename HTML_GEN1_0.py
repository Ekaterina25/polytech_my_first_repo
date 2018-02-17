def is_hex(_str):
    if _str[0] == '#':
        _num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'a', 'b', 'c', 'd', 'e', 'f']
        _temp = _str[1:len(_str)]
        for _i in _temp:
            if not (_i in _num):
                return 1
        return 0
    return 1

def set_parameter(_text, _avalaible_par, _par='0'):
    while (not (_par.lower() in _avalaible_par) and is_hex(_par.lower())):
        _par = input(_text + ': ')
        if (not (_par.lower() in _avalaible_par) and is_hex(_par.lower())):
            print('Не удалось распознать введеный параметр')
        else:
            if not is_hex(_par.lower()):
                return _par.upper()
            else:
                return _par.lower()

def create_html(_output, _tittle, _bckg_clr, _txt_clr, _hdr_algn, _hdr_h,
                _hdr_clr, _tittl_clr, _cntnt, _cntnt_algn, _brd_style):
    _output.write('''<!DOCTYPE html>
<html>
<head>
    <title>'''+_tittle+'''</title>
    <style type="text/css">
    body
    {
        background-color: '''+_bckg_clr+''';
    } p{
        color: '''+_txt_clr+''';
    } header{
        height: ''' +_hdr_h+ ''';
        background: ''' +_hdr_clr+ ''';
        text-align: '''+_hdr_algn+''';
        padding-left: 10px;;
       } #logo {
        display: block;
        padding: 0;
        font: bold 60px/50px 'PT Serif',Tahoma,Verdana,Segoe,sans-serif;
        color: '''+_tittl_clr+''';
        text-decoration: none;
        letter-spacing: -.02em;
    } #header{
        height: 50px;
        margin: auto;
    } footer{
        background-color: '''+_bckg_clr+''';
        color: #EAFF00;
        text-align: center;
    } .content{
        background-color: '''+_bckg_clr+''';
        border-style:'''+_brd_style+''';
        border-width: 1px;
        border-color: darkgrey;
        min-height: 600px;
        width: 1024px;
        margin: 0 auto;
        text-align:'''+_cntnt_algn+'''
    }
    #box{
        padding:20px;
    }
    </style>
</head>
<body>
<header>
<div id="box">
<div id="header">
    <a id="logo">'''+_tittle+'''</a></div>
</div>
</header>
<div class="content">
<p>'''+_cntnt+'''</p>
</div>
<footer>
</footer>
</body>
</html>''')

colors = ['white', 'black', 'green', 'yellow', 'red', 'blue', 'grey', 
          'brown', 'violet', 'purple', 'pink']
aligns = ['left', 'right', 'center']
border_styles = ['none', 'hidden', 'dotted', 'dashed', 'solid', 'double',
                 'groove', 'ridge', 'inset', 'outset']

with open('Generated.html', 'w') as html:
    print('''Вас приветствует HTML_GEN 1.0!
По заданным вами параметрами будет сгенерирована HTML страница
ПРИМЕЧАНИЕ: цвет можно задать в виде его названия на английском или в 16-ричной форме''')
    tittle = input('Введите заголовок страницы: ')
    background_color = set_parameter('Введите цвет фона(16-ичный формат недопустим)', colors)
    text_color = set_parameter('Введите цвет текста', colors)
    header_align = set_parameter('Задайте выравнивание шапки', aligns)
    header_height = input('Введите высоту шапки: ')
    header_color = set_parameter('Введите цвет фона шапки', colors)
    tittle_color = set_parameter('Введите цвет текста шапки', colors)
    content = input('Введите содержание сайта:\n')
    content_align = set_parameter('Введите выравнивание контента', aligns)
    border_style = set_parameter('Введите стиль границы вокруг контента', border_styles)
    create_html(html, tittle, background_color, text_color, header_align,
                header_height, header_color, tittle_color, content, content_align, border_style);
