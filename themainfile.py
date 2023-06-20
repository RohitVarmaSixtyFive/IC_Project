from manim import *
import numpy as np
import random


class First(Scene):
    def construct(self):
        # func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        # stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        # self.add(stream_lines)
        # stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        # self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
        text1 = Tex("100101", color=WHITE).shift(LEFT*5).scale(1.2)
        self.play(Write(text1))
        square = Square(side_length=2, fill_color=BLUE,
                        fill_opacity=1, stroke_width=0)
        square.shift(LEFT*0.4).set_z_index(1)
        channel = Text("Encoder", color=WHITE).scale(0.5).next_to(square, UP)
        self.play(FadeIn(square), FadeIn(channel))
        self.wait(0.5)
        text2 = Tex("100101", color=WHITE).scale(0.2)
        self.play(Transform(text1, text2), run_time=2)
        self.play(FadeOut(text1), FadeOut(text2), run_time=0.01)
        # self.wait(1)
        string_list = ["ACATACGT", "CATGTACA", "GCTATGCC"]
        colors = [WHITE, WHITE, WHITE]
        text_objects = []
        max_width = 0
        max_height = 0
        for i, string in enumerate(string_list):
            text = Text(string, color=colors[i]).scale(0.3).shift(LEFT*0.4)
            text.shift(UP * (1 - i) * 0.5)

            max_width = max(max_width, text.get_width())
            max_height = max(max_height, text.get_height())
            text_objects.append(text)

        for text in text_objects:
            text.scale_to_fit_width(max_width)
            text.scale_to_fit_height(max_height)
        # self.play(*[Write(text) for text in text_objects],run_time = 0.5)
        text_objects_big = [None, None, None]
        text_objects_big[0] = text_objects[0].copy().shift(
            RIGHT*4+UP*2).scale(2)
        text_objects_big[1] = text_objects[1].copy().shift(RIGHT*4).scale(2)
        text_objects_big[2] = text_objects[2].copy().shift(
            RIGHT*4+DOWN*2).scale(2)
        text_objects_big[0].set_z_index(0)
        text_objects_big[1].set_z_index(0)
        text_objects_big[2].set_z_index(0)
        self.Shake(square)
        self.play(
            Transform(text_objects[0], text_objects_big[0]),
            Transform(text_objects[1], text_objects_big[1]),
            Transform(text_objects[2], text_objects_big[2]),
            run_time=2
        )
        text_group1 = VGroup(text_objects_big[0], text_objects[0])
        text_group2 = VGroup(text_objects_big[1], text_objects[1])
        text_group3 = VGroup(text_objects_big[2], text_objects[2])
        self.play(
            ApplyMethod(text_group1.shift, LEFT*8.8),
            ApplyMethod(text_group2.shift, LEFT*8.8),
            ApplyMethod(text_group3.shift, LEFT*8.8),
            ApplyMethod(square.shift, LEFT*8.8),
            ApplyMethod(channel.shift, LEFT*8.8),
            run_time=1
        )
