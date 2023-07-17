from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import glob

pasta = "cartoes"
cartoes = glob.glob(f"{pasta}/*")#Pega o nome de todos os arquivos dentro da pasta

def cm_to_pt(centimetros):#transforma a medida em centimetros
    pontos = centimetros * 28.35
    return pontos

def desenhe(c, cartoes):
    x_start, y_start = 3, 50  # Posição inicial para desenhar as imagens
    x, y = x_start, y_start  # Variáveis para acompanhar a posição atual
    line_height = 185  # Altura de cada linha
    images_per_line = 2  # Quantidade de imagens por linha
    images_per_page = 8  # Quantidade de imagens por página
    for idx, cartao in enumerate(cartoes):
        c.drawImage(f"{cartao}", x,y, width=cm_to_pt(10.32), height=cm_to_pt(5.77))
        x +=297
        if(idx+1)%images_per_line ==0:
            x=x_start
            y+=line_height
        if(idx+1)%images_per_page==0:
            c.showPage()
            x, y = x_start, y_start
    if len(cartoes)%images_per_page != 0:
        c.showPage()

   


c = canvas.Canvas("Impressoes.pdf", pagesize=A4)#Cria o pdf
desenhe(c, cartoes)
c.save()

