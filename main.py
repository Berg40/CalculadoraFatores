import flet as ft
import math


def main(page: ft.Page):
    page.title = "Calculadora Prof.Augusto"
    page.scroll = ft.ScrollMode.AUTO

    page.update()
    # Funções de cálculo
    def calcular_forca(e):
        try:
            massa = float(massa_input.value)
            aceleracao = float(aceleracao_input.value)
            forca = massa * aceleracao
            resultado.value = f"""Caro Augusto o resultado foi: 
Força (F) = {forca} N"""
        except ValueError:
            resultado.value = "Por favor, insira valores numéricos válidos."
        page.update()

    def calcular_energia_cinetica(e):
        try:
            massa = float(massa_input.value)
            velocidade = float(velocidade_input.value)
            energia_cinetica = 0.5 * massa * (velocidade ** 2)
            resultado.value = f"""Caro Augusto o resultado foi:
Energia Cinética (K.E.) = {energia_cinetica} J"""
        except ValueError:
            resultado.value = "Por favor, insira valores numéricos válidos."
        page.update()

    def calcular_energia_potencial(e):
        try:
            massa = float(massa_input.value)
            altura = float(altura_input.value)
            gravidade = 9.81  # Constante da gravidade
            energia_potencial = massa * gravidade * altura
            resultado.value = f"""Caro Augusto o resultado foi:
Energia Potencial Gravitacional (P.E.) = {energia_potencial} J"""
        except ValueError:
            resultado.value = "Por favor, insira valores numéricos válidos."
        page.update()

    def calcular_trabalho(e):
        try:
            forca = float(forca_input.value)
            deslocamento = float(deslocamento_input.value)
            angulo = float(angulo_input.value)
            trabalho = forca * deslocamento * math.cos(math.radians(angulo))
            resultado.value = f"""Caro Augusto o resultado foi:
Trabalho (W) = {trabalho} J"""
        except ValueError:
            resultado.value = "Por favor, insira valores numéricos válidos."
        page.update()

    # Elementos de entrada de dados
    massa_input = ft.TextField(label="Massa (kg)", width=200, color=ft.colors.BLACK, text_size=20)
    aceleracao_input = ft.TextField(label="Aceleração (m/s²)", width=200, color=ft.colors.BLACK, text_size=20)
    velocidade_input = ft.TextField(label="Velocidade (m/s)", width=200, color=ft.colors.BLACK, text_size=20)
    altura_input = ft.TextField(label="Altura (m)", width=200, color=ft.colors.BLACK, text_size=20)
    forca_input = ft.TextField(label="Força (N)", width=200, color=ft.colors.BLACK, text_size=20)
    deslocamento_input = ft.TextField(label="Deslocamento (m)", width=200, color=ft.colors.BLACK, text_size=20)
    angulo_input = ft.TextField(label="Ângulo (graus)", width=200, color=ft.colors.BLACK, text_size=20)

    # Label para exibir o resultado
    resultado = ft.Text(value="", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD, size=20)

    # Botões para cálculo
    botao_forca = ft.ElevatedButton("Calcular Força", on_click=calcular_forca)
    botao_energia_cinetica = ft.ElevatedButton("Calcular Energia Cinética", on_click=calcular_energia_cinetica)
    botao_energia_potencial = ft.ElevatedButton("Calcular Energia Potencial", on_click=calcular_energia_potencial)
    botao_trabalho = ft.ElevatedButton("Calcular Trabalho", on_click=calcular_trabalho)

    # Adicionando os controles à página
    page.add(
        ft.Container(
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.WHITE54, ft.colors.GREY_600]
            ),
            margin=0,
            padding=10,

            content=ft.Column(
                spacing=20,
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(value="Calculadora de Fatores Físicos", size=30, weight=ft.FontWeight.BOLD),
                    ft.Text("Insira os valores necessários para cada cálculo:", size=20),
                    ft.Divider(),

                    ft.Text(value="Força (F) = Massa (kg) × Aceleração (m/s²)",
                            size=18,
                            color=ft.colors.BLACK
                            ),
                    massa_input,
                    aceleracao_input,
                    botao_forca,

                    ft.Divider(),
                    ft.Text(value="Energia Cinética (K.E.) = ½ × Massa (kg) × Velocidade² (m/s)",
                            color=ft.colors.BLACK,
                            size=18,
                            ),
                    massa_input,
                    velocidade_input,
                    botao_energia_cinetica,

                    ft.Divider(),
                    ft.Text(value="Energia Potencial Gravitacional (P.E.) = Massa (kg) × Gravidade (9.81 m/s²) × Altura (m)",
                            color=ft.colors.BLACK,
                            size=18
                            ),
                    massa_input,
                    altura_input,
                    botao_energia_potencial,

                    ft.Divider(),
                    ft.Text(value="Trabalho (W) = Força (N) × Deslocamento (m) × cos(θ)",
                            color=ft.colors.BLACK,
                            size=18
                            ),
                    forca_input,
                    deslocamento_input,
                    angulo_input,
                    botao_trabalho,

                    ft.Divider(),
                    resultado,
                    ft.Divider()

                ]
            )
        )
    )


# Rodar o app
ft.app(target=main)

