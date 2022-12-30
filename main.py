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

        self.play(Create(abstr), run_time = 1)
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

class eco1(Scene):
     def construct(self):
        eco = Text("II. Economic Trend")
        text = Text("Derivatives").shift(2*UP)
        deri = MathTex( r"f'(x) = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x} = \frac{dy}{dx}").shift(3.4*UP)
        axes = (
            Axes(
                x_range = [0,10,1],
                x_length = 9,
                y_range = [0,20,5],
                y_length = 6,
                axis_config={"include_numbers": True, "include_tip": False}
            ).to_edge(DL).set_color(GREY)
            )
        axes_label = axes.get_axis_labels(x_label ="x", y_label="f(x)")

        func = axes.plot(
            lambda x : 0.1*(x-2)*(x-5)*(x-7)+7, x_range = [0,10], color = BLUE
        )

        x = ValueTracker(7)
        dx = ValueTracker(2)

        secant = always_redraw(
            lambda : axes.get_secant_slope_group(
                x = x.get_value(),
                graph = func,
                dx = dx.get_value(),
                dx_line_color = YELLOW,
                dy_line_color = ORANGE,
                dx_label = "dx",
                dy_label = "dy",
                secant_line_color = GREEN,
                secant_line_length = 8,)
            )

        dot1 = always_redraw(
            lambda: Dot().scale(0.7).move_to(axes.c2p(x.get_value(), func.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(
            lambda: Dot().scale(0.7).move_to(axes.c2p((x).get_value() + dx.get_value(), func.underlying_function(x.get_value() + dx.get_value())))
        )
        self.play(Create(eco), run_time = 1)
        self.wait(1)
        self.play(ReplacementTransform(eco,text), run_time = 1)
        self.wait(2)
        self.play(ReplacementTransform(text,deri), Create( VGroup(axes, axes_label)), run_time = 3)
        self.wait(2)
        self.play(Create(func), run_time = 5)
        self.play(Create(VGroup(dot1, dot2, secant)), run_time = 5)
        self.play(dx.animate.set_value(0.001), run_time = 4)
        self.wait(1)
        self.play(x.animate.set_value(1), run_time = 4)
        self.wait(1)
        self.play(x.animate.set_value(7), run_time = 4)
        self.wait(1)
  
    
        
        

