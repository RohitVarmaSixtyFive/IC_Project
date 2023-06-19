from manim import *

class DisplayList1(Scene):
    def construct(self):
        name = Tex("TRANSMITTED INPUTS").to_edge(UL, buff=0.5).scale(0.6)
        self.play(Write(name),run_time=1)

        string_list = ["ACATACGT", "CATGTACA", "GCTATGCC"]
        colors = [BLUE, YELLOW, GREEN_B]
        text_objects = []

        max_width = 0
        max_height = 0

        for i, string in enumerate(string_list):
            text = Text(string, color=colors[i]).scale(0.5)
            text.to_edge(LEFT)
            text.shift(RIGHT * len(string_list) / 2)
            text.shift(UP * (1 - i) * 2)

            max_width = max(max_width, text.get_width())
            max_height = max(max_height, text.get_height())

            text_objects.append(text)

        for text in text_objects:
            text.scale_to_fit_width(max_width)
            text.scale_to_fit_height(max_height)
            self.play(Write(text),run_time=0.4)
 

        # Add curly brace vertically to the left of all input strings
        brace = Brace(VGroup(*text_objects), LEFT, buff=0.2)
        brace_text = brace.get_text("M", buff=0.2).scale(0.5)

        self.play(GrowFromCenter(brace),runtime = 0.5)
        self.play(Write(brace_text),run_time=1)
   

        # Add curly brace above the first string
        first_string = text_objects[0]
        brace_above = Brace(first_string, UP, buff=0.2)
        brace_text_above = brace_above.get_text("L", buff=0.2).scale(0.5)

        self.play(GrowFromCenter(brace_above), Write(brace_text_above),run_time=1)
      

        start_point = np.array([-2, 0, 0])  # Coordinates of the start point
        end_point = np.array([2, 0, 0])  # Coordinates of the end point

        arrow = Arrow(start_point, end_point, color=GOLD)  # Create the arrow

        self.play(Create(arrow),run_time=1)  # Animate the creation of the arrow


        toparrow = Tex("Sample  Perturb", color=BLUE).next_to(arrow, UP / 2, buff=0.5).scale(0.5)
        self.play(Write(toparrow),run_time=1)
    
        

        name1=   Tex("RECIEVED INPUTS").to_edge(UR,buff=0.5).scale(0.6)
        self.play(Write(name1),run_time=1)

        string_list = ["ACARAtGT","CgTGTACA","CATGTACA","ACATACGTt","CATACGT"]
        colors = [BLUE,YELLOW,GREEN_B,MAROON_B,GREY]
        text_objects = []

        max_width = 0
        max_height = 0

        for i, string in enumerate(string_list):
            text = Text(string,color=colors[i]).scale(0.4)
            
            text.to_edge(RIGHT)
            text.shift(LEFT*len(string_list)/2)
            text.shift(UP * (1.6-i)*1.2)

            max_width = max(max_width, text.get_width())
            max_height = max(max_height, text.get_height())

            text_objects.append(text)

        for text in text_objects:
            text.scale_to_fit_width(max_width)
            text.scale_to_fit_height(max_height)

        for text in text_objects:
            self.play(Write(text),run_time=0.4)
            

        brace1 = Brace(VGroup(*text_objects), RIGHT, buff=0.2)
        brace_text1 = brace1.get_text("N", buff=0.2).scale(0.5)

        self.play(GrowFromCenter(brace1), Write(brace_text1),run_time=1)
        
        