# # from manim import *

# # # class CreateCircle(Scene):

# # #     def construct(self):
# # #         circle = Circle()  # create a circle
# # #         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
# # #         self.play(Create(circle))  # show the circle on screen


# # # class test(Scene):
# # #     def construct(self):

# # #         # circ=Circle(radius=2.4,color=RED)

# # #         # self.play(Create(circ))

# # #         sq=Square(side_length=5, stroke_color=GREEN)
# # #         sq.set_fill(color=BLUE , opacity=6)
# # #         self.play(Create(sq),run_time=3)
# # #         self.wait()



# # # class test(Scene):
# # #     def construct(self):

# # #         #all these are just sitting in the middle 
# # #         #now we need to remove it 

# # #         name=Tex("3.45").to_edge(UL,buff=0.5)
# #         #UL = upper left and buff just adjusts it a bit 

# #         # sq = Square(side_length=0.5).shift(LEFT*3)
# # #         sq.set_fill(BLUE,opacity=5)
# # #         #shift the square to the left by 3 units 

# # #         tri = Triangle().scale(0.6).to_edge(DR)
# # #         #DR = down right 

# #         # self.play(Write(name))
    
# # #         self.play(DrawBorderThenFill(sq))
# # #         self.play(Create(tri))
# # #         self.wait()


# # #         #now we want to move the words and shapes 
# # #         self.play(name.animate.to_edge(DL),run_time=2)
# # #         self.play(sq.animate.scale(2),tri.animate.to_edge(UR),run_time=3)

# # # class SquareToCircle(Scene):
# # #     def construct(self):
# # #         circle = Circle()  # create a circle
# # #         circle.set_fill(PINK, opacity=0.5)  # set color and transparency

# # #         square = Square()  # create a square
# # #         square.rotate(PI / 4)  # rotate a certain amount

# # #         self.play(Create(square))  # animate the creation of the square
# # #         self.play(Transform(square, circle))  # interpolate the square into the circle
# # #         self.play(FadeOut(square))  # fade out animation
        

# # # class SquareAndCircle(Scene):
# # #     def construct(self):
# # #         circle = Circle()  # create a circle
# # #         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

# # #         square = Square()  # create a square
# # #         square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

# # #         square.next_to(circle, RIGHT,buff=4)  # set the position
# # #         #buff depicts how far u want both of them to be 
# # #         self.play(Create(circle), Create(square))  # show the shapes on screen
# # #         self.wait()

# # # class Squareandrect(Scene):
# # #     def construct(self):

# # #         # tra=Square(side_length=2)
# # #         # tra.set_fill(PINK, opacity=2)
# # #         num = Tex("TRANSMITTER")
# # #         box=SurroundingRectangle(num,color=BLUE,fill_opacity=0.4,fill_color=RED,buff=2).to_edge(UR)

# # #         # rec=Square(side_length=2)
# # #         # rec.set_fill(BLUE, opacity=2)
# # #         num2 = Tex("RECEIVER")
# # #         box2=SurroundingRectangle(num2,color=BLACK,fill_opacity=0.4,fill_color=GREEN,buff=2).to_edge(DL)

# # #         #move the trans to the letf a bit 
# # #         box2.shift(RIGHT*3)
# # #        # rec.shift(RIGHT*2)
# # #         box.next_to(box2, LEFT,buff=4) 



# # #         self.play(Create(VGroup(num,num2,box,box2)))
# # #         self.wait(2)




# # # class Squareandrect(Scene):
# # #     def construct(self):
# # #         ax=Axes()
# # #         self.play(Create(ax))
# # #         self.wait(4)

# # # class Getters(Scene):
# #     # def construct(self):

# #         # rect = Rectangle(color= RED , height=2,width= 3).to_edge(UL)
# #         # circ=Circle().to_edge(DOWN)

# #     #     arrow=Line(start=rect.get_bottom(),end=circ.get_top()).add_tip()

