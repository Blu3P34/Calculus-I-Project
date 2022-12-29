from manim import*

class introduction(Scene):
    def construct(self):
        intro1 = Text("Calculus I project")
        intro2 = Text("The application of Calculus I")
        self.play(Create(intro1), run_time = 2)
        self.play(ReplacementTransform(intro1,intro2))
        self.wait(2)

