import pygame
import sys
import time
from snake import Snake
from food import Food
from highscores import HighScores
from sounds import SoundManager
from synthwave_effects import SynthwaveEffects

pygame.init()

# Configuración pantalla
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

# Colores synthwave
BLACK = (0, 0, 0)
NEON_GREEN = (0, 255, 127)
NEON_PINK = (255, 20, 147)
NEON_CYAN = (0, 255, 255)
NEON_PURPLE = (138, 43, 226)
NEON_ORANGE = (255, 165, 0)
GRID_COLOR = (50, 50, 100)

clock = pygame.time.Clock()

def get_player_name(effects):
    """Permite al jugador ingresar su nombre"""
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)
    player_name = ""
    last_time = time.time()
    
    while True:
        # Calcular delta time
        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time
        
        # Actualizar efectos
        effects.update(dt)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and player_name.strip():
                    return player_name.strip()
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    # Solo permitir letras, números y espacios
                    if event.unicode.isalnum() or event.unicode == ' ':
                        if len(player_name) < 15:  # Limitar longitud
                            player_name += event.unicode
        
        # Dibujar efectos de fondo
        effects.draw_all_effects(screen)
        
        # Título con efecto neon
        title_text = font.render("¡NUEVA PUNTUACIÓN ALTA!", True, NEON_PINK)
        title_rect = title_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 80))
        screen.blit(title_text, title_rect)
        
        # Instrucciones
        instruction_text = small_font.render("Ingresa tu nombre:", True, NEON_CYAN)
        instruction_rect = instruction_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 40))
        screen.blit(instruction_text, instruction_rect)
        
        # Campo de entrada con efecto pulsante
        cursor_blink = "_" if int(time.time() * 2) % 2 else ""
        name_text = font.render(player_name + cursor_blink, True, NEON_GREEN)
        name_rect = name_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(name_text, name_rect)
        
        # Instrucciones de control
        control_text = small_font.render("ENTER para confirmar | ESC para salir", True, NEON_CYAN)
        control_rect = control_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 40))
        screen.blit(control_text, control_rect)
        
        pygame.display.update()
        clock.tick(15)

def show_high_scores(high_scores):
    """Muestra la tabla de puntuaciones altas"""
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Reiniciar juego
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        
        screen.fill(BLACK)
        
        # Título
        title_text = font.render("PUNTUACIONES ALTAS", True, NEON_CYAN)
        title_rect = title_text.get_rect(center=(WIDTH//2, 50))
        screen.blit(title_text, title_rect)
        
        # Mostrar puntuaciones
        y_offset = 100
        scores = high_scores.get_scores()
        
        if not scores:
            no_scores_text = small_font.render("No hay puntuaciones registradas", True, NEON_PINK)
            no_scores_rect = no_scores_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(no_scores_text, no_scores_rect)
        else:
            for i, score_data in enumerate(scores):
                rank_text = small_font.render(f"{i+1}.", True, NEON_GREEN)
                name_text = small_font.render(f"{score_data['name']}", True, NEON_CYAN)
                score_text = small_font.render(f"{score_data['score']} puntos", True, NEON_PINK)
                
                # Posicionar elementos
                rank_rect = rank_text.get_rect(center=(WIDTH//2 - 100, y_offset + i * 40))
                name_rect = name_text.get_rect(center=(WIDTH//2, y_offset + i * 40))
                score_rect = score_text.get_rect(center=(WIDTH//2 + 100, y_offset + i * 40))
                
                screen.blit(rank_text, rank_rect)
                screen.blit(name_text, name_rect)
                screen.blit(score_text, score_rect)
        
        # Instrucciones
        restart_text = small_font.render("Presiona R para jugar de nuevo o Q para salir", True, NEON_ORANGE)
        restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT - 50))
        screen.blit(restart_text, restart_rect)
        
        pygame.display.update()
        clock.tick(10)

def show_main_menu(high_scores, effects):
    """Muestra el menú principal del juego"""
    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 24)
    last_time = time.time()
    
    while True:
        # Calcular delta time
        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time
        
        # Actualizar efectos
        effects.update(dt)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True  # Empezar juego
                elif event.key == pygame.K_h:
                    # Mostrar puntuaciones altas
                    show_high_scores(high_scores)
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        
        # Dibujar efectos de fondo
        effects.draw_all_effects(screen)
        
        # Título del juego con efecto neon
        title_text = font.render("SNAKE GAME 𓆗", True, NEON_CYAN)
        title_rect = title_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 100))
        screen.blit(title_text, title_rect)
        
        # Instrucciones
        start_text = small_font.render("Presiona ESPACIO para empezar", True, NEON_GREEN)
        start_rect = start_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 20))
        screen.blit(start_text, start_rect)
        
        high_scores_text = small_font.render("Presiona H para ver puntuaciones altas", True, NEON_PINK)
        high_scores_rect = high_scores_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))
        screen.blit(high_scores_text, high_scores_rect)
        
        quit_text = small_font.render("Presiona Q para salir", True, NEON_ORANGE)
        quit_rect = quit_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
        screen.blit(quit_text, quit_rect)
        
        pygame.display.update()
        clock.tick(15)

