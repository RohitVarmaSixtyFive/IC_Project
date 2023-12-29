from manim import *


class ZipfFunction(Scene):
    def construct(self):
        # Create and position the text object
        text = Text("LET'S TRY TO PROVE THE\n\n", font_size=40,
                    color=YELLOW_B).scale(1).shift(UP)
        # self.play(FadeIn(text), run_time=1.5)

        text2 = Text("STOARGE CAPACITY FOR NOISE - FREE CHANNEL\n\n",
                     font_size=40, color=YELLOW_B).scale(0.7)
        self.play(FadeIn(text), FadeIn(text2), run_time=1)
        # self.wait()

        self.play(FadeOut(text), FadeOut(text2), run_time=0.5)

        text3 = Text("THEOREM STATEMENT :\n", font_size=40,
                     color=MAROON_C).scale(0.9).shift(UP*2)
        self.play(FadeIn(text3), run_time=0.5)
        # self.wait()
        # self.play(FadeOut(text))

        text4 = Text("The storage capacity of the noise-free shuffling-sampling channel is\n",
                     font_size=40, slant=ITALIC, color=BLUE_A).scale(0.7).shift(UP)
        self.play(FadeIn(text4), run_time=0.5)
        # self.wait()
        formula8 = MathTex(
            "C = (1 - q)(1 - \\frac{1}{\\beta})",
            font_size=72,
            color=WHITE
        ).scale(0.5).shift(DOWN*0.7)

        # # # Add a box around the formula
        formula_box = SurroundingRectangle(formula8, buff=0.2)

        self.play(FadeIn(formula8))
        self.play(Create(formula_box))
        text5 = Text("In particular, if β ≤ 1, no positive rate is achievable\n",
                     font_size=40, slant=ITALIC, color=BLUE_A).scale(0.6).shift(DOWN*2)
        self.play(FadeIn(text5), run_time=1)
        self.wait(1)
        # Scale down the box while moving it to the top left corner
        self.play(FadeOut(text3), FadeOut(text4), FadeOut(text5), run_time=1)

        self.play(
            formula_box.animate.scale(0.8).shift(UP*4),
            formula8.animate.shift(UP * 4).scale(0.8)
        )

        # # Wait for a few seconds
        # self.wait(0.5)

        text2 = Text(" ➣ Encode a distinct index in the first log M bits of each molecule\n",
                     slant=ITALIC, font_size=40, color=WHITE).scale(0.6).shift(UP*1.2)
        self.play(FadeIn(text2), run_time=1.5)
        #######################################
        corona = ImageMobject("DNA.png")
        corona.scale(1.2).shift(DOWN)
        self.add(corona)
        self.wait(1)
        d_arrow = DoubleArrow(start=corona.get_left(), end=corona.get_right(),
                              color=RED_E)
        d_arrow.next_to(corona, DOWN)
        d_arrow_up = DoubleArrow(start=LEFT, end=RIGHT, color=RED_E)
        d_arrow_up.next_to(corona, UP).shift(RIGHT)
        l_uplabel = Tex("logM")
        l_uplabel.next_to(d_arrow_up, UP)
        l_label = Tex("L")
        l_label.next_to(d_arrow, DOWN)
        self.wait(0.2)
        self.play(LaggedStart(Create(d_arrow),
                              Write(l_label),
                              Create(d_arrow_up),
                              Write(l_uplabel),
                              lag_ratio=0.25,
                              run_time=2))
        self.add(l_label)
        self.add(l_uplabel)
        self.wait()
        brace = Brace(VGroup(l_label, l_uplabel), UP).next_to(
            corona, UP).shift(LEFT*1.3)
        label = Tex("L - logM").next_to(brace, UP)
        self.play(FadeOut(text2))
        self.play(LaggedStart(Create(brace), Write(label),lag_ratio = 0.25))
        text3 = Text(" ➣Then we have L - log M symbols left per molecule to encode data.",
                     slant=ITALIC, font_size=40, color=WHITE).scale(0.6).shift(UP*1.2)
        self.play(FadeIn(text3), run_time=1.5)
        self.wait()
        self.play(FadeOut(text3))
        text4 = Text("➣ ERASURE CHANNEL - when a molecule is not drawn (Ni = 0) with probability q0.",
                     slant=ITALIC, font_size=40, color=WHITE).scale(0.5).shift(UP*1.2)
        self.play(FadeIn(text4), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(corona), FadeOut(l_uplabel),
                  FadeOut(l_label), FadeOut(brace),
                  FadeOut(label),
                  FadeOut(d_arrow),FadeOut(d_arrow_up),
                  )
##############################################################################################################
        equation = MathTex(
            r"E\left[\frac{1}{M} \sum_{i=1}^{M} I_{\{N_i = 0\}}\right] = q_0",
            font_size=72,
            color=PURPLE_B
        ).scale(0.7).shift(DOWN*0.01)
        self.play(FadeIn(equation))
        self.wait(2)
        self.play(FadeOut(text4))
        self.play(FadeOut(formula8), FadeOut(formula_box),
                  FadeOut(equation) )
        formula = MathTex(
            r"\text{Storage Capacity} = \frac{\text{Amount of Data Recovered}}{\text{Total Amount of Data}}",
            color=WHITE
        ).shift(UP*3+LEFT*3).scale(0.7)

        self.play(FadeIn(formula))

        formula2 = MathTex(
            r"= \frac{(1 - q_0) \cdot M \cdot \left(L - \log(M)\right)}{ML}"
        ).scale(0.7).shift(UP*1.8 + LEFT * 2.5)

        self.play(FadeIn(formula2))

        text_side = Text("We know that", slant=ITALIC, font_size=40,
                         color=WHITE).scale(0.5).shift(UP + RIGHT*3)
        self.play(FadeIn(text_side), run_time=1.5)
        self.wait()
        formula_side = MathTex(
            r"\frac{L}{\log(M)} = \beta"
        ).shift(RIGHT*3 + UP*0.3).scale(0.7)
        self.play(FadeIn(formula_side), run_time=1.5)

        formula2 = MathTex(
            r"So \, \frac{L - \log(M)}{L}"
        ).shift(RIGHT*3 + DOWN*0.6).scale(0.7)

        self.play(FadeIn(formula2), run_time=1.5)

        formula3 = MathTex(
            r" = 1 - \left(\frac{\log(M)}{L}\right)"
        ).shift(RIGHT*3 + DOWN*1.5).scale(0.7)

        self.play(FadeIn(formula3), run_time=1.5)

        formula4 = MathTex(
            r" = 1 - \frac{1}{\beta}"
        ).shift(RIGHT*2.7 + DOWN*2.4).scale(0.7)

        self.play(FadeIn(formula4), run_time=1.5)

        formula_box_side = SurroundingRectangle(
            VGroup(text_side, formula_side, formula2, formula3, formula4), buff=0.2)

        self.play(Create(formula_box_side), run_time=1.5)
        self.wait()

        formula = MathTex(
            r" = (1 - q_0) \cdot \frac{L - \log(M)}{L}"
        ).scale(0.7).shift(UP*0.5 + LEFT * 2.7)

        self.play(FadeIn(formula))

        formula3 = MathTex(
            "=  (1 - q)(1 - \\frac{1}{\\beta})",
            font_size=72,
            color=WHITE
        ).scale(0.5).shift(DOWN*0.7 + LEFT * 3)

        self.play(FadeIn(formula3))

        formula_box_side2 = SurroundingRectangle(
            formula3, buff=0.2, color=MAROON_C)

        self.play(Create(formula_box_side2), run_time=1.5)
        self.wait(1)
