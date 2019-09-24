from graph import *
from random import*

global afraid
afraid=0

brushColor(220,220,220)
penColor("white")
rectangle(0,0,9999,250)
c=canvas()
brushColor("grey")
c.create_oval(50,200,300,350,fill="grey")
brushColor("white")
penColor("white")
rectangle(50,275,300,400)
penColor("black")
line (50,275,300,275)
line (57,250,296,250)
line (80,225,270,225)
line (120,210,240,210)
for i in range (-1,11):
	line (80+i*20,275,80+i*20,250)
for i in range (1,11):
	line (70+i*20,225,70+i*20,250)
for i in range (2,9):
	line (80+i*20,210,80+i*20,225)
line (195,200,195,210)
line (175,200,175,210)
line (155,200,155,210)


c.create_oval(400,300,500,700,fill='brown')
brushColor("white")
penColor("white")
rectangle(400,400,500,700)



c.create_oval(425,270,475,310,fill='brown',outline='brown')
c.create_oval(430,280,470,305,fill='grey')
c.create_oval(415,380,435,430,fill='brown',outline='brown')
c.create_oval(465,380,485,430,fill='brown',outline='brown')
c.create_oval(400,420,435,430,fill='brown',outline='brown')
c.create_oval(465,420,500,430,fill='brown',outline='brown')
brushColor(150,90,50)
penColor(150,90,50)
rectangle(400,400,500,390)
rectangle(440,390,460,310)
c.create_oval(430,330,360,340,fill='brown',outline='brown')
c.create_oval(470,330,540,340,fill='brown',outline='brown')
c.create_oval(436,286,446,293,fill='white')
c.create_oval(455,286,465,293,fill='white')
penSize(3)
penColor("black")
line(370,300,370,400)
penSize(1)

A1=polygon([(260,410),(275,390),(300,370),(340,350),(346,354),(347,360),(320,390),(285,410),(265,415)])
A2=c.create_oval(100,400,300,450,fill='brown',outline='brown')
A3=c.create_oval(80,360,140,420,fill='brown',outline='brown')
A4=c.create_oval(100,400,300,450,fill='brown',outline='brown')
d=c.create_oval(110,430,130,500,fill='brown',outline='brown')
f=c.create_oval(130,430,150,500,fill='brown',outline='brown')
b=c.create_oval(240,430,260,500,fill='brown',outline='brown')
a=c.create_oval(260,430,280,500,fill='brown',outline='brown')
A5=c.create_oval(90,380,100,390,fill='light blue')
A6=c.create_oval(120,380,130,390,fill='light blue')
A7=polygon([(95,340),(90,365),(105,360)])
A8=polygon([(120,340),(115,360),(130,365)])

def update():
	if afraid==0:
		
		if ((xCoord(a)<270)and(yCoord(a)<437)):
			moveObjectBy(a,1,0)
		elif (yCoord(a)<437):
			moveObjectBy(a,0,1)
		elif (xCoord(a)>260):
			moveObjectBy(a, -1, 0)
		elif (yCoord(a)>430):
			moveObjectBy(a,0,-1)


		if ((xCoord(b)<251)and(yCoord(b)<437)):
			moveObjectBy(b,1,0)
		elif (yCoord(b)<437):
			moveObjectBy(b,0,1)
		elif (xCoord(b)>240):
			moveObjectBy(b, -1, 0)
		elif (yCoord(b)>430):
			moveObjectBy(b,0,-1)


		if ((xCoord(d)<120)and(yCoord(d)<437)):
			moveObjectBy(d,1,0)
		elif (yCoord(d)<437):
			moveObjectBy(d,0,1)
		elif (xCoord(d)>110):
			moveObjectBy(d, -1, 0)
		elif (yCoord(d)>430):
			moveObjectBy(d,0,-1)


		if ((xCoord(f)<141)and(yCoord(f)<437)):
			moveObjectBy(f,1,0)
		elif (yCoord(f)<437):
			moveObjectBy(f,0,1)
		elif (xCoord(f)>130):
			moveObjectBy(f, -1, 0)
		elif (yCoord(f)>430):
			moveObjectBy(f,0,-1)

def hit():
	global afraid
	if randint(1, 10)<2:
		penSize(3)
		penColor("white")
		line(370,300,370,400)
		penColor("black")
		line(390,310,330,390)
		c.create_oval(430,330,360,340,fill='brown',outline='brown')
		afraid=100
	else:
		penSize(3)
		penColor("black")
		line(370,300,370,400)
		penColor("white")
		line(390,310,330,390)
		c.create_oval(430,330,360,340,fill='brown',outline='brown')
	
def mustfly():
	global afraid
	if afraid>50:
		moveObjectBy(A1, -5, 0)
		moveObjectBy(A2, -5, 0)
		moveObjectBy(A3, -5, 0)
		moveObjectBy(A4, -5, 0)
		moveObjectBy(A5, -5, 0)
		moveObjectBy(A6, -5, 0)
		moveObjectBy(A7, -5, 0)
		moveObjectBy(A8, -5, 0)
		moveObjectBy(a, -5, 0)
		moveObjectBy(b, -5, 0)
		moveObjectBy(d, -5, 0)
		moveObjectBy(f, -5, 0)
	global afraid
	if afraid<50 and afraid>0:
		moveObjectBy(A1, 5, 0)
		moveObjectBy(A2, 5, 0)
		moveObjectBy(A3, 5, 0)
		moveObjectBy(A4, 5, 0)
		moveObjectBy(A5, 5, 0)
		moveObjectBy(A6, 5, 0)
		moveObjectBy(A7, 5, 0)
		moveObjectBy(A8, 5, 0)
		moveObjectBy(a, 5, 0)
		moveObjectBy(b, 5, 0)
		moveObjectBy(d, 5, 0)
		moveObjectBy(f, 5, 0)
	global afraid
	if afraid>0:
		afraid=afraid-1

onTimer(update,50)
onTimer(hit,1000)
onTimer(mustfly, 50)


run()