####################################################################################################################################
        synthesis = Square(side_length=2, fill_color=BLUE,
                           fill_opacity=1, stroke_width=0)
        synthesis.shift(LEFT*0.4).set_z_index(1)
        Nameof = Text("Synthesis", color=WHITE).scale(
            0.5).next_to(synthesis, UP)
        self.play(FadeIn(synthesis), FadeIn(Nameof), run_time=1)
        self.wait(0.5)
        curvebro1 = FunctionGraph(
            lambda x: 1, x_range=[-1, 0.3]).shift(DOWN*0.8)
        curvebro2 = FunctionGraph(
            lambda x: 1, x_range=[-1, 0.3]).shift(DOWN*1.2)
        curvebrogroup1 = VGroup(curvebro1, curvebro2).set_z_index(2)
        curvebro3 = FunctionGraph(
            lambda x: 1, x_range=[-1, 0.3]).shift(DOWN*0.1)
        curvebro4 = FunctionGraph(
            lambda x: 1, x_range=[-1, 0.3]).shift(DOWN*0.5)
        curvebrogroup2 = VGroup(curvebro3, curvebro4).set_z_index(2)
        curvebro5 = FunctionGraph(
            lambda x: 1, x_range=[-1, 0.3]).shift(DOWN*1.5)
        curvebro6 = FunctionGraph(
            lambda x: 1, x_range=[-1, 0.3]).shift(DOWN*1.9)
        curvebrogroup3 = VGroup(curvebro5, curvebro6).set_z_index(2)

        sinmid = FunctionGraph(lambda x: np.sin(1 * x), color=RED_E)
        sinmid1 = FunctionGraph(lambda x: -np.sin(1 * x), color=RED_E)
        curve_groupmid = VGroup(sinmid, sinmid1).shift(LEFT*0.4)
        curve_groupmid.scale(0.1).set_z_index(2)
        sinup = FunctionGraph(lambda x: np.sin(1 * x), color=RED_E)
        sinup1 = FunctionGraph(lambda x: -np.sin(1 * x), color=RED_E)
        curve_groupup = VGroup(sinup, sinup1).shift(LEFT*0.4+UP*0.8)
        curve_groupup.scale(0.1).set_z_index(2)
        sindown = FunctionGraph(lambda x: np.sin(1 * x), color=RED_E)
        sindown1 = FunctionGraph(lambda x: -np.sin(1 * x), color=RED_E)
        curve_groupdown = VGroup(sindown, sindown1).shift(LEFT*0.4 + DOWN*0.8)
        curve_groupdown.scale(0.1).set_z_index(2)

        colors = [WHITE, WHITE, WHITE]
        text_objects_extra = []
        max_width = 0
        max_height = 0
        for i, string in enumerate(string_list):
            textbro = Text(string, color=colors[i]).scale(0.3).shift(LEFT*0.4)
            textbro.shift(UP * (1 - i) * 0.5)

            max_width = max(max_width, textbro.get_width())
            max_height = max(max_height, textbro.get_height())
            text_objects_extra.append(textbro)

        for textbro in text_objects_extra:
            textbro.scale_to_fit_width(max_width)
            textbro.scale_to_fit_height(max_height)
        self.play(
            Transform(text_group1, text_objects_extra[0]),
            Transform(text_group2, text_objects_extra[1]),
            Transform(text_group3, text_objects_extra[2]),
            run_time=2
        )

        self.play(LaggedStart(Create(curvebro1), Create(curvebro2), Create(curvebro3),
                  Create(curvebro4), Create(curvebro5), Create(curvebro6),
                  lag_ratio=0.25,
                  runtime=2.5))
        self.play(LaggedStart(Transform(curvebrogroup1, curve_groupmid),
                  Transform(curvebrogroup2, curve_groupup),
                  Transform(curvebrogroup3, curve_groupdown), lag_ratio=0.25, run_time=3))
        # self.wait(2)
        self.play(FadeOut(text_group1),
                  FadeOut(text_group2),
                  FadeOut(text_group3),
                  run_time=0.1
                  )
        temp_curve_group = VGroup(
            curvebrogroup1, curvebrogroup2, curvebrogroup3)
