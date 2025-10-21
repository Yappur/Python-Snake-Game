import pygame

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = "RIGHT"
        self.grow_pending = False

    def change_direction(self, new_direction):
        opposites = {"UP":"DOWN", "DOWN":"UP", "LEFT":"RIGHT", "RIGHT":"LEFT"}
        if new_direction != opposites.get(self.direction):
            self.direction = new_direction

    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= 20
        elif self.direction == "DOWN":
            y += 20
        elif self.direction == "LEFT":
            x -= 20
        elif self.direction == "RIGHT":
            x += 20

        new_head = (x, y)
        self.body.insert(0, new_head)

        if self.grow_pending:
            self.grow_pending = False
        else:
            self.body.pop()

    def grow(self):
        self.grow_pending = True

    def reset(self):
        """Reinicia la serpiente a su estado inicial"""
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = "RIGHT"
        self.grow_pending = False

    def draw(self, screen, color, cell_size):
        for (x, y) in self.body:
            pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
    
    def draw_neon(self, screen, color, cell_size):
        """Dibuja la serpiente con efecto neon"""
        # Verificar que el color sea válido
        try:
            if len(color) != 3:
                color = (0, 255, 127)  # Color por defecto si hay error
            r, g, b = color
            if not all(isinstance(c, int) and 0 <= c <= 255 for c in [r, g, b]):
                color = (0, 255, 127)  # Color por defecto si hay error
        except (ValueError, TypeError):
            color = (0, 255, 127)  # Color por defecto si hay error
        
        for i, (x, y) in enumerate(self.body):
            # Efecto de brillo más intenso para la cabeza
            if i == 0:
                # Dibujar múltiples capas para efecto glow
                for glow_size in range(3, 0, -1):
                    glow_surface = pygame.Surface((cell_size + glow_size*2, cell_size + glow_size*2))
                    glow_surface.set_alpha(50 // glow_size)
                    glow_surface.fill(color)
                    screen.blit(glow_surface, (x - glow_size, y - glow_size))
                
                # Cabeza principal
                pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
                
                # Ojos de la serpiente
                eye_size = cell_size // 4
                pygame.draw.rect(screen, (255, 255, 255), (x + eye_size, y + eye_size, eye_size, eye_size))
                pygame.draw.rect(screen, (255, 255, 255), (x + cell_size - eye_size*2, y + eye_size, eye_size, eye_size))
            else:
                # Cuerpo con efecto glow más sutil
                glow_surface = pygame.Surface((cell_size + 2, cell_size + 2))
                glow_surface.set_alpha(30)
                glow_surface.fill(color)
                screen.blit(glow_surface, (x - 1, y - 1))
                
                pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))