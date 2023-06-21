from manim import *

class ZipfFunction(Scene):
    def construct(self):
        # Create and position the text object
        text = Text("TO SUM EVERYTHING UP , LET'S TAKE UP AN EXAMPLE \n\n", font_size=40, color=YELLOW_B).scale(0.7)
        self.play(FadeIn(text), run_time=.75)

        text2 = Text("AND UNDERSTAND ENTIRE ENCODING AND STORAGE CAPACITY\n\n", font_size=40, color=YELLOW_B).scale(0.7).shift(DOWN)
        self.play(FadeIn(text2), run_time=.75)
        self.wait()
        self.play(FadeOut(text), FadeOut(text2))

        text = Text("Consider a SHUFFLING - SAMPLING CHANNEL\n\n which operates on M molecules each of length L", font_size=40, color=TEAL_A).scale(0.7)
        self.play(FadeIn(text), run_time=.75)
        self.wait()
        self.play(FadeOut(text))

        distribution_text = Text("STEP 1 : ENCODING THE INDICES ", font_size=30, font="sans-serif", slant=ITALIC)
        distribution_text.set_color_by_gradient(RED, ORANGE)  # Add gradient effect
        distribution_text.shift(UP * 2.5)
        self.play(FadeIn(distribution_text))

        text2 = Text(" Encode a distinct index in the first log M bits of each molecule\nwe need log M bits for encoding ",
                     slant=ITALIC, font_size=40, color=WHITE).scale(0.6).shift(UP)
        self.play(FadeIn(text2), run_time=.75)
        self.wait()

        text = Text(" Assume M = 8, so we have 3 bits available for the index encoding", slant=ITALIC, font_size=40, color=WHITE).scale(0.6)
        self.play(FadeIn(text), run_time=.75)
        self.wait()

        indices_values = [
            (0, "000"),
            (1, "001"),
            (2, "010"),
            (3, "011"),
            (4, "100"),
            (5, "101"),
            (6, "110"),
            (7, "111"),
        ]

        # Create and position the text objects
        k = 0.5
        text_objects = []
        for index, value in indices_values:
            text_object = MathTex(f"\\text{{Index {index}: }} {value}", font_size=36, color=WHITE)
            text_objects.append(text_object)

        for i, text_object in enumerate(text_objects):
            text_object.scale(0.6).shift(DOWN * (k))
            k = k + 0.3
            self.play(Write(text_object),run_time=0.2)


        # Fade out all elements
        self.wait(1)
        self.play(*[FadeOut(obj) for obj in [distribution_text, text2, text] + text_objects])

        distribution_text = Text("STEP 2 : REMAINING SYMBOLS FOR DATA ENCODING ", font_size=30, font="sans-serif", slant=ITALIC)
        distribution_text.set_color_by_gradient(RED, ORANGE)  # Add gradient effect
        distribution_text.shift(UP * 2.5)
        self.play(FadeIn(distribution_text))

        text2 = Text(" After encoding, we have L - log M symbols left per molecule to encode data.",
                     slant=ITALIC, font_size=40, color=WHITE).scale(0.6).shift(UP)
        self.play(FadeIn(text2), run_time=0.75)
        self.wait()

        text = Text("Assume L = 10, so we have 10 - 3 = 7 symbols remaining for data encoding", slant=ITALIC, font_size=40, color=WHITE).scale(0.6)
        self.play(FadeIn(text), run_time=0.75)
        self.wait()

        self.play(*[FadeOut(obj) for obj in [distribution_text, text2, text] ])


        distribution_text = Text("STEP 3 :DECODING AND ERASURE CHANNEL INTERPRETATION ", font_size=30, font="sans-serif", slant=ITALIC)
        distribution_text.set_color_by_gradient(RED, ORANGE)  # Add gradient effect
        distribution_text.shift(UP * 2.5)
        self.play(FadeIn(distribution_text))


        text1 = Text("Consider an erasure channel where an erasure occurs", slant=ITALIC, font_size=40, color=WHITE).scale(0.6).shift(UP)
        self.play(FadeIn(text1), run_time=0.75)
        self.wait()




        text4 = Text(" when a molecule is not drawn (Ni = 0) with probability q0.", slant=ITALIC, font_size=40, color=WHITE).scale(0.6)
        self.play(FadeIn(text4), run_time=0.75)
        self.wait()

        equation = MathTex(
            r"E\left[\frac{1}{M} \sum_{i=1}^{M} I_{\{N_i = 0\}}\right] = q_0",
            font_size=72,
            color=WHITE
        ).scale(0.7).shift(DOWN*1.2)

        self.play(FadeIn(equation))
        self.wait()


        text = Text("Assume q0 = 0.2, meaning there's a 20% chance of a molecule being not drawn.", slant=ITALIC, font_size=40, color=WHITE).scale(0.6).shift(DOWN*2.5)
        self.play(FadeIn(text), run_time=0.75)
        self.wait()

        self.play(*[FadeOut(obj) for obj in [distribution_text, text] ],FadeOut(equation),FadeOut(text1),FadeOut(text4))

        distribution_text = Text("STEP 4 : CALCULATE THE STORAGE RATE", font_size=30, font="sans-serif", slant=ITALIC)
        distribution_text.set_color_by_gradient(RED, ORANGE)  # Add gradient effect
        distribution_text.shift(UP * 2.5)
        self.play(FadeIn(distribution_text))

        text3 = Text("➣ We need to determine the number of molecules", slant=ITALIC, font_size=40, color=WHITE).scale(0.6).shift(UP)
        self.play(FadeIn(text3), run_time=0.75)
        self.wait()

        text2 = Text("that can be effectively stored and transmitted", slant=ITALIC, font_size=40, color=WHITE).scale(0.6).shift(UP*0.6)
        self.play(FadeIn(text2), run_time=0.75)
        self.wait()

        text4 = Text("➣ The number of molecules that can be transmitted is (1 - q0) * M", slant=ITALIC, font_size=40, color=WHITE).scale(0.6)
        self.play(FadeIn(text4), run_time=0.75)
        self.wait()


        text5 = Text("since each molecule has a probability of 1 - q0 of not being erased.", slant=ITALIC, font_size=40, color=WHITE).scale(0.6).shift(DOWN*0.6)
        self.play(FadeIn(text5), run_time=0.75)
        self.wait()


        text6 = Text("➣The number of symbols per transmitted molecule is (L - log M)", slant=ITALIC, font_size=40, color=WHITE).scale(0.6).shift(DOWN*1.7)
        self.play(FadeIn(text6), run_time=0.75)
        self.wait()

        text7 = Text("since we use log M bits for indexing.", slant=ITALIC, font_size=40, color=WHITE).scale(0.6).shift(DOWN*2)
        self.play(FadeIn(text7), run_time=0.75)
        self.wait()

        self.play(FadeOut(text3),FadeOut(text2),FadeOut(text4),FadeOut(text5),FadeOut(text6),FadeOut(text7),)

        equation = MathTex(
            r"\text{In our example: Storage rate} = (1 - 0.2) \times 8 \times (10 - 3) \div (8 \times 10)",
            r"= 0.8 \times 8 \times 7 \div 80 =",
            r"0.56",
            font_size=36,
            color=WHITE
        ).scale(0.7).shift(UP*2)
        
        self.play(FadeIn(equation[0]),run_time=0.75)
        self.wait()
        self.play(FadeIn(equation[1]),run_time=0.75)
        self.wait()
        self.play(FadeIn(equation[2]),run_time=0.75)
        self.wait()


        text = Text("Checking with the storage rate expression :", slant=ITALIC, font_size=40, color=WHITE).scale(0.6).shift(UP*0.5)
        self.play(FadeIn(text), run_time=0.75)
        self.wait()

        equation1 = MathTex(
            r"C = (1 - q_0) \cdot (1 - \frac{1}{\beta}) = 0.8 \cdot (1 - \frac{1}{8}) = 0.8 \cdot \frac{7}{8} = 0.56",
            font_size=36,
            color=WHITE
        ).scale(0.7)

        self.play(FadeIn(equation1))
        self.wait(2)

