import pygame as py
from sys import exit
import numpy as np

def barra(rect,bar,n,lis,name,label):
    mouse = py.mouse.get_pressed()

    if mouse[0] == True:
        t = py.mouse.get_pos()
        if rect.collidepoint(t):

            p = rect.x - t[0]
            d = abs(p)
            if py.key.get_pressed()[py.K_RIGHT]==1:
                p+=1

            if label[0] == 1:
                bar.fill('Pink')
                bar.fill('Red', (0, 0, (d /bar.get_width()) * bar.get_width(), bar.get_height()))
            if label[0] == 2:
                bar.fill('yellow')
                bar.fill('red', (0, 0, (d /bar.get_width()) * bar.get_width(), bar.get_height()))
            if label[0] == 3:
                bar.fill('blue')
                bar.fill('red', (0, 0, (d /bar.get_width()) * bar.get_width(), bar.get_height()))
            if label[0] == 4:
                bar.fill('gray')
                bar.fill('red', (0, 0, (d /bar.get_width()) * bar.get_width(), bar.get_height()))
            if n == 0:
                lis[n] = round((d /bar.get_width()),5)
                name[n] = round((d /bar.get_width()),5)
            else :
                lis[n] = round(4*(d /bar.get_width())-2,5)
                name[n] = round(4*(d /bar.get_width())-2,5)

    return lis
def reset(re,va,kne) :
    mouse = py.mouse.get_pressed()

    if mouse[0] == True:
        t = py.mouse.get_pos()
        if re.collidepoint(t):
            va = kne[:]
            screen.fill((0,0,0))
            x=[0]
            y=[0]
    return va

def scale(n,m,flo,bu):
    mouse = py.mouse.get_pressed()

    if mouse[0] == True:
        t = py.mouse.get_pos()
        if m.collidepoint(t):
            n.fill("gray")
            p = m.x - t[0]+0.0001
            d = abs(p)
            n.fill('blue', (0, 0, (d / n.get_width()) * n.get_width(), n.get_height()))
            if bu == True:
                flo = round(10* (d / n.get_width()), 2)

    return flo
def desloc1(re,va):
    mouse = py.mouse.get_pressed()

    if mouse[0] == True:
        t = py.mouse.get_pos()
        if re.collidepoint(t):
            va+=5
            screen.fill((0, 0, 0))
            x = [0]
            y = [0]
    return va
def desloc2(re,va):
    mouse = py.mouse.get_pressed()

    if mouse[0] == True:
        t = py.mouse.get_pos()
        if re.collidepoint(t):
            va+=-5
            screen.fill((0, 0, 0))
            x = [0]
            y = [0]
    return va


py.init()
bul = True
clock = py.time.Clock()
screen = py.display.set_mode((1200,800), py.RESIZABLE)
knew1 = [0]*7
knew2 = [0]*7
knew3 = [0]*7
knew4 = [0]*7
surf=py.Surface((1,1))
tela = py.image.load('venv/iii.jpeg').convert_alpha()
tela = py.transform.scale(tela, (800,800))

val1 = [0.01,0,0,0,0.16,0,0]
val2 = [0.86,0.85,0.04,-0.04,0.85,0,1.6]
val3 = [0.93,0.20,-0.26,0.23,0.22,0,1.6]
val4 = [1,-0.15,0.28,0.26,0.24,0,0.44]
x = [0]
y = [0]

cont=0
mat=[]
lab = ['p','a','b','c','d','e','f']

lab2=[]
lab2_rec = []
for c in range(4):
    mat.append([c+1,[],[],[0]*7,[],[]])

botao = py.Surface((50,50))
botao.fill("Red")
botao_rect = botao.get_rect(midbottom = (625,155))
text_font = py.font.Font(None,25)
text_font1 = py.font.Font(None,25)
tex = text_font.render("Clear",True,'white').convert_alpha()
cont1=0
cima = py.Surface((50,50))
cima.fill("red")
cima_rec = cima.get_rect(midbottom = (625,220))
text_font2 = py.font.Font(None,50)
baixo = py.Surface((50,50))
baixo.fill("red")
baixo_rec = cima.get_rect(midbottom = (625,280))
tex1 = text_font2.render("/\ ",True,'white').convert_alpha()
tex2 = text_font2.render("\/",True,'white').convert_alpha()

dire = py.Surface((50,50))
dire.fill("red")
dire_rec = dire.get_rect(midbottom = (625,350))
text_font2 = py.font.Font(None,50)
esque = py.Surface((50,50))
esque.fill("red")
esque_rec = esque.get_rect(midbottom = (625,420))
tex3 = text_font2.render("->",True,'white').convert_alpha()
tex4 = text_font2.render("<-",True,'white').convert_alpha()

