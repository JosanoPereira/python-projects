import turtle


def desenha(t, tam):
    for i in ['white', 'red', 'green', 'black']:
        t.color(i)
        t.forward(tam)
        t.left(90)


wi = turtle.Screen()
wi.bgcolor('blue')

atr = turtle.Turtle()
atr.pensize(4)

tamanho = 20
for i in range(25):
    desenha(atr, tamanho)
    tamanho += 5
    atr.forward(10)
    atr.right(18)

wi.exitonclick()