# #     #     self.play(Create(VGroup(rect,circ,arrow)))  #cerates all at once - Vgroup = vector group 
# #     #     self.wait()
# #     #     self.play(rect.animate.to_edge(UR))

# # # class Updaters(Scene):
# # #     def construct(self):

# # #         num = MathTex("ln(2)")
# # #         box=SurroundingRectangle(num,color=BLUE,fill_opacity=0.4,fill_color=RED,buff=2)

# # #         name=Tex("Aniruth").next_to(box,DOWN,buff=0.5)

# # #         self.play(Create(VGroup(num,box,name)))

# # # class Valuetracker(Scene):     #to display a decimal number 
# # #     def construct(self):

# # #         k=ValueTracker(3.59)

# # #         num=always_redraw(lambda : DecimalNumber().set_value(k.get_value())) # allows the value to change 


# # #         self.play(FadeIn(num))
# # #         self.wait()
# # #         self.play(k.animate.set_value(7.45),run_time=1)


# # from manim import *

# # # class Box(Scene):
# # #     def construct(self):
# # #         # Create the receiver box
# # #         receiver_box = self.create_box("RECEIVER")

# # #         # Create the transmitter box
# # #         transmitter_box = self.create_box("TRANSMITTER")

# # #         # Position the boxes
# # #         receiver_box.shift(3 * LEFT)
# #         # transmitter_box.shift(3 * RIGHT)

# # #         # Add the boxes to the scene
# # #         self.add(receiver_box, transmitter_box)

# # #         # Run the animations
# # #         self.wait(2)

# # #     def create_box(self, label):
# # #         # Create the box shape
# # #         box = Rectangle(width=5, height=2, color=BLUE, fill_opacity=0.7)

# # #         # Create the label text
# # #         text = Text(label, color=WHITE).scale(0.4)

# # #         # Position the label at the center of the box
# # #         text.move_to(box.get_center())

# # #         # Group the box and label together
# # #         box_with_label = Group(box, text)

# # #         return box_with_label

# # # # Create the scene
# # # scene = Box()

# # # # Render the scene
# # # scene.render()


# # from manim import *

# # # class Box(Scene):
# # #     def construct(self):
# # #         # Create the receiver box
# # #         receiver_box = self.create_box("RECEIVER")

# # #         # Create the transmitter box
# # #         transmitter_box = self.create_box("TRANSMITTER")

# # #         # Position the boxes
# # #         receiver_box.shift(3 * LEFT)
# # #         transmitter_box.shift(3 * RIGHT)

# # #                 # Create the input message
# # #         input_message = Text("Input: 101010", color=WHITE).next_to(transmitter_box, UP).scale(0.3)

     

# # #         # Create the altered message
# # #         altered_message = Text("Altered: 00100", color=WHITE).next_to(receiver_box, UP).scale(0.3)
       

# # #         # Add the boxes and messages to the scene
# # #         self.add(receiver_box, transmitter_box, input_message, altered_message)

# # #         # Run the animations
# # #         self.wait()

# # #     def create_box(self, label):
# # #         # Create the box shape
# # #         box = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.7)

# # #         # Create the label text
# # #         text = Text(label, color=WHITE).scale(0.4)
# # #         # self.wait(1)

# # #         # Position the label at the center of the box
# # #         text.move_to(box.get_center())

# # #         # Group the box and label together
# # #         box_with_label = Group(box, text)

# # #         return box_with_label

# # # # Create the scene
# # # scene = Box()

# # # # Render the scene
# # # # scene.render()

# # from manim import *  
# # from manim import *
# #  # NOISE INTERFERNCING THE SIGNAL   -- BIT FLIPPING !!!


# # # class StringTransformation(Scene):
# # #     def construct(self):
# # #         box = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.7).to_edge(LEFT)

# # #         # Create the label text
# # #         text = Text("TRANSMITTER", color=WHITE).scale(0.4)

# # #         # Position the label at the center of the box
# # #         text.move_to(box.get_center())

