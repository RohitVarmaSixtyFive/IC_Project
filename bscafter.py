from manim import *

class BinaryMapping(Scene):
    def construct(self):

        equation = MathTex("C = (1 - q)(1 - H(p) - \\frac{1}{\\beta})")
        self.play(Create(equation))
        self.wait(3)