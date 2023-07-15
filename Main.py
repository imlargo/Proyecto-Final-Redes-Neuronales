from manim import *
import itertools as it
import random

red = "aa70ff"
cream = "#ffc4f7"

#---------------------------------------------------#
#Proyecto Final Introduccion Ingenieria de Sistemas:
#Video Redes Neuronales
#...................................................
#Creado por Juan Carlos Largo
#---------------------------------------------------#
        
        
class All(Scene):
    arguments = {
        "network_size": 1.5,
        "network_position": ORIGIN,
        "layer_sizes": [3, 5, 5, 3],
        "layer_buff": LARGE_BUFF,
        "neuron_radius": 0.15,
        "neuron_color": cream,
        "neuron_width": 3,
        "neuron_fill_color": BLACK,
        "neuron_fill_opacity": 1,
        "neuron_buff": MED_SMALL_BUFF,
        "edge_color": "#ffffff",
        "edge_width": 1.25,
        "edge_opacity": 0.75,
        "layer_label_color": WHITE,
        "layer_label_size": 0.5,
        "neuron_label_color": WHITE
    }

    def construct(self):
        
        #---Presentacion---
        self.Codigo()
        self.clear()
        #---Intro---
        self.Intro()
        self.clear()
        #---Estructura---
        self.Neurona()
        self.Layers()
        self.Conexiones()
        #---Aprendizaje---
        self.Entrenamiento()
        self.Aprendizaje()
        self.Funcion_costo()
        self.Retropropagacion()
        self.Final()

    def Codigo(self):
        # --- DESPEDIDA ---
        code = '''import manim

class Saludo(Scene):
    def construct(self):
        self.play(Write(Tex("Redes Neuronales")))
        self.wait()
        self.play(Write(Tex("Proyecto Final :)")))
        self.wait()
'''
        titulo = Tex("Todo el código usado en este video será de uso libre")
        rendered_code = Code(code=code, tab_width=4, background="window", language="Python", font="Monospace")
        self.play(Write(titulo))
        self.play(titulo.animate.next_to(rendered_code, UP, buff=0.5))
        self.play(Create(rendered_code))
        self.wait(3)
   
    def Intro(self):
        encabezado = Tex("¿Qué es una Red Neuronal?.").to_corner(UP + LEFT)
        titulo = Tex("Redes Neuronales").scale(1.25)
        sep = Line(start=titulo.get_left(), end=titulo.get_right(), color=WHITE, buff=0.5).next_to(titulo, DOWN, buff=0.5)
        aut = Tex("Por: Juan Carlos Largo y Jimena Hernandez")
        aut.next_to(sep, DOWN, buff=0.5)
        
        tipos = ["Convolucionales", "Generativas", "Long-Short Term Memory (ChatGPT)", "Recurrentes (RNN)", "...", "Diferentes Estructuras"]
        size = 0.7
        types = VGroup(*[Tex(tipo).scale(size) for tipo in tipos])
        types.arrange(DOWN, buff=0.5)
        types.shift(LEFT * 3.5)
        lista = ["Aprendizaje Supervisado", "Aprendizaje no Supervisado", "Aprendizaje por Reforzamiento", "...", "Cálculo Avanzado", "Álgebra Lineal"]
        types2 = VGroup(*[Tex(tipo).scale(size) for tipo in lista])
        types2.arrange(DOWN, buff=0.5)
        types2.shift(RIGHT * 3.5)
        
        self.play(Write(titulo), Create(sep), Write(aut), run_time = 1)
        self.wait(4)
        self.play(FadeOut(sep),FadeOut(aut))
        self.play(Transform(titulo, encabezado))
        self.wait()
        
        self.add_neuronsIntro()
        self.edge_security()
        layers = self.layers
        salida = Arrow(start=LEFT, end=RIGHT).scale(0.8, scale_tips = True).next_to(layers, RIGHT, buff=0.2)
        aviso = Tex("Tigre!").next_to(salida, RIGHT, buff=0.3)
        meme = ImageMobject("/content/meme2.JPG").scale(1).next_to(layers, LEFT, buff=0.5)    
            
        self.play(FadeIn(meme), run_time = 0.5)
        self.continual_animation()
        self.wait(3)
        self.play(Write(aviso), Create(salida), run_time = 0.5)
        self.wait(4)
        self.play(FadeOut(aviso), FadeOut(salida), run_time = 0.5)
        self.wait(5)
        
        self.play(FadeOut(self.layers, self.edges, meme))
        
        self.play(Write(types), run_time = 1)
        self.wait(3)
        self.play(Write(types2), run_time = 1)
        self.wait(6)
        self.play(FadeOut(types, types2, titulo))
             
    def Neurona(self):
        speed = 0.2
        neuron = Circle(color=PURPLE_A)
        active = Circle(color=PURPLE_A, fill_opacity = 0.6)
        neuronas = (Tex("La Red Neuronal.").to_corner(UP + LEFT))
        texto = Tex("La Neurona.")
        valor = Tex("0.1")
        entrada  = Arrow(start=LEFT, end=RIGHT).next_to(neuron, LEFT, buff=0.5)
        salida = Arrow(start=LEFT, end=RIGHT).next_to(neuron, RIGHT, buff=0.5)
        salida_t = Tex("Salida").next_to(salida, DOWN, buff=0.5).scale(0.7)
        entrada_t = Tex("Entrada").next_to(entrada, DOWN, buff=0.5).scale(0.7)
        meme = ImageMobject("/content/Meme1.jpg").scale(1.5).next_to(salida, RIGHT, buff=0.4)

        self.play(Write(texto))
        self.play(texto.animate.next_to(neuron, UP, buff=0.5))
        self.play(Create(neuron))
        self.wait(2)
        
        self.play(Write(valor), Create(entrada), Write(entrada_t), run_time =0.3) 
        self.wait(11)
        
        aviso = Tex("Los pesos se ajustan durante el proceso de entrenamiento de la red").scale(0.8).next_to(neuron, DOWN, buff=1) 
        self.play(Write(aviso),  Transform(valor, Tex("0.4")), run_time = 1)
        self.wait(3)
        self.wait(1)
        self.play(FadeOut(aviso))
        
        aviso = MathTex(r"peso_{1} \cdot entrada_{1} + peso_{2} \cdot entrada_{2} + c").next_to(neuron, DOWN, buff=0.51).scale(0.8)
        self.play(Write(aviso), Transform(valor, Tex("0.2")),  run_time = 1)
        self.wait(2)
        self.wait(2)
        self.play(FadeOut(aviso))
        
        aviso2 = Tex("Por ejemplo la función ReLU, Sigmoid").next_to(neuron, DOWN, buff=0.5).scale(0.8)
        aviso = Tex("(Busca evitar la linealidad en la salida de la neurona)").scale(0.7).next_to(aviso2, DOWN, buff=0.5) 
        self.play(Write(aviso2), Transform(valor, Tex("0.3")), run_time = 1)
        self.wait(4)
        self.play(Write(aviso), Transform(valor, Tex("0.5")), run_time = 1)
        self.wait(10)
        
        self.play(FadeOut(aviso, aviso2))
        
        self.play(Transform(valor, Tex("0.2")), run_time=0.5)
        self.play(Transform(valor, Tex("0.4")), run_time=0.5)
        self.play(Transform(valor, Tex("0.5")), run_time=0.5)
        self.play(Transform(valor, Tex("0.9")), Transform(neuron, active), run_time=0.5)
        self.play(Write(salida_t), Create(salida), FadeIn(meme),  run_time = 0.5)
        self.wait(3)

        self.play(FadeOut(neuron, active, valor, entrada, salida, entrada_t, salida_t, meme), Transform(texto, neuronas))
    
    def Layers(self):
        layers = VGroup(*[self.get_layer(size) for size in All.arguments["layer_sizes"]])
        layers.arrange(RIGHT, buff=All.arguments["layer_buff"])
        layers.scale(All.arguments["network_size"])
        layers.shift(All.arguments["network_position"])
        self.layers = layers

        #...Capa Entrada
        self.play(Write(layers[0]))
        self.wait(1)
        self.play(Write(layers[1:3]))
        self.wait(1)
        self.play(Write(layers[3]))
        self.wait(3)
        
        enfasis = SurroundingRectangle(layers[0], color= TEAL_C, buff=0.51)
        self.play(Create(enfasis), run_time=0.5)
        self.play(FadeOut(enfasis), run_time=0.5)
        self.wait(1)
        
        enfasis = SurroundingRectangle(layers[1:3], color= TEAL_C, buff=0.51)
        self.play(Create(enfasis), run_time=0.5)
        self.play(FadeOut(enfasis), run_time=0.5)
        self.wait(1)
        
        enfasis = SurroundingRectangle(layers[3], color= TEAL_C, buff=0.51)
        self.play(Create(enfasis), run_time=0.5)
        self.play(FadeOut(enfasis), run_time=0.5)
        
        enfasis = SurroundingRectangle(layers[0], color= TEAL_C, buff=0.51)
        tag_capa = Tex("Capa de Entrada").next_to(enfasis, UP, buff=0.2).scale(0.6)
        anuncio = Tex("Claramente la estructura puede ser mucho más grande").next_to(layers, DOWN, buff=0.5).scale(0.6)
        self.play(Create(enfasis), Write(tag_capa), Write(anuncio), run_time=1)
        self.wait(5)
        self.play(FadeOut(enfasis, anuncio))
        
        #...Capa Oculta
        enfasis = SurroundingRectangle(layers[1:3], color= TEAL_C, buff=0.51)
        tag_capa = Tex('Capas "Ocultas"').next_to(enfasis, UP, buff=0.2).scale(0.6)
        anuncio = Tex("La estructura de una red neuronal puede variar en complejidad y tamaño dependiendo de la tarea y los datos específicos").next_to(layers, DOWN, buff=0.5).scale(0.6)
        self.play(Create(enfasis), Write(tag_capa), Write(anuncio), run_time=1)
        self.wait(8)
        self.play(FadeOut(enfasis, anuncio))
        
        #...Capa Salida
        enfasis = SurroundingRectangle(layers[3], color= TEAL_C, buff=0.51)
        tag_capa = Tex("Capa de Salida").next_to(enfasis, UP, buff=0.2).scale(0.6)
        anuncio = Tex("").next_to(layers, DOWN, buff=0.5).scale(0.6)
        self.play(Create(enfasis), Write(tag_capa), Write(anuncio), run_time=1)
        self.wait(9)
        self.play(FadeOut(enfasis, anuncio))
        #...............

    def Conexiones(self):
    
        layers = self.layers
        entrada  = Arrow(start=LEFT, end=RIGHT).next_to(layers, RIGHT, buff=0.4)
        salida = Arrow(start=LEFT, end=RIGHT).next_to(layers, LEFT, buff=0.4)            
        anuncio = Tex("Al activarse cierta neurona, puede hacer que la siguiente se active").next_to(layers, DOWN, buff=0.5).scale(0.6)
        self.edge_groups = VGroup()

        self.label_neurons()
        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            for n1, n2 in it.product(l1.neurons, l2.neurons):
                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
            self.play(Write(edge_group), run_time=2)
            self.edge_groups.add(edge_group)
        
        self.wait(1)
        self.reajustar()
        self.wait(5)
        self.play(Create(salida), Write(anuncio), run_time = 0.3)
        self.pulso()
        self.play(Create(entrada), run_time = 0.3)
        self.wait(3)
        self.play(FadeOut(entrada, salida, anuncio))
        self.wait(2)
        anuncio = Tex("¿Por qué capas?").next_to(layers, DOWN, buff=0.5).scale(0.6)
        self.play(Write(anuncio), run_time = 0.3)
        self.pulse_animation_2()
        self.pulse_animation_2()
        self.wait(2)
        self.play(FadeOut(anuncio))
            
    def Entrenamiento(self):
        write_speed = 0.5
        layers = self.layers
        edges = self.edge_groups
        labels = self.neuronLabels
        self.Network = VGroup(layers, edges, labels)
        network = self.Network
        titulo = (Tex("Entrenamiento.").to_corner(UP + LEFT))
        texto = Tex("Entrenamiento.")
        tipos = ["Aprendizaje:", "...", "Supervisado", "No supervisado", "Por refuerzo", "..."]
        types = VGroup(*[Tex(tipo).scale(0.7) for tipo in tipos])
        types.arrange(DOWN, buff=0.5)
        types.shift(LEFT * 5)
        entrada  = Arrow(start=LEFT, end=RIGHT).next_to(network, LEFT, buff=0.5).scale(0.7, scale_tips=True)
        salida  = Arrow(start=LEFT, end=RIGHT).next_to(network, RIGHT, buff=0.5).scale(0.7, scale_tips=True)
        good = Arrow(start=DOWN, end=UP, color = GREEN_B).next_to(network, RIGHT, buff=0.5).scale(0.7, scale_tips=True)
        bad = Arrow(start=UP, end=DOWN, color = RED_B).next_to(network, RIGHT, buff=0.5).scale(0.7, scale_tips=True)
             
        self.clear()
        
        self.play(Write(texto), run_time = write_speed)
        self.wait()
        self.play(Transform(texto, titulo), run_time = 1)
        self.play(Create(network), run_time = 1)
        
        self.wait(2)

        activa = self.activar_neurona(capa = -1, neurona = -1, light = 0.6)
        self.play(Create(entrada), run_time = write_speed)
        self.pulso()
        self.pulse_animation()
        self.pulse_animation()
        self.play(Create(bad), FadeIn(activa), run_time = write_speed)
        self.reajustar()
        self.play(FadeOut(bad, entrada), FadeOut(activa), run_time = 0.1)

        aviso = Tex("Datos de entrenamiento").next_to(network, DOWN, buff=0.5).scale(0.7)
        aviso2 = Tex("Datos de entrenamiento de buena calidad!").next_to(network, DOWN, buff=0.5).scale(0.7)
        activa = self.activar_neurona(capa = -1, neurona = 1, light = 0.6)
        
        self.wait(4)

        self.play(Create(types), run_time = write_speed)
        self.pulso()
        self.pulse_animation()
        self.pulse_animation()
        self.play(Create(good), FadeIn(activa), run_time = write_speed)
        self.wait(2)
        self.play(Write(aviso), run_time = write_speed)
        self.reajustar()
        self.play(FadeOut(good, activa), run_time = 0.1)
        self.wait(2)
        self.play(Transform(aviso, aviso2), FadeOut(types), run_time = write_speed) 
        
        #Trash in - Trash out
        trashin = ImageMobject("/content/trash.png").scale(0.1).next_to(entrada, LEFT, buff=0.2)
        trashout = ImageMobject("/content/trash.png").scale(0.1).next_to(salida, RIGHT, buff=0.2)
        trash = MathTex(r"???").next_to(network, UP, buff=0.1).scale(0.8)
        self.play(Create(entrada), FadeIn(trashin), run_time = write_speed)
        self.pulso()
        self.play(Create(salida), FadeIn(trashout, trash), run_time = write_speed)
        self.wait()
        self.play(FadeOut(aviso, aviso2, entrada, salida, trashin, trashout, trash), run_time = write_speed)
        
        #“Medida de error”
        margen = Tex("Precision:").scale(0.6).next_to(network, DOWN, buff=0.5)
        margen_value = Tex("0"+ "\%").scale(0.6).next_to(margen, RIGHT, buff=0.2)
                
        self.play(Write(margen), Write(margen_value), run_time = write_speed)
        
        activa = self.activar_neurona(capa = -1, neurona = (random.randint(0, 2)), light = 0.6)
        tag = Tex("Incorrecto", color = RED_C).next_to(activa, RIGHT, buff=0.5).scale(0.6)
        self.pulso()
        self.play(FadeIn(activa, tag), run_time = 0.3)
        for x in range(0, 45):
            new = Tex(f"{x}" + "\%").scale(0.6).next_to(margen, RIGHT, buff=0.2)
            self.play(Transform(margen_value, new), run_time = 0.001)
        self.play(FadeOut(activa, tag), run_time = 0.1)

        
        activa = self.activar_neurona(capa = -1, neurona = (random.randint(0, 2)), light = 0.6)
        tag = Tex("Correcto", color = GREEN_C).next_to(activa, RIGHT, buff=0.5).scale(0.6)
        self.pulso()
        self.play(FadeIn(activa, tag), run_time = 0.3)
        for x in range(45, 76):
            new = Tex(f"{x}" + "\%").scale(0.6).next_to(margen, RIGHT, buff=0.2)
            self.play(Transform(margen_value, new), run_time = 0.001)
        self.play(FadeOut(activa, tag), run_time = 0.1)
        
        activa = self.activar_neurona(capa = -1, neurona = (random.randint(0, 2)), light = 0.6)
        tag = Tex("Correcto", color = GREEN_C).next_to(activa, RIGHT, buff=0.5).scale(0.6)
        self.pulso()
        self.play(FadeIn(activa, tag), run_time = 0.3)
        for x in range(76, 81):
            new = Tex(f"{x}" + "\%").scale(0.6).next_to(margen, RIGHT, buff=0.2)
            self.play(Transform(margen_value, new), run_time = 0.001)
        self.play(FadeOut(activa, tag), run_time = 0.1)
        
        activa = self.activar_neurona(capa = -1, neurona = (random.randint(0, 2)), light = 0.6)
        tag = Tex("Correcto", color = GREEN_C).next_to(activa, RIGHT, buff=0.5).scale(0.6)
        self.pulso()
        self.play(FadeIn(activa, tag), run_time = 0.3)
        for x in range(81, 97):
            new = Tex(f"{x}" + "\%").scale(0.6).next_to(margen, RIGHT, buff=0.2)
            self.play(Transform(margen_value, new), run_time = 0.001)
        self.play(FadeOut(activa, tag), run_time = 0.1)
        self.play(FadeOut(margen, margen_value, texto), run_time = 0.1)
        self.clear()
        
    def Aprendizaje(self):
        write_speed = 0.5
        layers = self.layers
        edges = self.edge_groups
        labels = self.neuronLabels
        network = self.Network
        texto = Tex("¿Cómo aprende realmente?.")
        
        self.play(Write(texto), run_time = write_speed)
        self.wait()
        #La funcion de Activacion
        self.play(Transform(texto, (Tex("La función de activación.").to_corner(UP + LEFT))))
        self.wait()
        
        #Recordemos el inicio de la neurona
        All.arguments["layer_sizes"] = [3, 1]
        self.add_neurons()
        self.etiquetar()
        self.add_edges()
        ejemplo = VGroup(self.layers, self.edge_groups, self.neuronLabels)
        meme = ImageMobject("/content/Meme1.jpg").scale(1).next_to(ejemplo, RIGHT, buff=0.5).set_opacity(0.8)
        
        All.arguments["layer_sizes"] = [3, 5, 5, 3]
        pesos = VGroup()
        self.wait()
        for n, edge in enumerate(self.edge_groups[0]):
            t = "p_" + f"{n+1}"
            tag = MathTex(t).next_to(edge, RIGHT, buff= -1).scale(0.6)
            tag.add_background_rectangle(color = BLACK ,opacity = 1)
            pesos.add(tag)
        self.play(Write(pesos), run_time = 0.2)
        
        
        activa = self.activar_neurona(capa = -1, neurona = 0, light = 0.6)
        calculo = MathTex(r"(p_{1} \cdot x_{1}) + (p_{2} \cdot x_{2}) + (p_{3} \cdot x_{3}) + c").next_to(self.layers, DOWN, buff=0.5).scale(0.7)
        valor = MathTex(r"(valor)").next_to(self.layers, DOWN, buff=0.5).scale(0.7)
        relu = MathTex(r"R(valor)").next_to(self.layers, DOWN, buff=0.5).scale(0.7)
        funcion = MathTex(r"R(x) = max\left \{ 0, x \right \} = (Funcion \; de \; activacion \; ReLU)").next_to(valor, DOWN, buff=0.3).scale(0.6)
        pensando = MathTex(r"...").next_to(self.layers[-1].neurons[0], UP, buff=0.1).scale(0.7)
        done = MathTex(r"!").next_to(self.layers[-1].neurons[0], UP, buff=0.1).scale(0.7)
        
        for x in range(7):
            self.pulso()
            self.wait(1)
        self.pulso()
        self.play(Write(calculo), run_time = write_speed)
        self.wait(2)
        self.play(Transform(calculo, valor), Write(pensando), run_time = write_speed)
        self.wait(3)
        self.play(Transform(calculo, relu), FadeIn(funcion), Transform(pensando, done), run_time = write_speed)
        self.wait(2)
        
        self.play(FadeIn(activa, meme), run_time = write_speed)
        self.wait(1)
        self.play(FadeOut(meme))
        
        self.wait(1)
        
        self.play(FadeOut(calculo, pensando, activa, pesos, funcion, texto), run_time = write_speed)
        self.play(Transform(ejemplo, network), run_time = 1)
        self.layers = layers
        self.edge_groups = edges 
        self.neuronLabels = labels
        self.clear()

    def Funcion_costo(self):
        All.arguments["layer_sizes"] = [3, 5, 5, 3]
        
        write_speed = 0.5
        layers = self.layers
        edges = self.edge_groups
        network = self.Network
        self.add(network)
        
        titulo = Tex("La función de costo.").to_corner(UP + LEFT)
        aviso = Tex("Matemáticamente es una función muy compleja, y de muchas dimensiones\nque toma como entrada las conexiones, pesos y valores").next_to(network, DOWN, buff=0.5).scale(0.7)
        rabia = ImageMobject("/content/rabia.png").scale(0.3).next_to(network, LEFT, buff=0).shift((UP * 1.7 )+ (RIGHT * 1.4)) 
        boink = ImageMobject("/content/Bonk.png").scale(0.5).next_to(network, LEFT, buff=0.2)
        entrada  = Arrow(start=LEFT, end=RIGHT).next_to(network, LEFT, buff=0.5).scale(0.6, scale_tips=True)
        
        self.play(FadeIn(titulo))
        self.wait(3)
        self.play(Write(aviso), run_time = 1)
        self.wait(4)

        #- - - Primer Ejemplo  - - -
        activa1 = self.activar_neurona(capa = -1, neurona = 1, light = 0.2)
        activa2 = self.activar_neurona(capa = -1, neurona = 0, light = 0.4)
        activa3 = self.activar_neurona(capa = -1, neurona = 2, light = 0.7)
        
        good = Arrow(start=UP, end=DOWN, color = GREEN_B).scale(0.3, scale_tips=True).next_to(activa3, RIGHT, buff=0.1)
        bad2 = Arrow(start=UP, end=DOWN, color = RED_B).scale(0.3, scale_tips=True).next_to(activa1, RIGHT, buff=0.1)
        bad3 = Arrow(start=UP, end=DOWN, color = RED_B).scale(0.3, scale_tips=True).next_to(activa2, RIGHT, buff=0.1)

        tag1 = Tex("Casi correcto", color = GREEN_C).scale(0.6).next_to(good, RIGHT, buff=0.2)
        tag2 = Tex("Incorrecto", color = RED_C).scale(0.6).next_to(bad2, RIGHT, buff=0.2)
        tag3 = Tex("MUY Incorrecto", color = RED_C).scale(0.6).next_to(bad3, RIGHT, buff=0.2)
        
        
        self.play(Create(entrada), run_time = 1)
        self.pulso()
        self.play(Create(good), Create(bad2), Create(bad3), Write(tag1),  Write(tag2), Write(tag3), FadeIn(activa1, activa2, activa3, rabia), run_time = 1)
        self.wait(1)
        self.play(FadeOut(good, bad2, bad3, tag1, tag2, tag3, entrada, activa1, activa2, activa3, rabia), run_time = 0.2)
        self.wait(1)
        
        #- - - Matriz  - - -
        matriz = Matrix([[r"\hat{y}_{1}"], [r"\hat{y}_{2}"], [r"\hat{y}_{3}"], [r"..."]])
        tag1 = Tex("+ 0.1", color = GREEN_C).scale(0.8).next_to((matriz.get_rows())[0], RIGHT, buff=0.7)
        tag2 = Tex("- 0.3", color = RED_C).scale(0.8).next_to((matriz.get_rows())[1], RIGHT, buff=0.7)
        tag3 = Tex("+ 0.2", color = RED_C).scale(0.8).next_to((matriz.get_rows())[2], RIGHT, buff=0.7)
        
        matrix = VGroup(matriz, tag1, tag2, tag3).scale(0.8)
        matrix.next_to(network, LEFT, buff=0.5)

        
        #- - - SEGUNDO Ejemplo  - - -        
        target1 = edges[-1][-1]
        ajust1 = (MathTex(r"w_{2} + ?").scale(0.6).next_to(target1, DOWN + (RIGHT * 0.2), buff=0.2)).add_background_rectangle(color = BLACK ,opacity = 1)
        target2 = edges[-1][0]
        ajust2 = (MathTex(r"w_{0} - ?").scale(0.6).next_to(target2, UP + (RIGHT * 0.2), buff=0.2)).add_background_rectangle(color = BLACK ,opacity = 1)
        target3 = edges[-1][1]
        ajust3 = (MathTex(r"w_{1} - ?").scale(0.6).next_to(target3, UP * 3, buff=0.2)).add_background_rectangle(color = BLACK ,opacity = 1)
        target4 = edges[-1][-2]
        ajust4 = (MathTex(r"w_{3} + ?").scale(0.6).next_to(target4, DOWN * 3, buff=0.2)).add_background_rectangle(color = BLACK ,opacity = 1)
        
        line1 = Line(ajust1,target1.get_center(),buff=1.25,stroke_color=All.arguments["edge_color"],stroke_width=All.arguments["edge_width"],stroke_opacity=All.arguments["edge_opacity"])
        line2 = Line(ajust2,target2.get_center(),buff=1.25,stroke_color=All.arguments["edge_color"],stroke_width=All.arguments["edge_width"],stroke_opacity=All.arguments["edge_opacity"])
        line3 = Line(ajust3,target3.get_center(),buff=1.25,stroke_color=All.arguments["edge_color"],stroke_width=All.arguments["edge_width"],stroke_opacity=All.arguments["edge_opacity"])
        line4 = Line(ajust4,target4.get_center(),buff=1.25,stroke_color=All.arguments["edge_color"],stroke_width=All.arguments["edge_width"],stroke_opacity=All.arguments["edge_opacity"])
        
        activa1 = self.activar_neurona(capa = -1, neurona = 1, light = 0.2)
        activa2 = self.activar_neurona(capa = -1, neurona = 2, light = 0.4)
        activa3 = self.activar_neurona(capa = -1, neurona = 0, light = 0.7)
        
        good = Arrow(start=UP, end=DOWN, color = GREEN_B).scale(0.3, scale_tips=True).next_to(activa3, RIGHT, buff=0.1)
        bad2 = Arrow(start=UP, end=DOWN, color = GREEN_B).scale(0.3, scale_tips=True).next_to(activa1, RIGHT, buff=0.1)
        bad3 = Arrow(start=UP, end=DOWN, color = RED_B).scale(0.3, scale_tips=True).next_to(activa2, RIGHT, buff=0.1)

        tag1 = Tex("Correcto", color = GREEN_C).scale(0.6).next_to(good, RIGHT, buff=0.2)
        tag2 = Tex("Casi correcto", color = GREEN_B).scale(0.6).next_to(bad2, RIGHT, buff=0.2)
        tag3 = Tex("Incorrecto", color = RED_C).scale(0.6).next_to(bad3, RIGHT, buff=0.2)
        
        self.play(Create(entrada), run_time = 1)
        self.pulso()
        self.play(FadeOut(entrada), run_time = 1)
        self.play(Create(good), Create(bad2), Create(bad3), Write(tag1),  Write(tag2), Write(tag3), FadeIn(activa1, activa2, activa3), FadeIn(rabia, line1, line2, line3, line4, ajust1, ajust2, ajust3, ajust4, matrix), run_time = 1)
        self.wait()
        self.reajustar()
        self.wait()
        self.play(FadeOut(aviso, titulo, good, bad2, bad3, tag1, tag2, tag3, activa1, activa2, activa3, matrix, line1, line2, line3, line4, ajust1, ajust2, ajust3,ajust4), run_time = 0.5)
        self.wait(1)
        self.play(FadeIn(boink), run_time = 1)
        self.reajustar()
        self.wait(1)
        self.reajustar()
        self.wait(3)
        self.play(FadeOut(rabia, boink))
 
    def Retropropagacion(self):
        
        write_speed = 0.5
        layers = self.layers
        edges = self.edge_groups
        labels = self.neuronLabels
        network = self.Network
        self.create_reverse_edges()
        
        aviso = Tex("(Detrás de esto hay mucha matematica)").next_to(network, DOWN, buff=0.5).scale(0.7)
        nerd = ImageMobject("/content/nerd.png").scale(0.05).next_to(network, UP, buff=0.01)
        entrada  = Arrow(start=LEFT, end=RIGHT).next_to(network, LEFT, buff=0.5).scale(0.6, scale_tips=True)
        titulo = Tex("Retropropagación.").to_corner(UP + LEFT)
        activa1 = self.activar_neurona(capa = -1, neurona = 1, light = 0.2)
        activa2 = self.activar_neurona(capa = -1, neurona = 0, light = 0.4)
        activa3 = self.activar_neurona(capa = -1, neurona = 2, light = 0.7)
        good = Arrow(start=UP, end=DOWN, color = GREEN_B).scale(0.3, scale_tips=True).next_to(activa3, RIGHT, buff=0.1)
        bad2 = Arrow(start=UP, end=DOWN, color = RED_B).scale(0.3, scale_tips=True).next_to(activa1, RIGHT, buff=0.1)
        bad3 = Arrow(start=UP, end=DOWN, color = RED_B).scale(0.3, scale_tips=True).next_to(activa2, RIGHT, buff=0.1)

        tag1 = Tex("Casi correcto", color = GREEN_C).scale(0.6).next_to(good, RIGHT, buff=0.2)
        tag2 = Tex("Incorrecto", color = RED_C).scale(0.6).next_to(bad2, RIGHT, buff=0.2)
        tag3 = Tex("MUY Incorrecto", color = RED_C).scale(0.6).next_to(bad3, RIGHT, buff=0.2)
        
        #Inicia
        self.play(Write(titulo))
        self.wait(2)
        self.play(Write(aviso), run_time = 1)
        
        self.wait(4)
        #Animacion
        self.play(Create(entrada), run_time = 0.2)
        self.pulso()
        self.play(Create(good), Create(bad2), Create(bad3), Write(tag1),  Write(tag2), Write(tag3), FadeIn(activa1, activa2, activa3), run_time = 1)
        #self.pulse_animation_reverse()
        self.wait()
        self.pulso_reverse()
        self.pulso_reverse()
        self.pulso_reverse()
        self.reajustar()
        self.play(FadeIn(nerd), run_time = 1)
        self.play(FadeOut(good, bad2, bad3, tag1, tag2, tag3, entrada, activa1, activa2, activa3), run_time = 0.5)
        self.wait(2)
        self.play(FadeOut(aviso, network, nerd), run_time = 1)
        
    
        #A forma de vector
        matriz = Matrix([[r"p{_{1}}"], [r"p{_{2}}"], [r"p{_{3}}"], [r"..."], [r"p{_{97}}"], [r"p{_{98}}"], [r"p{_{99}}"]]).scale(0.8)
        aviso = Tex("(De manera simplificada, es mucho más complejo)").next_to(matriz, DOWN, buff=0.5).scale(0.7)
        matriz_c = Matrix([[r"p{_{1}}"], [r"p{_{2}}"], [r"p{_{3}}"], [r"..."], [r"p{_{97}}"], [r"p{_{98}}"], [r"p{_{99}}"]]).scale(0.8)
        matriz_v = Matrix([[r"-0.5"], [r"0.3"],[r"-0.7"],[r"..."],[r"0.1"],[r"-0.4"],[r"0.3"],]).scale(0.8)
        
        tag1 = Tex("Debe aumentar + 0.1", color = GREEN_C).scale(0.8).scale(0.8).next_to((matriz.get_rows())[0], RIGHT, buff=0.7)
        tag2 = Tex("Debe aumentar + 0.2", color = GREEN_C).scale(0.8).scale(0.8).next_to((matriz.get_rows())[1], RIGHT, buff=0.7)
        tag3 = Tex("Debe disminuir - 0.3", color = RED_C).scale(0.8).scale(0.8).next_to((matriz.get_rows())[2], RIGHT, buff=0.7)
        
        tag4 = Tex("Debe disminuir - 0.3", color = RED_C).scale(0.8).scale(0.8).next_to((matriz.get_rows())[4], RIGHT, buff=0.7)
        tag5 = Tex("Debe aumentar + 0.1", color = GREEN_C).scale(0.8).scale(0.8).next_to((matriz.get_rows())[5], RIGHT, buff=0.7)
        tag6 = Tex("Debe disminuir - 0.2", color = RED_C).scale(0.8).scale(0.8).next_to((matriz.get_rows())[6], RIGHT, buff=0.7)
        
        name = MathTex(r"\vec{Pesos} = ").scale(0.8).next_to(matriz, LEFT, buff=0.2)
        tags = VGroup(tag1, tag2, tag3, tag4, tag5, tag6)
        
        self.play(Write(name), Write(aviso), run_time = 0.5)
        self.wait()
        self.play(Write(matriz), run_time = 0.5)
        self.wait(1)
        self.play(Transform(matriz, matriz_v), run_time = 0.5)
        self.wait(1)
        self.play(Transform(matriz, matriz_c), run_time = 0.5)
        self.wait(1)
        self.play(Write(tags), run_time = 0.5)
        self.wait(5)
        self.play(FadeOut(matriz, name, tags, aviso, titulo))
        

    def Final(self):
        network = self.Network
        bigbrain = ImageMobject("/content/BigBrain.png").scale(0.7).next_to(network, RIGHT, buff=0.01)
        nerd = ImageMobject("/content/nerd.png").scale(0.05).next_to(network, UP, buff=0.01)
        parcial = Tex("Momento de parcial!").next_to(network, DOWN, buff=0.5).scale(0.7)
        
        cheem = ImageMobject("/content/Ohno.png").scale(0.35).next_to(network,LEFT, buff=0.01)
        ohno = Tex("Oh no..").next_to(cheem, UP, buff=0.1).scale(0.5)
        
        self.play(Create(network), FadeIn(nerd), FadeIn(Tex("Conclusión.").to_corner(UP + LEFT)), run_time = 2)
        for x in range(3):
            self.pulso()
            self.pulso_reverse()
            self.reajustar()
        
        self.play(Write(parcial), FadeOut(nerd), run_time = 0.5)
        self.play(FadeIn(cheem), Write(ohno), run_time = 0.5)
        self.wait(3)
        self.play(FadeOut(parcial, cheem, ohno), run_time = 0.5)
        
        self.play(FadeOut(self.edge_groups))
        aviso = Tex("Lista para dominar el mundo").next_to(network, DOWN, buff=0.5).scale(0.7)
        self.edge_security()
        self.continual_animation()
        self.play(FadeIn(bigbrain), Write(aviso), run_time = 0.5)
        
        self.wait(7)
    
    def activar_neurona(self, capa, neurona, light):
        layers = self.layers
        layers_copy = layers.copy()
        return (layers_copy[capa].neurons[neurona]).set_fill(color=All.arguments["neuron_color"], opacity = light)
        
    def pulse_animation(self):
        edge_group = self.edge_groups.copy()
        edge_group.set_stroke(TEAL_C, 6)  # color, width
        self.play(LaggedStartMap(ShowPassingFlash, edge_group), run_time = 0.5)
            
    def pulse_animation_reverse(self):
        edge_group = self.reverse_edges.copy()
        edge_group.set_stroke(TEAL_C, 6)  # color, width
        self.play(LaggedStartMap(ShowPassingFlash, edge_group), run_time = 0.5)
     
    def add_neuronsIntro(self):
        layers = VGroup(*[self.get_layer(size) for size in [3,5,5,3]])
        layers.arrange(RIGHT, buff=All.arguments["layer_buff"])
        layers.scale(All.arguments["network_size"])
        self.layers = layers
        layers.shift(All.arguments["network_position"])
        self.play(Write(layers), run_time = 0.1)
            
    def pulse_animation_2(self):
        pulsos = 7
        velocidad = 1
        edge_group = VGroup(*it.chain(*self.edge_groups))
        edge_group = edge_group.copy()
        edge_group.set_stroke(TEAL_C, 6)  # color, width
        for i in range(pulsos):
            self.play(LaggedStartMap(
                ShowPassingFlash, edge_group,
                run_time=velocidad))
            
    def pulso(self):
        edge_group = VGroup(*it.chain(*self.edge_groups))
        edge_group = edge_group.copy()
        edge_group.set_stroke(TEAL_C, 6)  # color, width
        self.play(LaggedStartMap(
            ShowPassingFlash, edge_group,
            run_time=1))
        
    def pulso_reverse(self):
        edge_groups = self.reverse_edges
        
        edge_group = VGroup(*it.chain(*edge_groups))
        edge_group = edge_group.copy()
        edge_group.set_stroke(TEAL_C, 6)  # color, width
        self.play(LaggedStartMap(ShowPassingFlash,edge_group,run_time=1))
        
    def create_reverse_edges(self):
        edge_groups = VGroup()
        a = [self.layers[-1], self.layers[-2], self.layers[-3]]
        b = [self.layers[-2], self.layers[-3], self.layers[-4]]
        for l1, l2 in zip(a,b ):
            edge_group = VGroup()
            for n1, n2 in it.product(l1.neurons, l2.neurons):
                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
            edge_groups.add(edge_group)
        self.reverse_edges = edge_groups
        
    def add_neurons(self):
        layers = VGroup(*[self.get_layer(size) for size in All.arguments["layer_sizes"]])
        layers.arrange(RIGHT, buff=All.arguments["layer_buff"])
        layers.scale(All.arguments["network_size"])
        self.layers = layers
        layers.shift(All.arguments["network_position"])
        self.play(Write(layers))

    def get_layer(self, size):
        layer = VGroup()
        n_neurons = size
        neurons = VGroup(*[
            Circle(
                radius=All.arguments["neuron_radius"],
                stroke_color=All.arguments["neuron_color"],
                stroke_width=All.arguments["neuron_width"],
                fill_color=All.arguments["neuron_fill_color"],
                fill_opacity=All.arguments["neuron_fill_opacity"],
            )
            for i in range(n_neurons)
        ])
        neurons.arrange(DOWN, buff=All.arguments["neuron_buff"])
        layer.neurons = neurons
        layer.add(neurons)
        return layer

    def edge_security(self):
        self.edge_groups = VGroup()
        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            for n1, n2 in it.product(l1.neurons, l2.neurons):
                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
            self.edge_groups.add(edge_group)

    def add_edges(self):
        self.edge_groups = VGroup()
        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            for n1, n2 in it.product(l1.neurons, l2.neurons):
                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
            self.play(Write(edge_group), run_time=0.5)
            self.edge_groups.add(edge_group)

    def get_edge(self, neuron1, neuron2):
        return Line(
            neuron1.get_center(),
            neuron2.get_center(),
            buff=1.25*All.arguments["neuron_radius"],
            stroke_color=All.arguments["edge_color"],
            stroke_width=All.arguments["edge_width"],
            stroke_opacity=All.arguments["edge_opacity"]
        )

    def etiquetar(self):
        time = 0.1
        
        allLabels = VGroup()
        for x in range(len(self.layers)):
            layer_labels = VGroup()
            for n, neuron in enumerate(self.layers[x].neurons):
                if x == 0:
                    label = MathTex(f"x_{n + 1}") 
                elif x == (len(self.layers) - 1):
                    label = MathTex(f"y_{n + 1}") 
                else:
                    label = MathTex(f"h_{n + 1}") 
                    
                label.set_height(0.3 * neuron.get_height())
                label.set_color(All.arguments["neuron_label_color"])
                label.move_to(neuron)
                layer_labels.add(label)
            self.play(Write(layer_labels), run_time = time)
            allLabels.add(layer_labels)
        self.neuronLabels = allLabels
        
    def label_neurons(self):
        time = 0.5
        input_labels = VGroup()
        
        for n, neuron in enumerate(self.layers[0].neurons):
            label = MathTex(f"x_{n + 1}")
            label.set_height(0.3 * neuron.get_height())
            label.set_color(All.arguments["neuron_label_color"])
            label.move_to(neuron)
            input_labels.add(label)
        self.play(Write(input_labels), run_time = time)

        hidden_labels1 = VGroup()
        for n, neuron in enumerate(self.layers[1].neurons):
            label = MathTex(f"h_{n + 1}")
            label.set_height(0.3 * neuron.get_height())
            label.set_color(All.arguments["neuron_label_color"])
            label.move_to(neuron)
            hidden_labels1.add(label)
        self.play(Write(hidden_labels1), run_time = time)

        hidden_labels2 = VGroup()
        for n, neuron in enumerate(self.layers[2].neurons):
            label = MathTex(f"h_{n + 6}")
            label.set_height(0.3 * neuron.get_height())
            label.set_color(All.arguments["neuron_label_color"])
            label.move_to(neuron)
            hidden_labels2.add(label)
        self.play(Write(hidden_labels2), run_time = time)

        output_labels = VGroup()
        for n, neuron in enumerate(self.layers[-1].neurons):
            label = MathTex(r"\hat{y}_" + "{" + f"{n + 1}" + "}")
            label.set_height(0.4 * neuron.get_height())
            label.set_color(All.arguments["neuron_label_color"])
            label.move_to(neuron)
            output_labels.add(label)
        self.play(Write(output_labels), run_time = time)
        self.wait()
        
        self.neuronLabels = VGroup(output_labels, hidden_labels1, hidden_labels2, input_labels)

    def reajustar(self):
        edges = VGroup(*it.chain(*self.edge_groups))
        self.play(LaggedStartMap(
            ApplyFunction, edges,
            lambda mob: (lambda m: m.rotate(np.pi/24).set_color(TEAL_A), mob),
            rate_func=wiggle), run_time = 2)

    def continual_animation(self):
        args = {
            "colors": [TEAL_C, LIGHT_PINK, PURPLE_A, WHITE],
            "n_cycles": 8,
            "max_width": 5,
            "exp_width": 7
        }
        self.internal_time = 1
        self.move_to_targets = []
        edges = VGroup(*it.chain(*self.edge_groups))
        for edge in edges:
            edge.colors = [random.choice(args["colors"]) for i in range(args["n_cycles"])]
            msw = args["max_width"]
            edge.widths = [msw * random.random()**args["exp_width"] for i in range(args["n_cycles"])]
            edge.cycle_time = 1 + random.random()

            edge.generate_target()
            edge.target.set_stroke(edge.colors[0], edge.widths[0])
            edge.become(edge.target)
            self.move_to_targets.append(edge)

        self.edges = edges
        animation = self.edges.add_updater(lambda m, dt: self.update_edges(dt))
        self.play(FadeIn(animation), run_time=0.05)

    def update_edges(self, dt):
        self.internal_time += dt
        if self.internal_time < 1:
            alpha = smooth(self.internal_time)
            for i in self.move_to_targets:
                i.update(alpha)
            return
        for edge in self.edges:
            t = (self.internal_time-1)/edge.cycle_time
            alpha = ((self.internal_time-1)%edge.cycle_time)/edge.cycle_time
            low_n = int(t)%len(edge.colors)
            high_n = int(t+1)%len(edge.colors)
            color = interpolate_color(edge.colors[low_n], edge.colors[high_n], alpha)
            width = interpolate(edge.widths[low_n], edge.widths[high_n], alpha)
            edge.set_stroke(color, width)

    def fast_pulse(self):
        edge_group = VGroup(*it.chain(*self.edge_groups))
        edge_group = edge_group.copy()
        edge_group.set_stroke(TEAL_C, 6)  # color, width
        self.play(LaggedStartMap(
            ShowPassingFlash, edge_group,
            run_time=0.6))
        
    def fast_pulse_reverse(self):
        edge_groups = self.reverse_edges
        
        edge_group = VGroup(*it.chain(*edge_groups))
        edge_group = edge_group.copy()
        edge_group.set_stroke(TEAL_C, 6)  # color, width
        self.play(LaggedStartMap(ShowPassingFlash,edge_group,run_time=0.6))