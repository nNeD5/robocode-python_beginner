#!/usr/bin/env python3


import turtle


class TurtleController:
    def __init__(self) -> None:
        self._run = True
        self._input = []
        self.PENCIL = turtle.Turtle()
        self.SCREEN = turtle.getscreen()
        self.SCREEN.bgcolor("#181818")
        self.PENCIL.color("white")
        self.pos_questions = {
            "rectangle": [
                "Enter left bottom point [x] [y]\n> ",
                "Enter height and width [height] [width]\n> ",
            ],
            "circle": [
                "start point [x] [y]\n> ",
                "Enter radius [radius]\n> "],
            "triangle": [
                "Enter first point [x] [y]\n> ",
                "Enter second point [x] [y]\n> ",
                "Enter third point [x] [y]\n> ",
            ],
        }

    def _get_input(self):
        item = input("> ")
        self._input.append(item)

    def draw_triangle(self):
        pos = []
        for question in self.pos_questions["triangle"]:
            pos.append(input(question))
        x_0, y_0 = map(float, pos[0].split())
        pos.pop(0)
        self.PENCIL.penup()
        self.PENCIL.goto(x_0, y_0)
        self.PENCIL.pendown()
        for p in pos:
            x, y = map(float, p.split())
            self.PENCIL.goto(x, y)
        x, y = map(float, pos[0].split())
        self.PENCIL.goto(x_0, y_0)
        print("tirangle complete")

    def draw_circle(self):
        pos = []
        for question in self.pos_questions["circle"]:
            pos.append(input(question))
        x, y = map(float, pos[0].split())
        self.PENCIL.penup()
        self.PENCIL.goto(x, y)
        self.PENCIL.pendown()

        self.PENCIL.circle(float(pos[1]))
        print("circle complete")

    def draw_rectangle(self):
        pos = []
        for question in self.pos_questions["rectangle"]:
            pos.append(input(question))

        # move to start pos
        x, y = map(float, pos[0].split())
        self.PENCIL.penup()
        self.PENCIL.goto(x, y)
        self.PENCIL.pendown()

        height, width = map(float, pos[1].split())

        print(height, width)
        self.PENCIL.forward(width)
        self.PENCIL.left(90)
        self.PENCIL.forward(height)
        self.PENCIL.left(90)
        self.PENCIL.forward(width)
        self.PENCIL.left(90)
        self.PENCIL.forward(height)
        print("rectangle complete")

    def begin_screen(self):
        self.PENCIL.write(
            """
                          Type 'exit' to exit
                          Type 'circle' to draw circle
                          Type 'rectangle' to draw rectangle
                          All other will render as text
                          (garbge input -> garbage output)
                          """,
            align="center",
            font=("Arial", 20, "bold"),
        )

    def main(self):
        self.begin_screen()
        while self._run:
            self._get_input()
            item = self._input.pop()

            self.PENCIL.clear()
            self.PENCIL.color("white")
            if item == "exit":
                self._run = False
            elif item == "circle":
                self.draw_circle()
            elif item == "triangle":
                self.draw_triangle()
            elif item == "rectangle":
                self.draw_rectangle()
            else:
                self.PENCIL.write(item, align="center", font=("Arial", 20, "bold"))


if __name__ == "__main__":
    TurtleController().main()
