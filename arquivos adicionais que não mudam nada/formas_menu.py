import turtle

t = turtle.Turtle()

print("1 - Quadrado")
print("2 - Triângulo")

op = input("Escolha: ")

if op == "1":
    for _ in range(4):
        t.forward(100)
        t.right(90)

elif op == "2":
    for _ in range(3):
        t.forward(100)
        t.left(120)

turtle.done()