from manim import*

class introduction(Scene):
    def construct(self):
        intro1 = Text("Calculus I project")
        intro2 = Text("The application of Calculus I")
        self.play(Create(intro1), run_time = 2)
        self.play(ReplacementTransform(intro1,intro2))
        self.wait(2)

class abstraction1(Scene):
    def construct(self):
        abstr = Text("I. Abstraction")
        calc1 = Text("Calculus I")
        deriv = Text("Derivatives").shift(UP)
        intgr = Text("Integrals")
        diffeq = Text("Differential equations").shift(DOWN)
        self.play(Create(abstr), run_time = 0.5)
        self.wait(2)
        self.play(ReplacementTransform(abstr,calc1), run_time = 0.5)
        self.wait(1)
        self.play(ReplacementTransform(calc1,deriv), run_time = 1)
        self.play(Create(intgr), run_time = 1)
        self.play(Create(diffeq), run_time = 1)
        self.wait(1)

class abstraction2(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[RED_D, RED_E], resolution=(15, 32)
        )
        text1 = Text("Volumn \nSurface area ")
        text2 = Text("?", font_size = 96)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(axes), run_time = 1)
        self.play(Create(sphere), run_time = 1)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait()
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Uncreate(axes), run_time = 0.5)
        self.play(Uncreate(sphere), run_time = 0.5)
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.play(Create(text1), run_time = 1)
        self.play(ReplacementTransform(text1,text2), run_time = 0.5)
        self.wait(1)

