from game.personagem import Personagem


class Jogador(Personagem):
    def __init__(self, nome, idade, vida, x, y):
        super().__init__(nome, idade, vida)

        self.x = x
        self.y = y
        self.ataque = 25
        self.cor = (70, 170, 255)

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)

    def mover(self, dx, dy, mapa):
        novo_x = self.x + dx
        novo_y = self.y + dy

        if mapa.pode_andar(novo_x, novo_y):
            self.x = novo_x
            self.y = novo_y
            return True

        return False