# # #         # Create the initial input string
# # #         input_string = Tex("101010", color=WHITE).next_to(box,UP)

# # #         box2 = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.7).to_edge(RIGHT)

# # #         # Create the label text
# # #         text2 = Text("RECEIVER", color=WHITE).scale(0.4)

# # #         # Position the label at the center of the box
# # #         text2.move_to(box2.get_center())


 
# # #         transformed_string = Tex("102010", color=WHITE).next_to(box2,UP)

# # #         # Position the transformed string at the ending point
# # #         # transformed_string.move_to(3 * RIGHT)
        
# # #         self.play(Create(VGroup(box,text,box2,text2)))
# # #         self.wait(2)

# # #         # Animation: Move and transform the string
# # #         self.play(
# # #             input_string.animate.move_to(transformed_string.get_center()),
# # #             Transform(input_string, transformed_string),
# # #             run_time=2
# # #         )

# # #         self.wait()

# # # # Create the scene
# # # scene = StringTransformation()

# # # # Render the scene
# # # scene.render()

# # from manim import *

# # #TEXT TRANSITION !!


# # # class StringTransformation(Scene):
# # #     def construct(self):
# # #         # Create the initial string
# # #         initial_string = Text("ABC", color=WHITE)

# # #         # Position the initial string at the starting point
# # #         initial_string.move_to(3 * LEFT)

# # #         # Add the initial string to the scene
# # #         self.add(initial_string)

# # #         # Define the target strings
# # #         target_strings = ["ABD", "ABJ", "ABU", "IOP"]

# # #         # Transformation animation
# # #         for target_string in target_strings:
# # #             # Create the target string
# # #             target = Text(target_string, color=WHITE)

# # #             # Position the target string at the ending point
# # #             target.move_to(3 * RIGHT)

# # #             # Animation: Move and transform the string
# # #             self.play(
# # #                 initial_string.animate.move_to(target.get_center()),
# # #                 Transform(initial_string, target),
# # #                 run_time=1
# # #             )

# # #         self.wait()

# # # # Create the scene
# # # scene = StringTransformation()

# # # # Render the scene
# # # scene.render()

# # from manim import *
# # from manim import *

# # # class StringMapping(Scene):
# # #     def construct(self):
# # #         # Create the initial string
# # #         initial_string = Text("ABC", color=WHITE)
# # #         initial_string.shift(3 * LEFT)

# # #         # Create the target strings
# # #         target_strings = ["ABX", "UIO", "IOP","uiu"]
# # #         targets = []

# # #         # Create the target strings and arrows
# # #         arrows = []
# # #         for target_string in target_strings:
# # #             target = Text(target_string, color=WHITE)
# # #             targets.append(target)

# # #         # Position the target strings vertically
# # #         targets[0].shift(1.5 * UP)
# # #         for i in range(1, len(target_strings)):
# # #             targets[i].next_to(targets[i - 1], DOWN, buff=0.5)

# # #         self.add(initial_string)

# # #         # Animation: Map the strings one by one
# # #         for i in range(len(target_strings)):
# # #             target = targets[i]
# # #             arrow = Arrow(initial_string.get_edge_center(RIGHT), target.get_edge_center(LEFT), buff=0.2)
# # #             arrows.append(arrow)

# # #             self.play(
# # #                 Create(arrow),
# # #                 run_time=0.5
# # #             )
# # #             self.wait(0.5)
# # #             self.play(
# # #                 TransformFromCopy(initial_string, target),
# # #                 run_time=0.5
# # #             )
# # #             self.wait(0.5)

# # #         self.remove(*arrows)
# # #         self.add(*targets)

# # # # Create the scene
# # # scene = StringMapping()

# # # # Render the scene
# # # scene.render()

# # # from manim import *
# # # from manim import *
# # # from manim import *
# # from manim import *

# # from manim import *

# # class DisplayList1(Scene):
# #     def construct(self):
# #         name = Tex("TRANSMITTED INPUTS").to_edge(UL, buff=0.5).scale(0.6)
# #         self.play(Write(name))

