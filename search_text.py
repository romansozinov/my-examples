# поиск и вывод текста между символами

# start = 'alpha'
# end = 'bravo'
# text = 'from alpha all the way to bravo and beyond.'

# result = text.split(start)[-1].split(end)[0]

# print(result)

text_search = "<div class=\"additional-attributes-wrapper table-wrapper\"><table class=\"data table additional-attributes\" id=\"product-attribute-specs-table\"><caption class=\"table-caption\">M\u00e1s Informaci\u00f3n<\/caption><tbody> <tr><th class=\"col label\" scope=\"row\">G\u00e9nero<\/th><td class=\"col data\" data-th=\"G\u00e9nero\">Hombres<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Protecci\u00f3n UV<\/th><td class=\"col data\" data-th=\"Protecci\u00f3n UV\">100% Protecci\u00f3n UV, categor\u00eda 3<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Tipo de lente<\/th><td class=\"col data\" data-th=\"Tipo de lente\">Normal<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Ancho<\/th><td class=\"col data\" data-th=\"Ancho\">13,4 cm<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Altura<\/th><td class=\"col data\" data-th=\"Altura\">4,4 cm<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Longitud de la patilla<\/th><td class=\"col data\" data-th=\"Longitud de la patilla\">14,5 cm<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Color de la montura<\/th><td class=\"col data\" data-th=\"Color de la montura\">Dorado<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Color del Lente<\/th><td class=\"col data\" data-th=\"Color del Lente\">Verde<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Material<\/th><td class=\"col data\" data-th=\"Material\">Metal<\/td><\/tr><\/tbody><\/table><\/div> erfqefqwef qwefwqef  wefwqefwefqwefwfwef !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! <div class=\"additional-attributes-wrapper table-wrapper\"><table class=\"data table additional-attributes\" id=\"product-attribute-specs-table\"><caption class=\"table-caption\">M\u00e1s Informaci\u00f3n<\/caption><tbody> <tr><th class=\"col label\" scope=\"row\">G\u00e9nero<\/th><td class=\"col data\" data-th=\"G\u00e9nero\">Hombres<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Protecci\u00f3n UV<\/th><td class=\"col data\" data-th=\"Protecci\u00f3n UV\">100% Protecci\u00f3n UV, categor\u00eda 3<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Tipo de lente<\/th><td class=\"col data\" data-th=\"Tipo de lente\">Normal<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Ancho<\/th><td class=\"col data\" data-th=\"Ancho\">13,4 cm<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Altura<\/th><td class=\"col data\" data-th=\"Altura\">4,4 cm<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Longitud de la patilla<\/th><td class=\"col data\" data-th=\"Longitud de la patilla\">14,5 cm<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Color de la montura<\/th><td class=\"col data\" data-th=\"Color de la montura\">Dorado<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Color del Lente<\/th><td class=\"col data\" data-th=\"Color del Lente\">Verde<\/td><\/tr> <tr><th class=\"col label\" scope=\"row\">Material<\/th><td class=\"col data\" data-th=\"Material\">Metal<\/td><\/tr><\/tbody><\/table><\/div>"

start = "<div class=\"additional-attributes-wrapper table-wrapper\">"
end = "<\/div>"
text = (str(text_search).split(start)[-1].split(end)[0]) 
print(type(text))
print(text) # NDL2894

    