class Inventario:
    def __init__(self):
        self.itens = {
            "Pocao de vida": 3
        }

    def usar_pocao(self, jogador):
        if self.itens["Pocao de vida"] <= 0:
            return False

        if jogador.vida <= 0:
            return False

        if jogador.vida >= jogador.vida_maxima:
            return False

        cura = 30

        vida_anterior = jogador.vida
        jogador.vida = min(
            jogador.vida + cura,
            jogador.vida_maxima
        )

        vida_recuperada = jogador.vida - vida_anterior

        self.itens["Pocao de vida"] -= 1

        print(f"Voce recuperou {vida_recuperada} de vida!")

        return True