# #         string_list = ["ACATACGT", "CATGTACA", "GCTATGCC"]
# #         colors = [BLUE, YELLOW, GREEN_B]
# #         text_objects = []

# #         max_width = 0
# #         max_height = 0

# #         for i, string in enumerate(string_list):
# #             text = Text(string, color=colors[i]).scale(0.5)
# #             text.to_edge(LEFT)
# #             text.shift(RIGHT * len(string_list) / 2)
# #             text.shift(UP * (1 - i) * 2)

# #             max_width = max(max_width, text.get_width())
# #             max_height = max(max_height, text.get_height())

# #             text_objects.append(text)

# #         for text in text_objects:
# #             text.scale_to_fit_width(max_width)
# #             text.scale_to_fit_height(max_height)
# #             self.play(Write(text))
# #             self.wait(0.5)

# #         # Add curly brace vertically to the left of all input strings
# #         brace = Brace(VGroup(*text_objects), LEFT, buff=0.2)
# #         brace_text = brace.get_text("M", buff=0.2).scale(0.5)

# #         self.play(GrowFromCenter(brace),runtime = 0.5)
# #         self.play(Write(brace_text))
# #         self.wait(0.3)

# #         # Add curly brace above the first string
# #         first_string = text_objects[0]
# #         brace_above = Brace(first_string, UP, buff=0.2)
# #         brace_text_above = brace_above.get_text("L", buff=0.2).scale(0.5)

# #         self.play(GrowFromCenter(brace_above), Write(brace_text_above))
# #         self.wait(1)

# #         start_point = np.array([-2, 0, 0])  # Coordinates of the start point
# #         end_point = np.array([2, 0, 0])  # Coordinates of the end point

# #         arrow = Arrow(start_point, end_point, color=GOLD)  # Create the arrow

# #         self.play(Create(arrow))  # Animate the creation of the arrow
# #         self.wait(1)

# #         toparrow = Tex("Sample  Perturb", color=BLUE).next_to(arrow, UP / 2, buff=0.5).scale(0.5)
# #         self.play(Write(toparrow))
# #         self.wait(1)
        

# #         name1=   Tex("RECEIVED INPUTS").to_edge(UR,buff=0.5).scale(0.6)
# #         self.play(Write(name1))

# #         string_list = ["ACARAtGT","CgTGTACA","CATGTACA","ACATACGTt","CATACGT"]
# #         colors = [BLUE,YELLOW,GREEN_B,MAROON_B,GREY]
# #         text_objects = []

# #         max_width = 0
# #         max_height = 0

# #         for i, string in enumerate(string_list):
# #             text = Text(string,color=colors[i]).scale(0.4)
            
# #             text.to_edge(RIGHT)
# #             text.shift(LEFT*len(string_list)/2)
# #             text.shift(UP * (1.6-i)*1.2)

# #             max_width = max(max_width, text.get_width())
# #             max_height = max(max_height, text.get_height())

# #             text_objects.append(text)

# #         for text in text_objects:
# #             text.scale_to_fit_width(max_width)
# #             text.scale_to_fit_height(max_height)

# #         for text in text_objects:
# #             self.play(Write(text))
# #             self.wait(0.5)

# #         brace1 = Brace(VGroup(*text_objects), RIGHT, buff=0.2)
# #         brace_text1 = brace1.get_text("N", buff=0.2).scale(0.5)

# #         self.play(GrowFromCenter(brace1), Write(brace_text1))
# #         self.wait(1)


# # # from manim import *

# # # class DisplayList(Scene):
# # #     def construct(self):
# # #         name = Tex("TRANSMITTED INPUTS").to_edge(UL, buff=0.5).scale(0.6)
# # #         self.play(Write(name))

# # #         string_list = ["ACATACGT", "CATGTACA", "GCTATGCC"]
# # #         colors = [BLUE, YELLOW, GREEN_B]
# # #         text_objects = []

