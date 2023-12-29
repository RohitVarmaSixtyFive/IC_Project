from manim import *

class BinaryMapping(Scene):
    def construct(self):

        distribution = MathTex("Q \\sim \\text{Bern}(q_0)")       
        self.play(FadeIn(distribution))
        self.wait(3)
        self.play(FadeOut(distribution))
        topic = Tex("BINARY SYMMENTRIC CHANNEL",color=YELLOW_E).scale(1.5)
        # topic2=Tex("BSC",color=YELLOW_E).scale(1.5)

        self.play(Write(topic),run_time=1)
        # self.wait()
        self.play(FadeOut(topic),run_time=0.5)
        
        # self.play(Transform(topic,topic2))
        # self.wait()
        # self.play(Write(topic2),run_time=1)
        # self.play(FadeOut(topic2),run_time=0.5)

        text=Tex("ENCODER",color=YELLOW_A).to_edge(LEFT).shift(UP*3).shift(RIGHT*1).scale(0.5)
        self.play(Write(text),run_time=1)
        # self.wait(0.5)


        source = Dot(LEFT, color=BLUE).to_edge(LEFT).shift(RIGHT*2).scale(0.5).shift(UP*2)
        destination_0 = Dot(RIGHT * 2.5 + UP * 2, color=MAROON_C).scale(0.5)


        input_bit = MathTex("0").next_to(source, UP*0.2, buff=1).scale(0.5)
        output_bit_0 = MathTex("0").next_to(destination_0, UP*0.1, buff=1).scale(0.5)
        

        self.add(source, destination_0, input_bit)

        arrow_0 = Arrow(source.get_center(), destination_0.get_center(), buff=0.3, color=BLUE_C, stroke_width=3)
        arrow_label_0 = Tex(f"1 - p").next_to(arrow_0, UP*0.05, buff=0.3).scale(0.5)

        text=Tex("DECODER",color=YELLOW_C).to_edge(RIGHT).shift(UP*3).shift(LEFT*2.5).scale(0.5)
        self.play(Write(text),run_time=1)
        # self.wait(0.5)

        self.play(GrowArrow(arrow_0),run_time=0.5)
        # self.wait(0.5)
        self.play(Write(output_bit_0),run_time=0.5)

        # self.wait(0.5)

        self.play(Write(arrow_label_0),run_time=0.5)
        # self.wait(0.5)




 
        # source = Dot(LEFT, color=BLUE).to_edge(LEFT).shift(RIGHT*2).scale(0.5).shift(UP*1)
        destination_0 = Dot(RIGHT * 2.5 + DOWN * 2, color=MAROON_C).scale(0.5)


        #input_bit = MathTex("0").next_to(source, UP*0.2, buff=1).scale(0.5)
        output_bit_0 = MathTex("1").next_to(destination_0, UP*0.1, buff=1).scale(0.5)
        

        self.add(source, destination_0, input_bit)

        arrow_0 = Arrow(source.get_center(), destination_0.get_center(), buff=0.3, color=BLUE_C, stroke_width=3)
        arrow_label_0 = Tex(f"p").scale(0.5).shift(LEFT*1).shift(DOWN*0.75)


        self.play(GrowArrow(arrow_0),run_time=0.75)
        # self.wait(0.5)
        self.play(Write(arrow_label_0),run_time=0.75)
        # self.wait(0.5)

        self.play(Write(output_bit_0),run_time=0.75)

        # self.wait(0.5)



        source = Dot(LEFT, color=BLUE).to_edge(LEFT).shift(RIGHT*2+DOWN*3).scale(0.5).shift(UP*1)
        destination_0 = Dot(RIGHT * 2.5 + DOWN * 2, color=MAROON_C).scale(0.5)


        input_bit = MathTex("1").next_to(source, UP*0.2, buff=1).scale(0.5)
        output_bit_0 = MathTex("1").next_to(destination_0, UP*0.1, buff=1).scale(0.5)
        

        self.add(source, destination_0, input_bit)

        arrow_0 = Arrow(source.get_center(), destination_0.get_center(), buff=0.3, color=BLUE_C, stroke_width=3)
        arrow_label_0 = Tex(f"1 - p").scale(0.5).shift(LEFT*1).shift(DOWN*2.3)


        self.play(GrowArrow(arrow_0),run_time=0.75)
        # self.wait(0.5)
        self.play(Write(arrow_label_0),run_time=0.75)
        # self.wait(0.5)
        # self.play(Write(output_bit_0))
        # self.wait(0.5)
        #source = Dot(LEFT, color=BLUE).to_edge(LEFT).shift(RIGHT*2+DOWN*3).scale(0.5).shift(UP*1)
        destination_0 = Dot(RIGHT * 2.5 + UP* 2, color=MAROON_C).scale(0.5)
        #input_bit = MathTex("1").next_to(source, UP*0.2, buff=1).scale(0.5)
        #output_bit_0 = MathTex("1").next_to(destination_0, UP*0.1, buff=1).scale(0.5)
        self.add(source, destination_0, input_bit)

        arrow_0 = Arrow(source.get_center(), destination_0.get_center(), buff=0.3, color=BLUE_C, stroke_width=3)
        # arrow_label_0 = Tex(f"1-p").scale(0.5).shift(LEFT*1).shift(DOWN*1)
        self.play(GrowArrow(arrow_0),run_time=0.75)
        # self.wait(0.5)
        # self.play(Write(arrow_label_0))
        # self.wait(0.5)
        self.play(Write(output_bit_0),run_time=0.75)
        self.wait(1)
        # everything = VGroup(*self.mobjects)
        # self.play(FadeOut(everything))
        
        


        



