from manim import *
import numpy as np
import random

class Wiggle(Scene):
    
    def construct(self):
        # name = Tex("TRANSMITTED INPUTS").to_edge(UL).scale(0.5)
        # self.play(Write(name))

        string_list = ["ACATACGT", "CATGTACA", "GCTATGCC"]
        colors = [BLUE, YELLOW, GREEN_B]
        text_objects = []

        max_width = 0
        max_height = 0
        for i, string in enumerate(string_list):
            text = Text(string, color=colors[i]).scale(0.4)
            text.shift(LEFT*6)
            # text.shift(RIGHT * len(string_list) / 2)
            text.shift(UP * (1 - i) * 2.5)
            max_width = max(max_width, text.get_width())
            max_height = max(max_height, text.get_height())
            text_objects.append(text)

        for text in text_objects:
            text.scale_to_fit_width(max_width)
            text.scale_to_fit_height(max_height)
        
        self.play(*[Write(text) for text in text_objects])
        self.wait(0.5)
        
        curve1 = FunctionGraph(lambda x: np.sin(0.9*x))
        curve2 = FunctionGraph(lambda x: -np.sin(0.9*x))
        curve_group = VGroup(curve1, curve2)
        self.play(FadeIn(curve1), FadeIn(curve2), run_time=1)
        self.wait(0.1) 
        self.play(
            AnimationGroup(
                ApplyMethod(curve_group.scale, 0.25),
                run_time=1
            )
        )
        self.play(
            AnimationGroup(
                ApplyMethod(curve_group.shift, 4 * LEFT),
                run_time=1
            )
        )
        self.Shake(curve_group)
        curve_group_copy = curve_group.copy()
        self.play(
            AnimationGroup(
                ReplacementTransform(curve_group.copy(), curve_group_copy),
                ApplyMethod(curve_group_copy.shift, 8 * RIGHT),
                run_time=1
            )
        )
        self.wait(1)
        
    def Shake(self, obj, num_shakes=4, shake_range=0.1, run_time=0.1):
            original_pos = obj.get_center()
            for _ in range(num_shakes):
                dx = random.uniform(-shake_range, shake_range)
                dy = random.uniform(-shake_range, shake_range)
                self.play(ApplyMethod(obj.shift, dx * RIGHT + dy * UP), run_time=run_time / num_shakes)
                self.play(ApplyMethod(obj.shift, -dx * RIGHT - dy * UP), run_time=run_time / num_shakes)
            self.play(ApplyMethod(obj.move_to, original_pos), run_time=run_time / num_shakes)
# 
# 
# 
# 
# 

class ScaleShiftObject(Scene):
    def construct(self):
        # Create an object, such as a circle
        circle = Circle(radius=1, color=BLUE)

        # Define the scaling factor and shift values
        scaling_factor = 2
        shift_vector = np.array([2, 1, 0])

        # Apply scaling and shifting transformations simultaneously
        self.play(ApplyMethod(circle.scale, scaling_factor), ApplyMethod(circle.shift, shift_vector))
        self.wait(1)









class DisplayList1(Scene):
    def construct(self):
        name = Tex("TRANSMITTED INPUTS").to_edge(UL, buff=0.5).scale(0.6)
        self.play(Write(name))

        string_list = ["ACATACGT", "CATGTACA", "GCTATGCC"]
        colors = [BLUE, YELLOW, GREEN_B]
        text_objects = []

        max_width = 0
        max_height = 0

        for i, string in enumerate(string_list):
            text = Text(string, color=colors[i]).scale(0.5)
            text.to_edge(LEFT)
            text.shift(UP * (1 - i) * 2)
            max_width = max(max_width, text.get_width())
            max_height = max(max_height, text.get_height())
            text_objects.append(text)

        for text in text_objects:
            text.scale_to_fit_width(max_width)
            text.scale_to_fit_height(max_height)
        
        self.play(*[Write(text) for text in text_objects])
        self.wait(0.5)
        # brace = Brace(VGroup(*text_objects), LEFT, buff=0.2)
        # brace_text = brace.get_text("M", buff=0.2).scale(0.5)

        # self.play(GrowFromCenter(brace),runtime = 0.5)
        # self.play(Write(brace_text))
        # self.wait(0.3)

        # # Add curly brace above the first string
        # first_string = text_objects[0]
        # brace_above = Brace(first_string, UP, buff=0.2)
        # brace_text_above = brace_above.get_text("L", buff=0.2).scale(0.5)

        # self.play(GrowFromCenter(brace_above), Write(brace_text_above))
        # self.wait(1)

        # start_point = np.array([-2, 0, 0])  # Coordinates of the start point
        # end_point = np.array([2, 0, 0])  # Coordinates of the end point

        # arrow = Arrow(start_point, end_point, color=GOLD)  # Create the arrow

        # self.play(Create(arrow))  # Animate the creation of the arrow
        # self.wait(1)

        # toparrow = Tex("Sample  Perturb", color=BLUE).next_to(arrow, UP / 2, buff=0.5).scale(0.5)
        # self.play(Write(toparrow))
        # self.wait(1)
        

        # name1=   Tex("RECEIVED INPUTS").to_edge(UR,buff=0.5).scale(0.6)
        # self.play(Write(name1))

        # string_list = ["ACARAtGT","CgTGTACA","CATGTACA","ACATACGTt","CATACGT"]
        # colors = [BLUE,YELLOW,GREEN_B,MAROON_B,GREY]
        # text_objects = []

        # max_width = 0
        # max_height = 0

        # for i, string in enumerate(string_list):
        #     text = Text(string,color=colors[i]).scale(0.4)
            
        #     text.to_edge(RIGHT)
        #     text.shift(LEFT*len(string_list)/2)
        #     text.shift(UP * (1.6-i)*1.2)

        #     max_width = max(max_width, text.get_width())
        #     max_height = max(max_height, text.get_height())

        #     text_objects.append(text)

        # for text in text_objects:
        #     text.scale_to_fit_width(max_width)
        #     text.scale_to_fit_height(max_height)

        # for text in text_objects:
        #     self.play(Write(text))
        #     self.wait(0.5)

        # brace1 = Brace(VGroup(*text_objects), RIGHT, buff=0.2)
        # brace_text1 = brace1.get_text("N", buff=0.2).scale(0.5)

        # self.play(GrowFromCenter(brace1), Write(brace_text1))
        # self.wait(1)