# # #         max_width = 0
# # #         max_height = 0

# # #         for i, string in enumerate(string_list):
# # #             text = Text(string, color=colors[i]).scale(0.5)
# # #             text.to_edge(LEFT)
# # #             text.shift(RIGHT * len(string_list) / 2)
# # #             text.shift(UP * (1 - i) * 2)

# # #             max_width = max(max_width, text.get_width())
# # #             max_height = max(max_height, text.get_height())

# # #             text_objects.append(text)

# # #         for text in text_objects:
# # #             text.scale_to_fit_width(max_width)
# # #             text.scale_to_fit_height(max_height)
# # #             self.play(Write(text))
# # #             self.wait(0.5)

# # #         # Add curly brace
# # #         brace = Brace(text_objects[-1], DOWN, buff=0.2)
# # #         brace_text = brace.get_text("L", buff=0.2).scale(0.5)

# # #         self.play(GrowFromCenter(brace), Write(brace_text))
# # #         self.wait(1)

# # #         start_point = np.array([-2, 0, 0])  # Coordinates of the start point
# # #         end_point = np.array([2, 0, 0])  # Coordinates of the end point

# # #         arrow = Arrow(start_point, end_point, color=GOLD)  # Create the arrow

# # #         self.play(Create(arrow))  # Animate the creation of the arrow
# # #         self.wait(1)

# # #         toparrow = Tex("Sample and Perturb", color=BLUE).next_to(arrow, UP / 2, buff=0.5).scale(0.5)
# # #         self.play(Write(toparrow))
# # #         self.wait(1)


# # # from manim import *
# # # from manim import *

# # # class ArrowExample(Scene):
# # #     def construct(self):
# # #         start_point = np.array([-2, 0, 0])  # Coordinates of the start point
# # #         end_point = np.array([2, 0, 0])  # Coordinates of the end point

# # #         arrow = Arrow(start_point, end_point, color=WHITE)  # Create the arrow

# # #         self.play(Create(arrow))  # Animate the creation of the arrow
# # #         self.wait(1)  # Wait for a second

# # #         self.play(FadeOut(arrow))  # Animate the fading out of the arrow
# # #         self.wait(1)  # Wait for a second


# # # class HelveticaExample(Scene):
# # #     def construct(self):
# # #         text = Text("Hello, Manim!", font="Helvetica")
# # #         self.play(Write(text))
# # #         self.wait(2)


# # # from manim import *
# # # from manim import *

# # # class DisplayList(Scene):
# # #     def construct(self):
# # #         string_list = ["Hello", "World", "Manim", "OpenAI", "GPT-3.5"]
# # #         text_objects = []

# # #         max_width = 0

# # #         for i, string in enumerate(string_list):
# # #             text = Text(string)
# # #             text.to_edge(LEFT,buff=0.5)
# # #             text.shift(UP * 2 )
# # #             text_objects.append(text)

# # #             # Update maximum width if necessary
# # #             max_width = max(max_width, text.get_width())

# # #         for text in text_objects:
# # #             # Calculate scale factor for width adjustment
# # #             scale_factor = max_width / text.get_width()

# # #             # Adjust the width of the Text object
# # #             text.scale(scale_factor)

# # #             self.play(Write(text))
# # #             self.wait(0.5)

# # #         self.wait()


# # # class DisplayList(Scene):
# # #     def construct(self):

# # #         name=Tex("3.45",color=YELLOW).to_edge(LEFT,buff=0.5)
# # #         name.shift)

# # #         name2=Tex("3.4544",color=YELLOW).to_edge(LEFT,buff=0.5)
# # #         name2.shift(1)

# # #         self.play(Write(name))
# # #         self.wait(1)
# # #         self.play(Write(name2))
# # #         self.wait(1)


# # # from manim import *
# # # from manim_chemistry import *

# # # class DrawAdenine(Scene):
# # #     def construct(self):
# # #         adenine_structure = ChemistryText("Adenine")
        
