
from manim import *

class PoissonDistribution(Scene):
    def construct(self):
        # Create and position the text object
        text = Text("Let's consider ", font_size=40, font="sans-serif", slant=ITALIC,color=BLUE_A)

        # Add the text object to the scene
        self.add(text)
        text.shift(LEFT*3 + UP*2)
        # Fade in the initial text
        self.play(FadeIn(text))

        # Wait for a few seconds
        self.wait(1)

        distribution_text = Text("POISSON DISTRIBUTION", font_size=30, font="sans-serif", slant=ITALIC, t2c={'POISSON DISTRIBUTION': RED})
        distribution_text.set_color_by_gradient(RED, ORANGE)  # Add gradient effect
        distribution_text.shift(UP*2.5)
        # Add the distribution text to the scene
        self.play(Transform(text, distribution_text))
        self.play(FadeOut(distribution_text))

        # Create and position the formula object
        formula = MathTex(
            r"P(X=k) =",
            r"\frac{e^{-\lambda}\lambda^k}{k!}",
            font_size=48
        )

        # Add a box around the formula
        formula_box = SurroundingRectangle(formula, buff=0.2)

        # Align the formula components
        formula.arrange(RIGHT, buff=0.2)

        # Add the formula object and the box to the scene
        self.play(Write(formula))
        self.play(Create(formula_box))

        # Scale down the box while moving it to the top left corner
        self.play(
            formula_box.animate.scale(0.7 ).shift(UP * 3 + LEFT * 5),
            formula.animate.shift(UP * 3 + LEFT * 5).scale(0.6)
        )

        # Wait for a few seconds
        self.wait(0.5)

        # Fade in the additional text
        text2 = Text("Mean = λ\n\nVariance = λ", font_size=40, font="sans-serif", slant=ITALIC, color=BLUE_B).scale(0.6)
        self.play(FadeIn(text2))
        self.wait()
        self.play(ApplyMethod(text2.shift,LEFT*5),run_time = 1.2)
        self.play(FadeOut(text2),run_time=0.5)

        text = Text("But what exactly is λ in this distribution?? ", font_size=40, font="sans-serif", slant=ITALIC,color=BLUE_A).scale(0.7)
        self.play(FadeIn(text))
        self.wait()
        self.play(ApplyMethod(text.shift,UP*1),run_time = 1.2)

        text5=Text("λ = Sequencing Coverage Depth", font_size=40, font="sans-serif", slant=ITALIC,color=YELLOW_D).scale(0.7).shift(DOWN*1)
        self.play(FadeIn(text5))
        self.wait()
        self.play(FadeOut(text5),run_time=0.5)

        text3=Text("It represents the average number of times\n\n each sequence is expected to be drawn", font_size=40, font="avant garde",color=BLUE_D).scale(0.7).shift(DOWN*1)
        self.play(FadeIn(text3))
        self.wait()
        self.play(FadeOut(text3),run_time=1.2)
        self.play(FadeOut(text),run_time=1.2)

        var = 0.0
        on_screen_var = Variable(var, Text("λ"), num_decimal_places=3).shift(RIGHT*4.3).scale(.8)
        self.play(Write(on_screen_var))
        self.wait()

        formula_box2 = SurroundingRectangle(on_screen_var, buff=0.2,color=RED)
        self.play(Create(formula_box2))

        # Add the input string
        input_string = Text("ATACACGT", font_size=40, font="sans-serif",color=PURPLE_C).scale(0.7).shift(LEFT * 3 + DOWN * 1)
        self.play(FadeIn(input_string))
        self.wait(1)

        # Define the output strings
        output_strings = ["ACacCgT", "CATACGT", "ACATACGT","TAcatGAC"]

        # Define the vertical spacing between output strings
        vertical_spacing = 1.2

        # Define the initial position for the arrows
        arrow_start = input_string.get_right()
        i=0
        j=1
        # Animate the mapping for each output string
        output_text_list = []
        arrow_list = []
        for output_string in output_strings:
            # Create the output string
            output_text = Text(output_string, font_size=40, font="sans-serif",color=GOLD).scale(0.7).shift(RIGHT*2 + UP*(1.5-i))
            i=i+1.2
            self.play(FadeIn(output_text))
            output_text_list.append(output_text)

            # Create and animate the arrow
            arrow = Arrow(arrow_start, output_text.get_left(), color=WHITE,stroke_width=2)
            self.play(Create(arrow))
            arrow_list.append(arrow)

            var_tracker = on_screen_var.tracker
            var = 0.8+j*0.54
            j=j+1
            self.play(var_tracker.animate.set_value(var))

            # Update the starting position for the next arrow
           # arrow_start = output_text.get_left()

            self.wait(1)

        # Fade out the strings, lambda value, box, and arrows
        self.play(
            FadeOut(input_string),
            FadeOut(on_screen_var),
            FadeOut(formula_box2),
            *[FadeOut(string) for string in output_text_list],
            *[FadeOut(arrow) for arrow in arrow_list],
        )

        self.wait(2)

        # Create a box to display the text and lambda value
        # Create a box to display the text
        # Create the text inside the box
        text_inside_box = Text("As λ increases", font_size=40, font="sans-serif", slant=ITALIC, color=WHITE).scale(0.6).shift(UP*1.7)

        # Create a box to display the text
        text_box = SurroundingRectangle(text_inside_box, buff=0.2, color=BLUE_B, fill_opacity=0.3)

        # Display the text inside the box
        self.play(Create(text_box), Write(text_inside_box))

        self.wait(0.5)

        text_inside_box2 = Text("More output signals are processed\n\n(READ AND SAMPLED)", font_size=40, font="sans-serif", slant=ITALIC, color=WHITE).scale(0.6).shift(DOWN * 0.4)

        text_box2 = SurroundingRectangle(text_inside_box2, buff=0.2, color=BLUE_B, fill_opacity=0.3)

        arrow1 = Arrow(text_box.get_bottom(), text_box2.get_top(), color=WHITE)

        # Create a box to display the text
        self.play(Create(arrow1))

        self.play(Create(text_box2),Write(text_inside_box2))

        

        self.wait(0.5)


        text_inside_box3 = Text("Probability of obtaining the \noriginal message is high", font_size=40, font="sans-serif", slant=ITALIC, color=WHITE).scale(0.6).shift(DOWN*2.8)

        text_box3 = SurroundingRectangle(text_inside_box3, buff=0.2,color=BLUE_B, fill_opacity=0.3)

        # Create a box to display the text
        # Create an arrow between the bottom of text_box2 and top of text_box3
        arrow2 = Arrow(text_box2.get_bottom(), text_box3.get_top(), color=WHITE)

        # Add the arrow to the scene
        self.play(Create(arrow2))

    
        self.play(Create(text_box3), Write(text_inside_box3)) 
        self.wait(0.5)

        # Fade out the strings, lambda value, boxes, and arrows
        self.play(
            FadeOut(text_box),
            FadeOut(text_inside_box),
            FadeOut(arrow1),
            FadeOut(text_box2),
            FadeOut(text_inside_box2),
            FadeOut(arrow2),
            FadeOut(text_box3),
            FadeOut(text_inside_box3),
            FadeOut(formula_box)
        )

        self.play(
            formula.animate.move_to(ORIGIN)
            # formula_box.animate.move_to(ORIGIN)
        )

        self.wait()

        expression = MathTex(r"P(X=0) =", r"e^{-\lambda} \cdot \frac{\lambda^0}{0!}", font_size=36).shift(DOWN * 2).scale(0.7)
        self.play(Write(expression, run_time=1.5))
        self.play(Transform(expression, MathTex(r"P(X=0) =", r"e^{-\lambda}", font_size=36).shift(DOWN * 2).scale(0.8)))


        self.wait()
        self.play(FadeOut(formula))

        self.play(FadeOut(expression))
        

        self.wait()

        text_ = Text("CONCLUSIONS ?? ", font_size=40, font="sans-serif", slant=ITALIC, color=WHITE)
        self.play(FadeIn(text_),run_time=1)

        self.play(FadeOut(text_),run_time=1)

        text_fin=Text("As λ increases\n ",font="sans-serif", slant=ITALIC,color=BLUE_A).scale(0.7)
        text_2=Text("the probability of retrieving the input message increases  !!",font="sans-serif", slant=ITALIC,color=BLUE_A,).scale(0.7).shift(DOWN)
        self.play(FadeIn(text_fin),run_time=1)
        self.play(FadeIn(text_2),run_time=1)
        self.wait()
# , the probability of retrieving the input signal increases  !! "