for lista in mat:
    cont1+=1
    for c in range(7):
        lista[5].append(py.Surface((300, 10)))
        lista[4].append(lista[5][c].get_rect(midbottom =(900,30+15*c+120*cont1)))
        if cont1==1:
            lista[5][c].fill('pink')
        if cont1==2:
            lista[5][c].fill('yellow')
        if cont1==3:
            lista[5][c].fill('blue')
        if cont1==4:
            lista[5][c].fill('gray')
        lab2.append(text_font1.render(str(lab[c]),True,'white'))
        lista[1].append(text_font.render(str(lista[3][c]),True,'white'))
        lista[2].append(lista[1][c].get_rect(midbottom =(1060,35+15*c+120*cont1) ))
        lab2_rec.append(lab2[c].get_rect(midbottom = (1060-320,35+15*c+120*cont1-2)))

scal = py.Surface((300,10))
scal.fill("white")
scal_rec = scal.get_rect(midbottom = (900,60))

point = py.Surface((1,1))
point.fill((200,200,200))
rec_point = point.get_rect(midbottom =(400,300))
ecran = py.Surface((400,300))
rec_ecran = ecran.get_rect(midbottom =(400,800))
mult = 1
x1,y1=400,720
while True:
    for event in py.event.get():

        if event.type == py.QUIT:
            py.quit()
            exit()

    screen.blit(point, rec_point)
    screen.blit(tela,(730,0))
    screen.blit(botao,botao_rect)
    screen.blit(tex,(602,122))
    screen.blit(scal,scal_rec)
    screen.blit(cima,cima_rec)
    screen.blit(baixo,baixo_rec)
    screen.blit(tex1,(615,180))
    screen.blit(tex2,(615,235))
    screen.blit(esque,esque_rec)
    screen.blit(dire,dire_rec)
    screen.blit(tex3,((612,305)))
    screen.blit(tex4, (612,375))
    cont2=0
    for k in range(7):
        mat[0][1][k]= (text_font.render(str(mat[0][3][k]), True, 'white')).convert_alpha()
        screen.blit(mat[0][5][k],mat[0][4][k])
        screen.blit(mat[0][1][k],mat[0][2][k])
        screen.blit(lab2[k],lab2_rec[k])
        knew1 = barra(mat[0][4][k],mat[0][5][k],k,knew1,mat[0][3],mat[0])
    for k in range(7):
        mat[1][1][k]= (text_font.render(str(mat[1][3][k]), True, 'white')).convert_alpha()
        screen.blit(mat[1][5][k],mat[1][4][k])
        screen.blit(mat[1][1][k],mat[1][2][k])
        screen.blit(lab2[k+7], lab2_rec[k+7])
        knew2 = barra(mat[1][4][k],mat[1][5][k],k,knew2,mat[1][3],mat[1])
    for k in range(7):
        mat[2][1][k]= (text_font.render(str(mat[2][3][k]), True, 'white')).convert_alpha()
        screen.blit(mat[2][5][k],mat[2][4][k])
        screen.blit(mat[2][1][k],mat[2][2][k])
        screen.blit(lab2[k+14], lab2_rec[k+14])
        knew3 = barra(mat[2][4][k],mat[2][5][k],k,knew3,mat[2][3],mat[2])
    for k in range(7):
        mat[3][1][k]= (text_font.render(str(mat[3][3][k]), True, 'white')).convert_alpha()
        screen.blit(mat[3][5][k],mat[3][4][k])
        screen.blit(mat[3][1][k],mat[3][2][k])
        screen.blit(lab2[k+21], lab2_rec[k+21])
        knew4 = barra(mat[3][4][k],mat[3][5][k],k,knew4,mat[3][3],mat[3])


    val1 = reset(botao_rect,val1,knew1)
    val2 = reset(botao_rect,val2,knew2)
    val3 = reset(botao_rect, val3, knew3)
    val4 = reset(botao_rect, val4, knew4)

    rd = np.random.random()
    mult = scale(scal,scal_rec,mult,bul)
    if 0 < rd < val1[0]:
        x[0] = val1[1] * x[0] + val1[2] * y[0] - val1[5]*100*mult/1.5
        y[0] = val1[3] * x[0] + val1[4] * y[0] -  val1[6]*100*mult/1.5
        point.fill("white")

    if val1[0] < rd < val2[0]:
        x[0] = val2[1] * x[-1] + val2[2] * y[-1] - val2[5] * 100*mult / 1.5
        y[0] = val2[3] * x[-1] + val2[4] * y[-1] - val2[6] * 100 *mult/ 1.5
        point.fill("green")
    if val2[0] < rd < val3[0]:
        x[0] = val3[1] * x[-1] + val3[2] * y[-1] - val3[5] * 100*mult / 1.5
        y[0] = val3[3] * x[-1] + val3[4] * y[-1] - val3[6] * 100*mult/ 1.5
        point.fill("red")
    if val3[0] < rd < val4[0]:
        x[0] = val4[1] * x[-1] + val4[2] * y[-1] - val4[5] * 100*mult / 1.5
        y[0] = val4[3] * x[-1] + val4[4] * y[-1] - val4[6] * 100*mult/ 1.5
        point.fill("green")
    rec_point.x=x[0]+x1
    rec_point.y=y[0]+y1
    x1, y1 = desloc1(dire_rec,x1), desloc1(baixo_rec,y1)
    x1, y1 = desloc2(esque_rec,x1), desloc2(cima_rec, y1)
    clock.tick(500)
    py.display.update()
