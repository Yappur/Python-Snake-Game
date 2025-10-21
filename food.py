import random
import pygame

class Food:
    def __init__(self, width, height, cell_size):
        self.cell_size = cell_size
        self.position = (0, 0)
        self.new_position(width, height, cell_size, [])

    def new_position(self, width, height, cell_size, snake_body):
        while True:
            x = random.randrange(0, width, cell_size)
            y = random.randrange(0, height, cell_size)
            if (x, y) not in snake_body:
                self.position = (x, y)
                break

    def draw(self, screen, color, cell_size):
        pygame.draw.rect(screen, color, (self.position[0], self.position[1], cell_size, cell_size))
    
    def draw_neon(self, screen, color, cell_size):
        """Dibuja la comida con efecto neon pulsante"""
        # Verificar que el color sea válido
        try:
            if len(color) != 3:
                color = (255, 20, 147)  # Color por defecto si hay error
            r, g, b = color
            if not all(isinstance(c, int) and 0 <= c <= 255 for c in [r, g, b]):
                color = (255, 20, 147)  # Color por defecto si hay error
        except (ValueError, TypeError):
            color = (255, 20, 147)  # Color por defecto si hay error
        
        x, y = self.position
        
        # Efecto de pulso
        import time
        pulse = 1.0 + 0.3 * abs(__import__('math').sin(time.time() * 8))
        
        # Dibujar múltiples capas para efecto glow
        for glow_size in range(4, 0, -1):
            glow_alpha = int(60 * pulse / glow_size)
            glow_surface = pygame.Surface((int(cell_size + glow_size*2), int(cell_size + glow_size*2)))
            glow_surface.set_alpha(glow_alpha)
            glow_surface.fill(color)
            screen.blit(glow_surface, (x - glow_size, y - glow_size))
        
        # Comida principal con efecto de pulso
        scaled_size = int(cell_size * pulse)
        offset = (cell_size - scaled_size) // 2
        pygame.draw.rect(screen, color, (x + offset, y + offset, scaled_size, scaled_size))
        
        # Centro brillante
        center_size = scaled_size // 2
        center_offset = (scaled_size - center_size) // 2
        pygame.draw.rect(screen, (255, 255, 255), 
                        (x + offset + center_offset, y + offset + center_offset, 
                         center_size, center_size))