from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        # Cria um rótulo para instruções
        self.label = MDLabel(text="Informe seu peso (kg) e altura (m):", halign="center")

        # Cria campos de texto para inserir o peso e altura
        self.weight_field = MDTextField(hint_text="Peso (kg)",
                                        pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.height_field = MDTextField(hint_text="Altura (m)",
                                        pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Cria um botão para calcular o IMC
        self.button = MDRectangleFlatButton(text="Calcular IMC",
                                            pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                            on_release=self.calculate_imc)

        # Cria um rótulo para exibir o resultado do IMC
        self.result_label = MDLabel(halign="center",
                                    pos_hint={'center_x': 0.5, 'center_y': 0.3})

        # Adiciona os widgets à tela
        self.add_widget(self.label)
        self.add_widget(self.weight_field)
        self.add_widget(self.height_field)
        self.add_widget(self.button)
        self.add_widget(self.result_label)

    def calculate_imc(self, instance):
        # Obtém os valores de peso e altura dos campos de texto
        weight = float(self.weight_field.text)
        height = float(self.height_field.text)

        # Calcula o IMC
        imc = weight / (height ** 2)

        # Cria uma string com o resultado do IMC
        result_text = f"Seu IMC é {imc:.2f}"

        # Determina a faixa de peso com base no IMC
        if imc < 18.5:
            result_text += "\nVocê está abaixo do peso."
        elif imc < 25:
            result_text += "\nSeu peso está dentro da faixa normal."
        elif imc < 30:
            result_text += "\nVocê está com sobrepeso."
        else:
            result_text += "\nVocê está obeso."

        # Atualiza o texto do rótulo de resultado
        self.result_label.text = result_text


class MyApp(MDApp):
    def build(self):
        # Configura o estilo do tema
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"

        # Cria a tela principal da aplicação
        screen = MainScreen(name='main')
        return screen


# Executa o aplicativo
MyApp().run()