# # #         self.play(Create(adenine_structure))
# # #         self.wait(1)

# # from manim import *

# # from manim import *


# # # class BinaryMapping(Scene):
# # #     def construct(self):
# # #         p = 0.1  # Probability of mapping 0 to 1

# # #         source = Dot(LEFT, color=BLUE)
# # #         destination_0 = Dot(RIGHT * 0.5 + UP * 0.5, color=GREEN)
# # #         destination_1 = Dot(RIGHT * 0.5 + DOWN * 0.5, color=RED)

# # #         channel_0 = Line(source.get_center(), destination_0.get_center(), color=GREEN)
# # #         channel_1 = Line(source.get_center(), destination_1.get_center(), color=RED)

# # #         input_bit = MathTex("0").next_to(source, UP, buff=0.25)
# # #         output_bit_0 = MathTex("0").next_to(destination_0, UP, buff=0.25)
# # #         output_bit_1 = MathTex("1").next_to(destination_1, DOWN, buff=0.25)

# # #         self.add(source, destination_0, destination_1, channel_0, channel_1, input_bit, output_bit_0, output_bit_1)

# # #         arrow_0 = Arrow(source.get_center(), destination_0.get_center(), buff=0.1, color=GREEN)
# # #         arrow_1 = Arrow(source.get_center(), destination_1.get_center(), buff=0.1, color=RED)
# # #         arrow_label_0 = MathTex(f"1-p={1 - p}").next_to(arrow_0, UP, buff=0.2)
# # #         arrow_label_1 = MathTex(f"p={p}").next_to(arrow_1, DOWN, buff=0.2)

# # #         self.play(GrowArrow(arrow_0), Write(arrow_label_0))
# # #         self.play(GrowArrow(arrow_1), Write(arrow_label_1))
# # #         self.wait(1)

# # #         for _ in range(10):
# # #             if np.random.random() < p:
# # #                 # Bit flip to 1
# # #                 output_bit_0.set_opacity(0)
# # #                 output_bit_1.set_opacity(1)
# # #             else:
# # #                 # No bit flip, remains 0
# # #                 output_bit_0.set_opacity(1)
# # #                 output_bit_1.set_opacity(0)

# # #             self.play(Transform(input_bit.copy(), output_bit_0), Transform(input_bit.copy(), output_bit_1))
# # #             self.wait(0.5)


# # # BinaryMapping().render()

# # from manim import *


# # class BinaryMapping(Scene):
# #     def construct(self):

# #         source = Dot(LEFT, color=BLUE)
# #         destination_0 = Dot(RIGHT * 2.5 + UP * 1, color=GREEN)
# #         destination_1 = Dot(RIGHT * 2.5 + DOWN * 1, color=RED)

# #         channel_0 = Line(source.get_center(), destination_0.get_center(), color=GREEN)
# #         channel_1 = Line(source.get_center(), destination_1.get_center(), color=RED)

# #         input_bit = MathTex("0").next_to(source, UP, buff=0.5)
# #         output_bit_0 = MathTex("0").next_to(destination_0, UP, buff=0.5)
# #         output_bit_1 = MathTex("1").next_to(destination_1, DOWN, buff=0.5)

# #         self.add(source, destination_0, destination_1, channel_0, channel_1, input_bit, output_bit_0, output_bit_1)

# #         arrow_0 = Arrow(source.get_center(), destination_0.get_center(), buff=0.1, color=GREEN)
# #         arrow_1 = Arrow(source.get_center(), destination_1.get_center(), buff=0.1, color=RED)
# #         arrow_label_0 = Tex(f"1 - p").next_to(arrow_0, UP, buff=0.3)
# #         arrow_label_1 = Tex(f"p").next_to(arrow_1, DOWN, buff=0.3)

# #         self.play(GrowArrow(arrow_0), Write(arrow_label_0))
# #         self.play(GrowArrow(arrow_1), Write(arrow_label_1))
# #         self.wait(1)

