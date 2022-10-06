#Importando dados
import turtle

wn = turtle.Screen()
wn.title("Pong por Eduardo S.") #Título do Jogo
wn.bgcolor("black") #Fundo do jogo
wn.setup(width=800, height=600) #Tamanho da tela do jogo
wn.tracer(0) #Parece que a tela não atualiza da um boost no jogo.

#Score
score_a = 0
score_b = 0

# Traço da esquerda
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") #O formato do traço
paddle_a.color("white") #A cor do traço
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #É como se fossem as setas para cima e para baixo, neste caso para cima
paddle_a.goto(-350, 0)


# Traço da direita
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") #O formato do traço
paddle_b.color("white") #A cor do traço
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #É como se fossem as setas para cima e para baixo, neste caso para cima
paddle_b.goto(350, 0)


# Bola
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") #O formato do traço
ball.color("white") #A cor do traço
ball.penup() #É como se fossem as setas para cima e para baixo, neste caso para cima
ball.goto(0, 0)
ball.dx = 0.2 #X do plano cartesiano
ball.dy = 0.2 #Y do plano cartesiano

#Lápis
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


#Funções do jogo
def paddle_a_up():
    y = paddle_a.ycor() #Esta função é usada para retornar a coordenada da posição atual. Não requer nenhum argumento.
    y += 20 #y recebe ele mesmo + 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # Esta função é usada para retornar a coordenada da posição atual. Não requer nenhum argumento.
    y -= 20  # y recebe ele mesmo + 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor() #Esta função é usada para retornar a coordenada da posição atual. Não requer nenhum argumento.
    y += 20 #y recebe ele mesmo + 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # Esta função é usada para retornar a coordenada da posição atual. Não requer nenhum argumento.
    y -= 20  # y recebe ele mesmo + 20
    paddle_b.sety(y)

# vinculação do teclado
wn.listen()
wn.onkeypress(paddle_a_up, "w") #Aqui diz, quando eu apertar " W ", chama a função PADDLE_A_UP para fazer o traço subir
wn.onkeypress(paddle_a_down, "s") #Aqui diz, quando eu apertar " S ", chama a função PADDLE_A_DOWN para fazer o traço descer

wn.onkeypress(paddle_b_up, "Up") #Aqui diz, quando eu apertar " Up ", chama a função PADDLE_B_UP para fazer o traço subir
wn.onkeypress(paddle_b_down, "Down") #Aqui diz, quando eu apertar " Down ", chama a função PADDLE_B_DOWN para fazer o traço descer


#Loop do jogo principal
while True: #Toda vez que for VERDADE
    wn.update()


    #Mover a bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Borda Superior e Inferior
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #Borda Esquerda e Direita
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Borda Esquerda e Direita
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #Colisões da bola e dos traços
    if (ball.xcor()  > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor()  < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

