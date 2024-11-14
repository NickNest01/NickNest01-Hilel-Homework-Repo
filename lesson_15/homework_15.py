class Rombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Rombus side must be greater that 0")

        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Angle can't be less than 0 or greater than 180")
            self.angle_b = 180 - value

        super().__setattr__(name, value)

figure = Rombus(10, 90)
print(figure.side_a)
print(figure.angle_a)
print(figure.angle_b)