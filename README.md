# Simple Roguelike

Um jogo de exploração de masmorras desenvolvido em Python com Pygame, como projeto de estudo de programação e desenvolvimento de jogos.

## Sobre o projeto

O Simple Roguelike é um jogo 2D com visão de cima (*top-down*), no qual o jogador explora uma masmorra formada por salas e corredores, enfrenta inimigos e administra seus pontos de vida e itens.

O projeto foi desenvolvido com fins educacionais, com foco no aprendizado de Python, programação orientada a objetos e desenvolvimento de jogos.

## Inspiração

O projeto foi inspirado em **Shattered Pixel Dungeon**, um jogo roguelike de exploração de masmorras. A proposta é utilizar elementos característicos do gênero como referência para desenvolver uma implementação própria, com mecânicas e código desenvolvidos para fins de aprendizado.

## Tecnologias utilizadas

- **Python:** linguagem de programação.
- **Pygame:** biblioteca utilizada para renderização, entrada de teclado e execução do jogo.
- **Git e GitHub:** controle de versão e hospedagem do código-fonte.

## Funcionalidades

- Exploração de mapas com salas e corredores.
- Movimentação por teclado.
- Câmera que acompanha o jogador.
- Combate por turnos.
- Inimigos com movimentação e ataques.
- Sistema de pontos de vida.
- Inventário com poções de cura.

## Como executar

### Pré-requisitos

- Python instalado.
- Git instalado (opcional, caso queira clonar o repositório).

### Instalação

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd SimpleRoguelike-py
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o jogo:

```bash
python main.py
```

## Controles

| Tecla | Ação |
|---|---|
| W / ↑ | Mover para cima |
| S / ↓ | Mover para baixo |
| A / ← | Mover para a esquerda |
| D / → | Mover para a direita |
| I | Abrir ou fechar o inventário |
| 1 | Usar poção de vida |
| ESC | Sair do jogo |

## Estrutura do projeto

```text
SimpleRoguelike-py/
├── main.py
├── requirements.txt
└── game/
    ├── __init__.py
    ├── personagem.py
    ├── player.py
    ├── inimigo.py
    ├── mapa.py
    └── inventario.py
```

## Objetivos de aprendizagem

- Aplicar conceitos de programação orientada a objetos.
- Trabalhar com classes, objetos, herança e métodos.
- Desenvolver sistemas de movimentação e combate por turnos.
- Gerenciar mapas, colisões e câmera em um jogo 2D.
- Praticar organização de código e controle de versão.

## Licença e créditos

Este projeto é independente e foi desenvolvido para fins educacionais. Shattered Pixel Dungeon é uma obra de terceiros e serviu como inspiração. Este projeto não é oficial nem possui afiliação com seus desenvolvedores.

A licença do projeto deverá ser definida pelo autor.
