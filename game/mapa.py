class Mapa:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

        # Todas as posições começam como paredes.
        self.paredes = {
            (x, y)
            for x in range(largura)
            for y in range(altura)
        }

        # Cada sala é representada por (x, y, largura, altura).
        self.salas = [
            (2, 2, 8, 6),
            (15, 3, 8, 7),
            (29, 2, 8, 6),
            (4, 14, 9, 7),
            (19, 15, 8, 6),
            (30, 20, 7, 7),
            (13, 24, 7, 4),
        ]

        self.criar_salas()
        self.criar_corredores()

    def criar_salas(self):
        for x, y, largura, altura in self.salas:
            for pos_y in range(y, y + altura):
                for pos_x in range(x, x + largura):
                    self.paredes.discard((pos_x, pos_y))

    def centro_sala(self, indice):
        x, y, largura, altura = self.salas[indice]

        centro_x = x + largura // 2
        centro_y = y + altura // 2

        return centro_x, centro_y

    def criar_corredor(self, inicio, fim):
        x1, y1 = inicio
        x2, y2 = fim

        # Primeiro, andamos na horizontal.
        passo_x = 1 if x2 >= x1 else -1

        for x in range(x1, x2 + passo_x, passo_x):
            self.paredes.discard((x, y1))

        # Depois, andamos na vertical.
        passo_y = 1 if y2 >= y1 else -1

        for y in range(y1, y2 + passo_y, passo_y):
            self.paredes.discard((x2, y))

    def criar_corredores(self):
        # Ligações entre as salas.
        conexoes = [
            (0, 1),
            (1, 2),
            (0, 3),
            (3, 4),
            (4, 5),
            (4, 6),
        ]

        for sala_a, sala_b in conexoes:
            inicio = self.centro_sala(sala_a)
            fim = self.centro_sala(sala_b)

            self.criar_corredor(inicio, fim)

    def pode_andar(self, x, y):
        dentro_do_mapa = (
            0 <= x < self.largura
            and 0 <= y < self.altura
        )

        return dentro_do_mapa and (x, y) not in self.paredes