################################################################################################################################################

        self.play(ApplyMethod(synthesis.shift, LEFT*4),
                  ApplyMethod(Nameof.shift, LEFT*4),
                  ApplyMethod(temp_curve_group.shift, LEFT*4),
                  run_time=1.5
                  )
        self.wait(1)

        Amplifier = Square(side_length=2, fill_color=BLUE,
                           fill_opacity=1, stroke_width=0).set_z_index(1)
        Amplifiername = Text("Amplifier", color=WHITE).scale(
            0.5).next_to(Amplifier, UP)
        self.play(FadeIn(Amplifier), FadeIn(Amplifiername), run_time=1)
        self.play(LaggedStart(
            ApplyMethod(curvebrogroup1.shift, RIGHT*4.4),
            ApplyMethod(curvebrogroup2.shift, DOWN*0.7),
            # ApplyMethod(curvebrogroup2.shift,RIGHT*4),
            # ApplyMethod(curvebrogroup3.shift,UP*0.8),
            # ApplyMethod(curvebrogroup3.shift,RIGHT*4),
            lag_ratio=0.25,
            run_time=2
        ))
        self.play(LaggedStart(ApplyMethod(curvebrogroup2.shift, RIGHT*4.4),
                              ApplyMethod(curvebrogroup3.shift, UP*0.7),
                              ApplyMethod(curvebrogroup1.shift, UP*0.5),
                              run_time=2))
        self.play(ApplyMethod(curvebrogroup3.shift, RIGHT*4.4),
                  ApplyMethod(curvebrogroup2.shift, DOWN*0.7),
                  run_time=2)
        self.play(FadeOut(Amplifiername), rum_time=0.8)
        curvebrogroup11 = curvebrogroup1
        curvebrogroup22 = curvebrogroup2
        self.play(
            ApplyMethod(curvebrogroup11.shift, UP*0.3),
            ApplyMethod(curvebrogroup22.shift, DOWN * 0.3)
        )
        self.play(
            ApplyMethod(Amplifier.scale, 3.5),
            ApplyMethod(curvebrogroup11.scale, 2),
            ApplyMethod(curvebrogroup3.scale, 2),
            ApplyMethod(curvebrogroup11.scale, 2),
            ApplyMethod(curvebrogroup22.scale, 2),
            ApplyMethod(curvebrogroup22.scale, 2),
            ApplyMethod(synthesis.shift, LEFT*5),
            ApplyMethod(Nameof.shift, LEFT*5),
            run_time=2
        )
        self.wait(0.2)
        self.Shake(curvebrogroup11)
        self.Shake(curvebrogroup22)
        curvebrogroup1_copy = curvebrogroup11.copy()
        curvebrogroup2_copy = curvebrogroup22.copy()
        self.play(
            AnimationGroup(
                LaggedStart(
                    ApplyMethod(curvebrogroup1_copy.shift, 2*LEFT),
                    ApplyMethod(curvebrogroup2_copy.shift, 2*LEFT),
                    lag_ratio=0.25,
                    run_time=1
                ))
        )
        # self.play(
        #     TransformFromCopy(curvebrogroup1, curvebrogroup1_copy),
        #     TransformFromCopy(curvebrogroup2, curvebrogroup2_copy),

        #     run_time=1
        # )
        self.play(LaggedStart(ApplyMethod(curvebrogroup1.shift, 2*RIGHT),
                  ApplyMethod(curvebrogroup2.shift, 2*RIGHT), lag_ratio=0.25, run_time=2))

        curvebrogroup1next_copy = curvebrogroup1_copy.copy()
        curvebrogroup2next_copy = curvebrogroup2_copy.copy()

        self.play(
            AnimationGroup(
                LaggedStart(
                    ApplyMethod(curvebrogroup1next_copy.shift, 1*UP),
                    ApplyMethod(curvebrogroup2next_copy.shift, 1*DOWN),
                    lag_ratio=0.25,
                    run_time=1
                ))
        )
        curvebrogroup1right_copy = curvebrogroup1.copy()
        curvebrogroup2right_copy = curvebrogroup2.copy()
        self.play(
            AnimationGroup(
                LaggedStart(
                    ApplyMethod(curvebrogroup1right_copy.shift, 1*UP),
                    ApplyMethod(curvebrogroup2right_copy.shift, 1*DOWN),
                    lag_ratio=0.25,
                    run_time=1
                ))
        )
        group = VGroup(curvebrogroup1right_copy, curvebrogroup2right_copy,
                       curvebrogroup1next_copy, curvebrogroup2next_copy,
                       curvebrogroup11, curvebrogroup22,
                       curvebrogroup1_copy, curvebrogroup2_copy,
                       curvebro1, curvebro2, curvebrogroup3,
                       Amplifier)
        self.play(ApplyMethod(group.scale, 0.3), runtime=1.4)
        self.play(FadeIn(Amplifiername), run_time=0.5)
        self.play(ApplyMethod(group.shift, LEFT * 4),
                  ApplyMethod(Amplifiername.shift, LEFT*4),
                  run_time=0.5)

        # text1 = Tex("100101", color=WHITE).shift(LEFT*5).scale(1.2)
        # self.play(Write(text1))
        # square = Square(side_length=2, fill_color=BLUE,
        # fill_opacity=1, stroke_width=0)
        # square.shift(LEFT*0.4).set_z_index(1)
        # channel = Text("Encoder", color=WHITE).scale(0.5).next_to(square, UP)
        # self.play(FadeIn(square), FadeIn(channel))
        # self.wait(0.5)
        # text2 = Tex("100101", color=WHITE).scale(0.2)
        # self.play(Transform(text1, text2), run_time=2)
        # self.play(FadeOut(text1), FadeOut(text2), run_time=0.01)
        # self.wait(1)
        string_listdash = ["ACARAtGT", "CgTGTACA",
                           "CATGTACA", "ACATACGTt", "CATACGT"]
        colors = [WHITE, WHITE, WHITE, WHITE, WHITE]
        text_objectsdash = []
        max_width = 0
        max_height = 0
        for i, string in enumerate(string_listdash):
            textdash = Text(string, color=colors[i]).scale(0.3).shift(LEFT*4)
            textdash.shift(UP * (1 - i) * 0.3)

            max_width = max(max_width, textdash.get_width())
            max_height = max(max_height, textdash.get_height())
            text_objectsdash.append(textdash)

        for textdash in text_objectsdash:
            textdash.scale_to_fit_width(max_width)
            textdash.scale_to_fit_height(max_height)
        # self.play(*[Write(text) for text in text_objects],run_time = 0.5)
        text_objects_bigdash = [None, None, None,None,None]
        text_objects_bigdash[0] = text_objectsdash[0].copy().shift(
            RIGHT*7+UP*2).scale(1.3)
        text_objects_bigdash[1] = text_objectsdash[1].copy().shift(
            RIGHT*7+UP).scale(1.3)
        text_objects_bigdash[2] = text_objectsdash[2].copy().shift(
            RIGHT*7).scale(1.3)
        text_objects_bigdash[3] = text_objectsdash[3].copy().shift(
            RIGHT*7+DOWN*1).scale(1.3)
        text_objects_bigdash[4] = text_objectsdash[4].copy().shift(
            RIGHT*7+DOWN*2).scale(1.3)
        text_objects_bigdash[0].set_z_index(0)
        text_objects_bigdash[1].set_z_index(0)
        text_objects_bigdash[2].set_z_index(0)
        text_objects_bigdash[3].set_z_index(0)
        text_objects_bigdash[4].set_z_index(0)
        # self.Shake(square)\
        self.play(FadeOut(curvebrogroup1right_copy, curvebrogroup2right_copy,
                       curvebrogroup1next_copy, curvebrogroup2next_copy,
                       curvebrogroup11, curvebrogroup22,
                       curvebrogroup1_copy, curvebrogroup2_copy,
                       curvebro1, curvebro2, curvebrogroup3),run_time=1)
        self.play(
            Transform(text_objectsdash[0], text_objects_bigdash[0]),
            Transform(text_objectsdash[1], text_objects_bigdash[1]),
            Transform(text_objectsdash[2], text_objects_bigdash[2]),
            Transform(text_objectsdash[3], text_objects_bigdash[3]),
            Transform(text_objectsdash[4], text_objects_bigdash[4]),
            run_time=2
        )
        everything = VGroup(*self.mobjects)
        self.play(FadeOut(everything))
        self.wait(2)
######################################################################################################################################################

    def Shake(self, obj, num_shakes=6, shake_range=0.1, run_time=0.05):
        original_pos = obj.get_center()
        for _ in range(num_shakes):
            dx = random.uniform(-shake_range, shake_range)
            dy = random.uniform(-shake_range, shake_range)
            self.play(ApplyMethod(obj.shift, dx * RIGHT + dy * UP),
                      run_time=run_time / num_shakes)
            self.play(ApplyMethod(obj.shift, -dx * RIGHT - dy * UP),
                      run_time=run_time / num_shakes)
        self.play(ApplyMethod(obj.move_to, original_pos),
                  run_time=run_time / num_shakes)

################################################################################################################################################################
