import pygame
import os

class SoundManager:
    def __init__(self):
        """Inicializa el sistema de sonidos"""
        # Inicializar el mixer de pygame
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        
        # Diccionario para almacenar los sonidos
        self.sounds = {}
        
        # Cargar sonidos si existen
        self.load_sounds()
    
    def load_sounds(self):
        """Carga los archivos de sonido desde la carpeta sounds/"""
        sound_files = {
            'eat_food': 'eat.wav',
            'game_over': 'game_over.wav',
            'high_score': 'high_score.wav',
            'menu_select': 'menu_select.wav'
        }
        
        # Crear carpeta sounds si no existe
        if not os.path.exists('sounds'):
            os.makedirs('sounds')
            print("📁 Carpeta 'sounds' creada. Agrega archivos .wav para tener sonidos.")
        
        # Cargar cada sonido
        for sound_name, filename in sound_files.items():
            filepath = os.path.join('sounds', filename)
            if os.path.exists(filepath):
                try:
                    self.sounds[sound_name] = pygame.mixer.Sound(filepath)
                    print(f"✅ Sonido cargado: {sound_name}")
                except pygame.error as e:
                    print(f"❌ Error cargando {filename}: {e}")
            else:
                print(f"⚠️ Archivo no encontrado: {filepath}")
    
    def play_sound(self, sound_name, volume=0.5):
        """Reproduce un sonido específico"""
        if sound_name in self.sounds:
            try:
                # Configurar volumen (0.0 a 1.0)
                self.sounds[sound_name].set_volume(volume)
                # Reproducir el sonido
                self.sounds[sound_name].play()
            except pygame.error as e:
                print(f"❌ Error reproduciendo {sound_name}: {e}")
        else:
            print(f"⚠️ Sonido no encontrado: {sound_name}")
    
    def play_eat_food(self):
        """Reproduce el sonido de comer comida"""
        self.play_sound('eat_food', volume=0.3)
    
    def play_game_over(self):
        """Reproduce el sonido de game over"""
        self.play_sound('game_over', volume=0.4)
    
    def play_high_score(self):
        """Reproduce el sonido de puntuación alta"""
        self.play_sound('high_score', volume=0.5)
    
    def play_menu_select(self):
        """Reproduce el sonido de selección de menú"""
        self.play_sound('menu_select', volume=0.2)
    
    def create_default_sounds(self):
        """Crea sonidos básicos usando síntesis de audio"""
        print("🎵 Creando sonidos básicos...")
        
        # Sonido de comer comida (beep corto y agudo)
        eat_sound = self.generate_beep(frequency=800, duration=0.1)
        if eat_sound:
            pygame.mixer.Sound(eat_sound).play()
            pygame.mixer.Sound(eat_sound).stop()
        
        print("✅ Sonidos básicos creados")
    
    def generate_beep(self, frequency=440, duration=0.1, sample_rate=22050):
        """Genera un beep básico usando síntesis"""
        try:
            import numpy as np
            
            # Generar onda sinusoidal
            frames = int(duration * sample_rate)
            arr = np.zeros((frames, 2))
            
            for i in range(frames):
                # Crear onda sinusoidal con envolvente
                t = float(i) / sample_rate
                wave = np.sin(2 * np.pi * frequency * t)
                
                # Aplicar envolvente (fade in/out)
                envelope = 1.0
                if i < frames * 0.1:  # Fade in
                    envelope = i / (frames * 0.1)
                elif i > frames * 0.8:  # Fade out
                    envelope = (frames - i) / (frames * 0.2)
                
                wave *= envelope * 0.3  # Reducir volumen
                
                arr[i] = [wave, wave]
            
            # Convertir a formato de pygame
            arr = (arr * 32767).astype(np.int16)
            return arr
            
        except ImportError:
            print("⚠️ numpy no disponible para generar sonidos")
            return None
        except Exception as e:
            print(f"❌ Error generando beep: {e}")
            return None
