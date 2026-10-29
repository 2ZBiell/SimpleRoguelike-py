from game.personagem import Personagem

class Inimigo(Personagem):
    def __init__(self, nome, idade, vida, x, y):
        super().__init__(nome, idade, vida)

        self.x = x
        self.y = y
        self.ataque = 10
        self.cor = (220, 70, 70)

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)

    def agir(self, jogador, mapa):
        if self.vida <= 0 or jogador.vida <= 0:
            return

        distancia = (
            abs(self.x - jogador.x)
            + abs(self.y - jogador.y)
        )

        # Se estiver ao lado, ataca.
        if distancia == 1:
            jogador.receber_dano(self.ataque)
            return

        # Caso contrário, tenta se aproximar.
        dx = 0
        dy = 0

        if abs(jogador.x - self.x) > abs(jogador.y - self.y):
            dx = 1 if jogador.x > self.x else -1
        elif jogador.y != self.y:
            dy = 1 if jogador.y > self.y else -1
        elif jogador.x != self.x:
            dx = 1 if jogador.x > self.x else -1

        novo_x = self.x + dx
        novo_y = self.y + dy

        if mapa.pode_andar(novo_x, novo_y):
            if (novo_x, novo_y) != (jogador.x, jogador.y):
                self.x = novo_x
                self.y = novo_y
