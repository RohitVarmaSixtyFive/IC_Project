
from manim import *

class zipffunction(Scene):
    def construct(self):
        # Create and position the text object
        text = Text("WHAT'S THE DISTRIBUTION USED IN CASE OF     \n \n          ", font_size=40, color=BLUE_C).scale(0.7)
        noisy_channel_text = Text("NOISY CHANNEL ?? ", font_size=40, color=RED).scale(0.7)
        text.next_to(noisy_channel_text, UP)

        # Add the text objects to the scene
        self.add(text, noisy_channel_text)

        # Fade in the initial text
        self.play(FadeIn(text), FadeIn(noisy_channel_text))

        # Wait for a few seconds
        self.wait(1)
        self.play(FadeOut(noisy_channel_text),FadeOut(text))

        distribution_text = Text(" ZIPF DISTRIBUTION ", font_size=40, font="sans-serif", t2c={'POISSON DISTRIBUTION': YELLOW_B})
        distribution_text.set_color_by_gradient(YELLOW_B, ORANGE)  # Add gradient effect
        distribution_text.shift(UP*3.5)

        # Add the distributon text to the scene
        self.play(FadeIn(distribution_text))

        # Just make "NOISY CHANNEL" in a different colo

        self.wait(1)




        # # Create and position the formula object

        # Create and position the formula object
        formula8 = MathTex(
            "C = (1 - q)(1 - \\frac{1}{\\beta})",
            font_size=72,
            color=WHITE
        ).scale(0.7)

        # Add the formula object to the scene
        # self.play(Write(formula))

        # Wait for a few seconds
        # self.wait(3)

        # # Add a box around the formula
        formula_box = SurroundingRectangle(formula8, buff=0.2)

        # # Align the formula components
        formula8.arrange(RIGHT, buff=0.2)

        # # Add the formula object and the box to the scene
        self.play(Write(formula8))
        self.play(Create(formula_box))

        # Scale down the box while moving it to the top left corner
        self.play(
            formula_box.animate.scale(0.6 ).shift(UP * 2.5 + LEFT * 4.3),
            formula8.animate.shift(UP * 2.5 + LEFT * 4.3).scale(0.5)
        )

        # # Wait for a few seconds
        self.wait(0.5)


#to the number of copies drawn from each sequence        # Q follows a discrete distribution that assigns probabilities to the number of copies drawn from each sequence

        text2 = Text(" ➣ Q follows a discrete distribution that assigns probabilities", font_size=40, color=BLUE_A).scale(0.5).shift(UP*1)
        self.play(FadeIn(text2),run_time=1.5)
        text3=Text("to the number of copies drawn from each sequence", font_size=40, color=BLUE_A).scale(0.5).shift(UP*0.7)
        self.play(FadeIn(text3),run_time=1.5)
        self.wait()
        text4 = Text(" ➣ The Zipf distribution is a discrete power law distribution", font_size=40, color=BLUE_A).scale(0.5).shift(UP*0.05)
        self.play(FadeIn(text4),run_time=1.5)
        text5 = Text(" ➣ Few items are extremely common and the majority are rare", font_size=40, color=BLUE_A).scale(0.5).shift(DOWN*0.7)
        self.play(FadeIn(text5),run_time=1.5)

        self.play(FadeOut(text2, text3, text4, text5))

        text6 = Text("  ➣ The probability mass function of the Zipf distribution", font_size=40, color=BLUE_A).scale(0.5).shift(UP*1)
        self.play(FadeIn(text6),run_time=1.5)
        formula1 = MathTex(
            "P(Q=k) = \\frac{1}{k^s \\cdot H(M, s)}",
            font_size=72,
            color=WHITE
        )
        formula1.scale(0.5).shift(UP*0.2)

        # Add the formula object to the scene
        self.play(Write(formula1))

        # Wait for a few seconds
        self.wait()

        text7 = Text(" ➣ k = no of copies ", font_size=40, color=BLUE_A).scale(0.5).shift(DOWN*0.7)
        self.play(FadeIn(text7),run_time=1.5)
        text8=Text(" ➣ s = parameter = concentration of drawn copies ", font_size=40, color=BLUE_A).scale(0.5).shift(DOWN*1.2)
        self.play(FadeIn(text8),run_time=1.5)
        self.wait()
        text9 = Text(" ➣  H(M, s) is the generalized harmonic number which is defined as : ", font_size=40, color=BLUE_A).scale(0.5).shift(DOWN*1.7)
        self.play(FadeIn(text9),run_time=1.5)
        formula = MathTex(
            "H(M, s) = 1^{-s} + 2^{-s} + 3^{-s} + \\ldots + M^{-s}",
            font_size=72,
            color=WHITE
        )
        formula.scale(0.6).shift(DOWN*2.7)

        # Add the formula object to the scene
        self.play(Write(formula),run_time=2)

        # text11=Text(" ➣ s = parameter = concentration of drawn copies ", font_size=40, color=BLUE_A).scale(0.5).shift(DOWN*3.4)
        # self.play(FadeIn(text11),run_time=1.5)


        self.play(FadeOut(text7, text8, text9, formula,formula,formula1,text6,formula8,formula_box))


        text12=Text(" QUICK EXAMPLE OF ZIPF DISTRIBUTION  ", font_size=40, color=BLUE_A).scale(0.5)
        self.play(FadeIn(text12),run_time=1.5)

        self.play(FadeOut(text12))

        text13 = Text(" ➣ The probability P(k) of selecting k copies, where k ranges from 1 to 100 ", font_size=40, color=BLUE_A).scale(0.5).shift(UP*2)
        self.play(FadeIn(text13),run_time=1.5)

        text14 = Text(" ➣ Assume s = 1.5 ", font_size=40, color=BLUE_A).scale(0.5).shift(UP*1)
        self.play(FadeIn(text14),run_time=1.5)

        formula3 = MathTex(
            "H = 1^{-s} + 2^{-s} + 3^{-s} + \\ldots + 100^{-s}",
            font_size=48,
            color=WHITE
        ).scale(0.5).shift(UP*0.4)

        self.play(FadeIn(formula3),run_time=1.5)  

        probabilities = [
            MathTex("P(1) \\approx 0.013"),
            MathTex("P(2) \\approx 0.006"),
            MathTex("P(3) \\approx 0.004"),
            MathTex("P(4) \\approx 0.003"),
            MathTex("P(5) \\approx 0.002"),
            MathTex("P(6) \\approx 0.002"),
            MathTex("P(7) \\approx 0.001"),
            MathTex("P(8) \\approx 0.001"),
            MathTex("P(9) \\approx 0.001"),
            MathTex("P(10) \\approx 0.001"),
        ]

        j=0.2
        for i, probability in enumerate(probabilities):
            probability.scale(0.5).shift(DOWN*j)
            j=j+0.3
            self.play(Write(probability),run_time=0.1)

        # Wait for a few seconds
        self.wait(3)





