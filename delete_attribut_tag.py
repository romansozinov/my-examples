text = ("<div class=\"equipment-row\">\n<div class=\"equipment-left\">\n<div class=\"equipment-title\">Базовая комплектация</div>\n<div class=\"equipment-text\"><table height=\"90\" style=\"font: 14px segoe ui\" width=\"375\">\n<tbody>\n<tr style=\"background-color:#f7f7f7\">\n<td width=\"80%\"><ul><li>Дно</li></ul></td>\n<td style=\"text-align: right\" width=\"20%\">1 шт.</td>\n</tr>\n<tr>\n<td><ul><li>Боковая стенка</li></ul></td>\n<td style=\"text-align: right\">2 шт.</td>\n</tr>\n<tr style=\"background-color:#f7f7f7\">\n<td><ul><li>Стойка</li></ul></td>\n<td style=\"text-align: right\">2 шт.</td>\n</tr>\n</tbody>\n</table></div>\n</div>\n<div class=\"equipment-right\">\n<div class=\"equipment-title\">Дополнительные товары</div>\n<div class=\"equipment-text\"><table height=\"30\" style=\"font: 14px segoe ui\" width=\"375\">\n<tbody>\n<tr style=\"background-color:#f7f7f7\">\n<td><ul><li>Сумка для переноски</li></ul></td>\n</tr>\n</tbody>\n</table></div>\n</div>\n</div>")

for tag in text.find_all():
    if 'style' in tag.attrs:
        del tag.attrs['style']

print(text)



# Вы можете использовать пакет re для соответствия атрибуту text-align: center в style. Затем вы можете удалить атрибут style, просто проверив его наличие.

# Код:

# from bs4 import BeautifulSoup as soup
# import requests
# import re

# html = """<p style="padding-left: 140pt;text-indent: 0pt;line-height: 13pt;text-align: center;">blahblah</p>
# <ul>
#     <li style="padding-left: 11pt;text-indent: 0pt;line-height: 14pt;text-align: left;">
#         <p style="display: inline;">blahblah</p>
#     </li>
#     <li style="padding-left: 11pt;text-indent: 0pt;line-height: 14pt;text-align: left;">
#          <p style="text-indent: 0pt;text-align: center;">blahblah</p>
#     </li>
# </ul>"""

# page = soup(html, 'html.parser')

# style_center = page.find_all(style=re.compile('text-align: center'))
# for style in style_center:
#     style.decompose()

# for tag in page.find_all():
#     if 'style' in tag.attrs:
#         del tag.attrs['style']

# print(page)
# ВЫХОД:

# <ul>
# <li>
# <p>blahblah</p>
# </li>
# <li>

# </li>
# </ul>