from manim import *

class OneBadDay(Scene):
    def construct(self):
        # Create Axes
        axes = Axes(
            x_range=[0, 10],
            y_range=[0, 6],
            axis_config={"color": WHITE},
        ).scale(0.9).to_edge(DOWN)

        # Define Points for the Graph Path
        graph_points = [
            axes.coords_to_point(0, 0),
            axes.coords_to_point(1, 1),
            axes.coords_to_point(2, 0.5),
            axes.coords_to_point(3, 2),
            axes.coords_to_point(4, 1),
            axes.coords_to_point(5, 3),
            axes.coords_to_point(6, 2),
            axes.coords_to_point(7, 4),
            axes.coords_to_point(8, 3.5),
            axes.coords_to_point(9, 5),
        ]

        # Create Graph Line (Initially Red for "bad day" part)
        graph_line = VMobject()
        graph_line.set_points_as_corners(graph_points)
        graph_line.set_stroke(RED, width=4)

        # Character Silhouette
        character = ImageMobject("character.png").scale(0.15)
        character.move_to(graph_points[0])

        # Texts
        text1 = Text("One bad day", font_size=64, color=WHITE).to_edge(UP)
        text2 = Text("is not a bad life", font_size=64, color=GREEN).next_to(text1, DOWN)

        # Animations Start
        self.play(Create(axes))
        self.play(Create(graph_line), FadeIn(text1), FadeIn(character))
        self.wait(0.5)

        # Character Walking Animation
        self.play(MoveAlongPath(character, graph_line), run_time=6, rate_func=linear)
        self.wait(0.5)

        # Change Graph Color to Green after bad day
        green_line = graph_line.copy().set_color(GREEN)
        self.play(Transform(graph_line, green_line))

        # Show Motivational Text
        self.play(FadeIn(text2))

        # Glow Effect
        glow_circle = Circle(radius=0.5, color=GREEN, fill_opacity=0.4).move_to(graph_points[-1])
        self.play(Indicate(glow_circle, scale_factor=2), run_time=2)

        self.wait(2)

