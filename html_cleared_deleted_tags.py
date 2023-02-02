from bs4 import BeautifulSoup

html = """
<div id="description-block" class="full-width"><h3>Descripción del producto - Grifo de lavabo con cuerpo liso L20 Roca</h3><div><div><strong>Descripción del producto:</strong></div><div>&nbsp;</div><ul><li>Grifo&nbsp;monomando de lavabo de 11,5cm de largo x 14,2cm de alto.</li><li>Enlaces de alimentación flexibles incluídos. &nbsp; &nbsp; &nbsp;&nbsp;</li><li>Acabado: cromado.</li><li>Manecilla XL. &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</li><li>Ahorro de agua y energía.</li><li>Sistema Cold Start, de apertura frontal en agua fría.</li><li>Caudal de 5l/min a 3 bares. &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</li><li>Tipo de aireador: coin slot.</li><li>Tipo de cartucho: cerámico. &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</li><li>Tipo de instalación: de repisa.</li></ul><p></p><div id="sc4pProduct"><div class="sc4pMC sc4pLine"><p> <strong>Marca:</strong></p><p>El tejido comercial de <strong>Roca</strong> se ensancha por más de un centenar de estados a lo largo del planeta. Es una de las firmas más famosas en la creación de espacios de baños. A día de hoy, Roca es un ejemplo a nivel internacional.</p></div><div class="sc4pFC sc4pLine"><p><strong>Garantía de 5 años:</strong></p><p>Dispondrá de una garantía de amplia cobertura, la cual llega a los <b>cinco años</b> ante cualquier daño del fabricante que ocurra durante el empleo apropiado del producto.</p></div></div><style>.sc4pLine {
            margin-bottom: 25px;
        }</style><p class="referencecombseo"> <strong>SKU:</strong> 8433290340549</p><style>.referencecombseo {
        margin: 15px 0;
    }</style></div></div>
"""

soup = BeautifulSoup(html, 'html.parser')

for tag in soup.find_all("p", class_='referencecombseo'): # удалить тег <p class="referencecombseo"> с его содержимым
    tag.decompose()
    
for tag in soup.find_all("style"): # удалить все теги style
    tag.decompose()  
      
for tag in soup(lambda tag: tag.name == 'p' and not tag.text.strip()): # В этом примере, мы применяем soup(lambda tag: tag.name == 'p' and not tag.text.strip()) для нахождения всех тегов p с пустым содержимым. Далее, мы используем decompose() для удаления найденных тегов.
    tag.decompose()
    
for tag in soup.find_all(): # удалить все классы и id в html тегах
    tag.attrs = {}    

# for match in soup.findAll("div"): # удалить все div теги. [:-1] - удалить только первый тег div
#     match.replaceWithChildren()
                
new_html = (soup.prettify()) # .prettify() - formatting HTML code
print(new_html.replace("<div id=\"description-block\" class=\"full-width\">", ""))