# #         self.wait(0.5)


# # BinaryMapping().render()


# # from manim import *


# # class BinaryMapping(Scene):
# #     def construct(self):

# #         source = Dot(LEFT, color=BLUE)
# #         destination_0 = Dot(RIGHT * 2.5 + UP * 1, color=GREEN)
# #         destination_1 = Dot(RIGHT * 2.5 + DOWN * 1, color=RED)

# #         channel_0 = Line(source.get_center(), destination_0.get_center(), color=GREEN)
# #         channel_1 = Line(source.get_center(), destination_1.get_center(), color=RED)

# #         input_bit = MathTex("0").next_to(source, UP, buff=1)
# #         output_bit_0 = MathTex("0").next_to(destination_0, UP, buff=1)
# #         output_bit_1 = MathTex("1").next_to(destination_1, DOWN, buff=1)

# #         self.add(source, destination_0, destination_1, channel_0, channel_1, input_bit)

# #         arrow_0 = Arrow(source.get_center(), destination_0.get_center(), buff=0.3, color=GREEN, stroke_width=5)
# #         arrow_1 = Arrow(source.get_center(), destination_1.get_center(), buff=0.3, color=RED, stroke_width=5)
# #         arrow_label_0 = Tex(f"1 - p").next_to(arrow_0, UP, buff=0.3)
# #         arrow_label_1 = Tex(f"p").next_to(arrow_1, DOWN, buff=0.3)

# #         self.play(GrowArrow(arrow_0), Write(arrow_label_0))
# #         self.play(GrowArrow(arrow_1), Write(arrow_label_1))

# #         self.wait(0.5)

# #         self.play(Transform(source.copy(), output_bit_0), run_time=1.5)
# #         self.play(Transform(source.copy(), output_bit_1), run_time=1.5)

# #         self.wait(1)


# # BinaryMapping().render()
# from manim import *


# class BinaryMapping(Scene):
#     def construct(self):

#         source = Dot(LEFT, color=BLUE)
#         destination_0 = Dot(RIGHT * 2.5 + UP * 1, color=GREEN)

#         channel_0 = Line(source.get_center(), destination_0.get_center(), color=GREEN)

#         input_bit = MathTex("0").next_to(source, UP, buff=1)
#         output_bit_0 = MathTex("0").next_to(destination_0, UP, buff=1)

#         self.add(source, destination_0, channel_0, input_bit)

#         arrow_0 = Arrow(source.get_center(), destination_0.get_center(), buff=0.3, color=GREEN, stroke_width=5)
#         arrow_label_0 = Tex(f"1 - p").next_to(arrow_0, UP, buff=0.3)

#         self.play(GrowArrow(arrow_0), Write(arrow_label_0))
#         self.wait(0.5)

#         self.play(Transform(source.copy(), output_bit_0), run_time=1.5)

#         self.wait(1)


# BinaryMapping().render()
from manim import *
from manim import *


