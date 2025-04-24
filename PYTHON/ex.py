import pygame
import random

# Inicializando o Pygame
pygame.init()

# Constantes do jogo
LARGURA_TELA = 800
ALTURA_TELA = 600
VELOCIDADE_PERSONAGEM = 20  # Aumentamos ainda mais a velocidade do personagem
VELOCIDADE_BALA = 10  # Aumentamos a velocidade da bala para ter mais alcance
VELOCIDADE_INIMIGO = 3

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (213, 50, 80)
AZUL = (50, 153, 213)

# Tela do Jogo
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo de Tiro 2D")

# Fontes
fonte_pontos = pygame.font.SysFont("comicsansms", 35)

# Clock do jogo
clock = pygame.time.Clock()

# Classe do personagem


class Jogador:
    def __init__(self):
        self.x = LARGURA_TELA // 2
        self.y = ALTURA_TELA - 60
        self.largura = 50
        self.altura = 50
        self.velocidade = VELOCIDADE_PERSONAGEM
        self.cor = AZUL

    def mover(self, direcao):
        if direcao == 'esquerda' and self.x > 0:
            self.x -= self.velocidade
        if direcao == 'direita' and self.x < LARGURA_TELA - self.largura:
            self.x += self.velocidade
        if direcao == 'cima' and self.y > 0:
            self.y -= self.velocidade
        if direcao == 'baixo' and self.y < ALTURA_TELA - self.altura:
            self.y += self.velocidade

    def desenhar(self):
        pygame.draw.rect(tela, self.cor, (self.x, self.y,
                         self.largura, self.altura))

# Classe da bala


class Bala:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = 5
        self.altura = 10
        self.velocidade = VELOCIDADE_BALA
        self.cor = BRANCO

    def mover(self):
        self.y -= self.velocidade  # Mover a bala para cima

    def desenhar(self):
        pygame.draw.rect(tela, self.cor, (self.x, self.y,
                         self.largura, self.altura))

# Classe do inimigo


class Inimigo:
    def __init__(self):
        self.x = random.randint(0, LARGURA_TELA - 50)
        self.y = random.randint(-100, -40)
        self.largura = 50
        self.altura = 50
        self.velocidade = VELOCIDADE_INIMIGO
        self.cor = VERMELHO

    def mover(self):
        self.y += self.velocidade

    def desenhar(self):
        pygame.draw.rect(tela, self.cor, (self.x, self.y,
                         self.largura, self.altura))

# Função para exibir a pontuação


def mostrar_pontos(pontos):
    valor = fonte_pontos.render("Pontos: " + str(pontos), True, BRANCO)
    tela.blit(valor, [10, 10])

# Função de fim de jogo


def fim_de_jogo():
    mensagem = fonte_pontos.render(
        "Game Over! Pressione R para reiniciar ou Q para sair.", True, VERMELHO)
    tela.blit(mensagem, [LARGURA_TELA / 4, ALTURA_TELA / 2])
    pygame.display.update()

# Função principal


def main():
    jogador = Jogador()
    balas = []
    inimigos = [Inimigo()]
    pontos = 0
    jogo_rodando = True
    jogo_finalizado = False

    while jogo_rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jogador.mover('esquerda')
                if evento.key == pygame.K_RIGHT:
                    jogador.mover('direita')
                if evento.key == pygame.K_UP:
                    jogador.mover('cima')
                if evento.key == pygame.K_DOWN:
                    jogador.mover('baixo')
                if evento.key == pygame.K_SPACE and not jogo_finalizado:
                    # Criar 100 balas em sequência
                    for i in range(100):
                        balas.append(
                            Bala(jogador.x + jogador.largura // 2 - 2, jogador.y - (i * 2)))

        if not jogo_finalizado:
            # Mover balas
            for bala in balas[:]:
                bala.mover()
                if bala.y < 0:  # Remover a bala quando sair da tela
                    balas.remove(bala)

            # Mover inimigos
            for inimigo in inimigos[:]:
                inimigo.mover()
                if inimigo.y > ALTURA_TELA:  # Reiniciar inimigos que saem da tela
                    inimigos.remove(inimigo)
                    inimigos.append(Inimigo())

            # Verificar colisões entre balas e inimigos
            for bala in balas[:]:
                for inimigo in inimigos[:]:
                    if bala.x > inimigo.x and bala.x < inimigo.x + inimigo.largura:
                        if bala.y > inimigo.y and bala.y < inimigo.y + inimigo.altura:
                            balas.remove(bala)
                            inimigos.remove(inimigo)
                            inimigos.append(Inimigo())
                            pontos += 1
                            break

            # Verificar se o jogador foi atingido por um inimigo
            for inimigo in inimigos:
                if inimigo.x > jogador.x and inimigo.x < jogador.x + jogador.largura:
                    if inimigo.y > jogador.y and inimigo.y < jogador.y + jogador.altura:
                        jogo_finalizado = True
                        break

            # Desenhar tudo
            tela.fill(PRETO)
            jogador.desenhar()
            for bala in balas:
                bala.desenhar()
            for inimigo in inimigos:
                inimigo.desenhar()
            mostrar_pontos(pontos)

            pygame.display.update()
            clock.tick(60)

        if jogo_finalizado:
            fim_de_jogo()

            # Aguardar a resposta do jogador
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    jogo_rodando = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        jogo_rodando = False
                    if evento.key == pygame.K_r:
                        main()  # Reiniciar o jogo

    pygame.quit()


# Iniciar o jogo
if __name__ == "__main__":
    main()