def game_loop(sound_manager, effects):
    snake = Snake()
    food = Food(WIDTH, HEIGHT, CELL_SIZE)
    score = 0
    last_time = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snake.change_direction("UP")
        if keys[pygame.K_DOWN]:
            snake.change_direction("DOWN")
        if keys[pygame.K_LEFT]:
            snake.change_direction("LEFT")
        if keys[pygame.K_RIGHT]:
            snake.change_direction("RIGHT")

        snake.move()

        # Calcular delta time para efectos
        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time

        # Actualizar efectos visuales
        effects.update(dt)

        # Colisión con comida
        if snake.body[0] == food.position:
            snake.grow()
            food.new_position(WIDTH, HEIGHT, CELL_SIZE, snake.body)
            score += 1
            # Reproducir sonido de comer comida
            sound_manager.play_eat_food()
            # Agregar efecto de explosión
            effects.add_explosion_effect(food.position[0], food.position[1], NEON_GREEN)

        # Colisión con límites
        x, y = snake.body[0]
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            break

        # Colisión con sí mismo
        if snake.body[0] in snake.body[1:]:
            break

        # Dibujar efectos de fondo
        effects.draw_all_effects(screen)
        
        # Dibujar serpiente con efecto neon (usar color fijo por ahora)
        snake.draw_neon(screen, NEON_GREEN, CELL_SIZE)
        
        # Dibujar comida con efecto neon (usar color fijo por ahora)
        food.draw_neon(screen, NEON_PINK, CELL_SIZE)

        pygame.display.update()
        clock.tick(15)  # Aumentar FPS para efectos más fluidos

    return score

def show_game_over_screen(score, high_scores, sound_manager):
    """Muestra la pantalla de Game Over con opción de reiniciar"""
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)
    
    # Verificar si es una puntuación alta
    is_high_score = high_scores.is_high_score(score)
    
    # Reproducir sonido de game over
    sound_manager.play_game_over()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Reiniciar juego
                elif event.key == pygame.K_h:
                    # Mostrar puntuaciones altas
                    show_high_scores(high_scores)
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        
        screen.fill(BLACK)
        
        # Texto Game Over
        game_over_text = font.render("GAME OVER!", True, NEON_PINK)
        game_over_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 80))
        screen.blit(game_over_text, game_over_rect)
        
        # Puntuación
        score_text = font.render(f"Puntuación: {score}", True, NEON_CYAN)
        score_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 40))
        screen.blit(score_text, score_rect)
        
        # Mensaje especial si es puntuación alta
        if is_high_score:
            high_score_text = font.render("¡NUEVA PUNTUACIÓN ALTA!", True, NEON_GREEN)
            high_score_rect = high_score_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(high_score_text, high_score_rect)
            # Reproducir sonido de puntuación alta
            sound_manager.play_high_score()
        
        # Instrucciones
        restart_text = small_font.render("Presiona R para reiniciar", True, NEON_GREEN)
        restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 40))
        screen.blit(restart_text, restart_rect)
        
        high_scores_text = small_font.render("Presiona H para ver puntuaciones altas", True, NEON_CYAN)
        high_scores_rect = high_scores_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 70))
        screen.blit(high_scores_text, high_scores_rect)
        
        quit_text = small_font.render("Presiona Q para salir", True, NEON_ORANGE)
        quit_rect = quit_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))
        screen.blit(quit_text, quit_rect)
        
        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    high_scores = HighScores()
    sound_manager = SoundManager()
    effects = SynthwaveEffects(WIDTH, HEIGHT)
    
    # Mostrar menú principal
    show_main_menu(high_scores, effects)
    
    while True:
        score = game_loop(sound_manager, effects)
        
        # Verificar si es una puntuación alta
        if high_scores.is_high_score(score):
            # Pedir nombre del jugador
            player_name = get_player_name(effects)
            # Agregar la puntuación
            high_scores.add_score(player_name, score)
        
        # Mostrar pantalla de game over
        if not show_game_over_screen(score, high_scores, sound_manager):
            break