class BinaryMapping(Scene):
    def construct(self):

        topic = Tex("BINARY SYMMENTRIC CHANNEL",color=YELLOW_E).scale(1.5)
        topic2=Tex("BSC",color=YELLOW_E).scale(1.5)

        self.play(Write(topic))
        self.wait()
        self.play(FadeOut(topic))

        # self.play(Transform(topic,topic2))
        # self.wait()

        self.play(Write(topic2))
        

        self.play(FadeOut(topic2))

        text=Tex("ENCODER",color=YELLOW_C).to_edge(LEFT).shift(UP*3).shift(RIGHT*1).scale(0.5)
        self.play(Write(text))
        self.wait(0.5)


        source = Dot(LEFT, color=BLUE).to_edge(LEFT).shift(RIGHT*2).scale(0.5).shift(UP*2)
        destination_0 = Dot(RIGHT * 2.5 + UP * 2, color=MAROON_C).scale(0.5)


        input_bit = MathTex("0").next_to(source, UP*0.2, buff=1).scale(0.5)
        output_bit_0 = MathTex("0").next_to(destination_0, UP*0.1, buff=1).scale(0.5)
        

        self.add(source, destination_0, input_bit)

        arrow_0 = Arrow(source.get_center(), destination_0.get_center(), buff=0.3, color=BLUE_C, stroke_width=3)
        arrow_label_0 = Tex(f"1 - p").next_to(arrow_0, UP*0.05, buff=0.3).scale(0.5)

        text=Tex("DECODER",color=YELLOW_C).to_edge(RIGHT).shift(UP*3).shift(LEFT*2.5).scale(0.5)
        self.play(Write(text))
        self.wait(0.5)

        self.play(GrowArrow(arrow_0))
        # self.wait(0.5)
        self.play(Write(output_bit_0))

        self.wait(0.5)

        self.play(Write(arrow_label_0))
        self.wait(0.5)




 
        # source = Dot(LEFT, color=BLUE).to_edge(LEFT).shift(RIGHT*2).scale(0.5).shift(UP*1)
        destination_0 = Dot(RIGHT * 2.5 + DOWN * 2, color=MAROON_C).scale(0.5)


        #input_bit = MathTex("0").next_to(source, UP*0.2, buff=1).scale(0.5)
        output_bit_0 = MathTex("1").next_to(destination_0, UP*0.1, buff=1).scale(0.5)
        

        self.add(source, destination_0, input_bit)

        arrow_0 = Arrow(source.get_center(), destination_0.get_center(), buff=0.3, color=BLUE_C, stroke_width=3)
        arrow_label_0 = Tex(f"p").scale(0.5).shift(LEFT*1).shift(DOWN*0.75)


        self.play(GrowArrow(arrow_0))
        # self.wait(0.5)
        self.play(Write(arrow_label_0))
        self.wait(0.5)

        self.play(Write(output_bit_0))

        self.wait(0.5)



        source = Dot(LEFT, color=BLUE).to_edge(LEFT).shift(RIGHT*2+DOWN*3).scale(0.5).shift(UP*1)
        destination_0 = Dot(RIGHT * 2.5 + DOWN * 2, color=MAROON_C).scale(0.5)


        input_bit = MathTex("1").next_to(source, UP*0.2, buff=1).scale(0.5)
        output_bit_0 = MathTex("1").next_to(destination_0, UP*0.1, buff=1).scale(0.5)
        

        self.add(source, destination_0, input_bit)

        arrow_0 = Arrow(source.get_center(), destination_0.get_center(), buff=0.3, color=BLUE_C, stroke_width=3)
        arrow_label_0 = Tex(f"1 - p").scale(0.5).shift(LEFT*1).shift(DOWN*2.3)


        self.play(GrowArrow(arrow_0))
        # self.wait(0.5)
        self.play(Write(arrow_label_0))
        self.wait(0.5)

        # self.play(Write(output_bit_0))

        # self.wait(0.5)

        #source = Dot(LEFT, color=BLUE).to_edge(LEFT).shift(RIGHT*2+DOWN*3).scale(0.5).shift(UP*1)
        destination_0 = Dot(RIGHT * 2.5 + UP* 2, color=MAROON_C).scale(0.5)


        #input_bit = MathTex("1").next_to(source, UP*0.2, buff=1).scale(0.5)
        #output_bit_0 = MathTex("1").next_to(destination_0, UP*0.1, buff=1).scale(0.5)
        

        self.add(source, destination_0, input_bit)

        arrow_0 = Arrow(source.get_center(), destination_0.get_center(), buff=0.3, color=BLUE_C, stroke_width=3)
        # arrow_label_0 = Tex(f"1-p").scale(0.5).shift(LEFT*1).shift(DOWN*1)


        self.play(GrowArrow(arrow_0))
        # self.wait(0.5)
        # self.play(Write(arrow_label_0))
        # self.wait(0.5)

        self.play(Write(output_bit_0))

        self.wait(0.5)


        




