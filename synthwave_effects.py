import pygame
import math
import random
import numpy as np

class SynthwaveEffects:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.time = 0
        self.particles = []
        self.light_rays = []
        
        # Colores synthwave
        self.colors = {
            'background_dark': (10, 10, 30),
            'background_light': (20, 20, 50),
            'neon_pink': (255, 20, 147),
            'neon_cyan': (0, 255, 255),
            'neon_purple': (138, 43, 226),
            'neon_green': (0, 255, 127),
            'neon_orange': (255, 165, 0),
            'grid_color': (50, 50, 100),
            'glow': (100, 100, 200)
        }
        
        # Inicializar efectos
        self.init_particles()
        self.init_light_rays()
    
    def init_particles(self):
        """Inicializa partículas flotantes"""
        for _ in range(50):
            self.particles.append({
                'x': random.randint(0, self.width),
                'y': random.randint(0, self.height),
                'size': random.uniform(1, 3),
                'speed': random.uniform(0.5, 2),
                'color': random.choice([
                    self.colors['neon_pink'],
                    self.colors['neon_cyan'],
                    self.colors['neon_purple']
                ]),
                'alpha': random.randint(50, 200)
            })
    
    def init_light_rays(self):
        """Inicializa rayos de luz"""
        for _ in range(8):
            self.light_rays.append({
                'angle': random.uniform(0, 2 * math.pi),
                'length': random.uniform(100, 200),
                'speed': random.uniform(0.02, 0.05),
                'intensity': random.uniform(0.3, 0.8),
                'color': random.choice([
                    self.colors['neon_pink'],
                    self.colors['neon_cyan'],
                    self.colors['neon_purple']
                ])
            })
    
    def update(self, dt):
        """Actualiza todos los efectos"""
        self.time += dt
        
        # Actualizar partículas
        for particle in self.particles:
            particle['y'] -= particle['speed']
            particle['x'] += math.sin(self.time + particle['x'] * 0.01) * 0.5
            
            # Reaparecer partículas que salen de pantalla
            if particle['y'] < 0:
                particle['y'] = self.height
                particle['x'] = random.randint(0, self.width)
        
        # Actualizar rayos de luz
        for ray in self.light_rays:
            ray['angle'] += ray['speed']
            ray['intensity'] = 0.5 + 0.5 * math.sin(self.time * 2 + ray['angle'])
    
    def draw_background(self, screen):
        """Dibuja el fondo con gradiente dinámico"""
        # Crear superficie para el fondo
        bg_surface = pygame.Surface((self.width, self.height))
        
        # Gradiente base
        for y in range(self.height):
            # Gradiente vertical con variación temporal
            t = self.time * 0.5
            intensity = 0.3 + 0.2 * math.sin(t + y * 0.01)
            
            # Interpolación de colores
            r = int(10 + 10 * intensity)
            g = int(10 + 10 * intensity)
            b = int(30 + 20 * intensity)
            
            pygame.draw.line(bg_surface, (r, g, b), (0, y), (self.width, y))
        
        # Agregar líneas de grid dinámicas
        self.draw_grid(bg_surface)
        
        # Dibujar el fondo
        screen.blit(bg_surface, (0, 0))
    
    def draw_grid(self, surface):
        """Dibuja líneas de grid con efecto de profundidad"""
        grid_spacing = 40
        grid_color = self.colors['grid_color']
        
        # Líneas verticales
        for x in range(0, self.width, grid_spacing):
            # Efecto de profundidad
            alpha = int(50 + 30 * math.sin(self.time + x * 0.01))
            color = (*grid_color, alpha)
            
            # Crear superficie temporal para alpha
            temp_surface = pygame.Surface((2, self.height))
            temp_surface.set_alpha(alpha)
            temp_surface.fill(grid_color)
            surface.blit(temp_surface, (x, 0))
        
        # Líneas horizontales
        for y in range(0, self.height, grid_spacing):
            alpha = int(50 + 30 * math.sin(self.time + y * 0.01))
            color = (*grid_color, alpha)
            
            temp_surface = pygame.Surface((self.width, 2))
            temp_surface.set_alpha(alpha)
            temp_surface.fill(grid_color)
            surface.blit(temp_surface, (0, y))
    
    def draw_particles(self, screen):
        """Dibuja partículas flotantes"""
        for particle in self.particles:
            # Crear superficie con alpha
            particle_surface = pygame.Surface((int(particle['size'] * 2), int(particle['size'] * 2)))
            particle_surface.set_alpha(particle['alpha'])
            particle_surface.fill(particle['color'])
            
            # Dibujar con efecto de glow
            screen.blit(particle_surface, 
                       (particle['x'] - particle['size'], 
                        particle['y'] - particle['size']))
    
    def draw_light_rays(self, screen):
        """Dibuja rayos de luz desde el centro"""
        center_x = self.width // 2
        center_y = self.height // 2
        
        for ray in self.light_rays:
            # Calcular posición final del rayo
            end_x = center_x + ray['length'] * math.cos(ray['angle'])
            end_y = center_y + ray['length'] * math.sin(ray['angle'])
            
            # Crear gradiente de color
            steps = int(ray['length'] / 5)
            for i in range(steps):
                progress = i / steps
                alpha = int(ray['intensity'] * 255 * (1 - progress))
                
                if alpha > 0:
                    # Color con alpha
                    color = (*ray['color'], alpha)
                    
                    # Dibujar segmento del rayo
                    start_x = center_x + (ray['length'] * progress) * math.cos(ray['angle'])
                    start_y = center_y + (ray['length'] * progress) * math.sin(ray['angle'])
                    end_x = center_x + (ray['length'] * (progress + 1/steps)) * math.cos(ray['angle'])
                    end_y = center_y + (ray['length'] * (progress + 1/steps)) * math.sin(ray['angle'])
                    
                    # Crear superficie temporal para alpha
                    temp_surface = pygame.Surface((abs(end_x - start_x) + 1, abs(end_y - start_y) + 1))
                    temp_surface.set_alpha(alpha)
                    temp_surface.fill(ray['color'])
                    screen.blit(temp_surface, (min(start_x, end_x), min(start_y, end_y)))
    
    def draw_scanlines(self, screen):
        """Dibuja líneas de escaneo CRT"""
        scanline_surface = pygame.Surface((self.width, self.height))
        scanline_surface.set_alpha(30)
        
        for y in range(0, self.height, 4):
            pygame.draw.line(scanline_surface, (0, 255, 255), (0, y), (self.width, y))
        
        screen.blit(scanline_surface, (0, 0))
    
    def draw_all_effects(self, screen):
        """Dibuja todos los efectos visuales"""
        self.draw_background(screen)
        self.draw_particles(screen)
        self.draw_light_rays(screen)
        self.draw_scanlines(screen)
    
    def get_neon_color(self, base_color, intensity=1.0):
        """Obtiene color neon con efecto de brillo"""
        try:
            r, g, b = base_color
            glow_factor = 0.3 + 0.7 * math.sin(self.time * 3)
            
            # Asegurar que los valores sean enteros válidos entre 0 y 255
            new_r = max(0, min(255, int(r * intensity * glow_factor)))
            new_g = max(0, min(255, int(g * intensity * glow_factor)))
            new_b = max(0, min(255, int(b * intensity * glow_factor)))
            
            return (new_r, new_g, new_b)
        except (ValueError, TypeError):
            # Si hay error, devolver el color base
            return base_color
    
    def add_explosion_effect(self, x, y, color):
        """Agrega efecto de explosión en una posición"""
        for _ in range(10):
            self.particles.append({
                'x': x + random.randint(-20, 20),
                'y': y + random.randint(-20, 20),
                'size': random.uniform(2, 5),
                'speed': random.uniform(1, 3),
                'color': color,
                'alpha': 255
            })
