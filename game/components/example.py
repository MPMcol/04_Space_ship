import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Texto con salto de línea")

# Configurar los colores
background_color = (255, 255, 255)
text_color = (0, 0, 0)

# Configurar la fuente
font_size = 32
font = pygame.font.Font(None, font_size)

# Definir el texto con salto de línea
text = "Esto es\nun ejemplo\nde texto con\nsalto de línea."

# Dividir el texto en líneas separadas
lines = text.split("\n")

# Calcular el tamaño máximo de las líneas renderizadas
max_line_width = max(font.size(line)[0] for line in lines)
total_height = font_size * len(lines)

# Calcular la posición para centrar el texto en pantalla
text_x = (window_width - max_line_width) // 2
text_y = (window_height - total_height) // 2

# Bucle principal del juego
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Rellenar el fondo
    window.fill(background_color)

    # Renderizar cada línea de texto en la ventana
    for line in lines:
        text_surface = font.render(line, True, text_color)
        window.blit(text_surface, (text_x, text_y))
        text_y += font_size

    # Restablecer la posición vertical
    text_y = (window_height - total_height) // 2

    # Actualizar la ventana
    pygame.display.update()
