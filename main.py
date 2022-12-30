from manim import*

class introduction(Scene):
    def construct(self):
        intro1 = Text("Calculus I project")
        intro2 = Text("The application of Calculus I")
        self.play(Create(intro1), run_time = 2)
        self.play(ReplacementTransform(intro1,intro2))
        self.play(FadeOut(intro2), run_time = 2)

class abstraction1(Scene):
    def construct(self):
        abstr = Text("I. Abstraction")
        calc1 = Text("Calculus I")
        deriv = Text("Derivatives").shift(UP)
        intgr = Text("Integrals")
        diffeq = Text("Differential equations").shift(DOWN)
        framebox1 = SurroundingRectangle(deriv, buff = 0.1)
        framebox2 = SurroundingRectangle(intgr, buff = 0.1)
        framebox3 = SurroundingRectangle(diffeq, buff = 0.1)
        self.play(Create(abstr), run_time = 1)
        self.wait(1)
        self.play(ReplacementTransform(abstr,calc1), run_time = 1)
        self.wait(3)
        self.play(ReplacementTransform(calc1,deriv), Create(framebox1), run_time = 2)
        self.play(Create(intgr), ReplacementTransform(framebox1, framebox2), run_time = 2)
        self.play(Create(diffeq), ReplacementTransform(framebox2, framebox3), run_time = 2)
        self.play(Uncreate(framebox3), run_time = 1)
        self.wait(6)

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
        text3 = Text("Issac Newton      Gottfried Leibniz").shift(2*DOWN)
        img = ImageMobject("assets/Newton-Leibniz.jpg").scale(2).next_to(text3, UP)

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
        self.play(ReplacementTransform(text2, text3), run_time = 1)
        self.add(img)
        self.wait(5)
     
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

class archi1(Scene):
    def construct(self):
        archi = Text("III. Architectures")
         
        self.play(Create(archi))
        self.wait(1)

class harmo1(Scene):
    def construct(self):
        text0 = Text("III. Sound processing")
        texta = Text("Calculus")
        textb = Text("Music")
        textc = Text("Sound processing")
        C = MathTex(r"C_4 = 262 Hz").shift(UP*3)
        D = MathTex(r"D_4 = 294 Hz").shift(UP*2)
        E = MathTex(r"E_4 = 330 Hz").shift(UP*1)
        F = MathTex(r"F_4 = 349 Hz")
        G = MathTex(r"G_4 = 342 Hz").shift(DOWN*1)
        A = MathTex(r"A_4 = 440 Hz").shift(DOWN*2)
        B = MathTex(r"B_4 = 494 Hz").shift(DOWN*3)
        CM = MathTex(r"C\,major = C + G + E")
        AM = MathTex(r"A\,major = A + C\# + E")
        axes1 = Axes(x_range = [0,10,1], y_range = [-1,1,1], x_length = 10, y_length = 1, axis_config = {"include_tip": False})
        axis_labels1 = axes1.get_axis_labels(x_label = "t", y_label = "x(t)")
        graph1 = axes1.plot(lambda x : np.cos(2*x), x_range = [0,10], color = RED)
        text1 = MathTex(r"f = 2f_0").next_to(axes1, RIGHT, buff = 0.5)
        sound1 = VGroup(axes1, graph1, axis_labels1, text1).to_corner(UL, buff = 0.3)

        axes2 = Axes(x_range = [0,10,1], y_range = [-1,1,1], x_length = 10, y_length = 1, axis_config = {"include_tip": False})
        axis_labels2 = axes2.get_axis_labels(x_label = "t", y_label = "y(t)")
        graph2 = axes2.plot(lambda x : np.cos(3*x), x_range = [0,10], color = RED)
        text2 = MathTex(r"f = 3f_0").next_to(axes2, RIGHT, buff = 0.5)
        sound2 = VGroup(axes2, graph2, axis_labels2, text2).next_to(sound1, DOWN, buff = 0.3)

        axes3 = Axes(x_range = [0,10,1], y_range = [-2,2,1], x_length = 10, y_length = 2, axis_config = {"include_tip": False})
        axis_labels3 = axes3.get_axis_labels(x_label = "t", y_label = "z(t) = x(t) + y(t)")
        graph3 = axes3.plot(lambda x : np.cos(2*x) + np.cos(3*x), x_range = [0,10], color = RED)
        text3 = MathTex(r"f = f_0").next_to(axes3, RIGHT, buff = 0.5)
        sound3 = VGroup(axes3, graph3, axis_labels3, text3).next_to(sound2, DOWN, buff = 0.3)
        
        self.play(Create(text0), run_time = 1)
        self.wait(1)
        self.play(ReplacementTransform(text0,texta), run_time = 1)
        self.play(Rotate(texta, PI/4), run_time = 1)
        self.play(Rotate(texta, -PI/2), run_time = 1)
        self.play(Rotate(texta, PI/4), run_time = 1)
        self.play(Rotate(texta, PI/4), run_time = 1)
        self.play(Rotate(texta, -PI/2), run_time = 1)
        self.play(Rotate(texta, PI/4), run_time = 1)
        self.play(Rotate(texta, PI/4), run_time = 1)
        self.play(Rotate(texta, -PI/2), run_time = 1)
        self.play(Rotate(texta, PI/4), run_time = 1)
        self.play(ReplacementTransform(texta,textb), run_time = 1)
        self.wait(1)
        self.play(ReplacementTransform(textb,textc), run_time = 1)
        self.play(FadeOut(textc), run_time = 1)
        self.play(Write(C), run_time = 2)
        self.play(Write(D), run_time = 2)
        self.play(Write(E), run_time = 2)
        self.play(Write(F), run_time = 2)
        self.play(Write(G), run_time = 2)
        self.play(Write(A), run_time = 2)
        self.play(Write(B), run_time = 2)
        self.play(FadeOut(A),FadeOut(B),FadeOut(C),FadeOut(D),FadeOut(F),FadeOut(G),FadeOut(E), run_time = 1)
        self.play(Write(CM),run_time = 1)
        self.wait()
        self.play(ReplacementTransform(CM, AM), run_time = 1)
        self.wait()
        self.play(FadeOut(AM), run_time = 1)
        self.play(DrawBorderThenFill(axes1), DrawBorderThenFill(axes2), DrawBorderThenFill(axes3), Write(axis_labels1),Write(axis_labels2),Write(axis_labels3))
        self.play(Create(graph1),Create(graph2),Create(graph3),Write(text1),Write(text2),Write(text3))
        self.wait(4)
        self.play(FadeOut(sound1),FadeOut(sound2),FadeOut(sound3))

        
        


  
    
        
        

