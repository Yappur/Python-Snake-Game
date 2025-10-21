# 🐍 Snake Game - Synthwave Edition

Un juego clásico de Snake reinventado con efectos visuales synthwave y características modernas.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎮 Descripción

Snake Game Synthwave Edition es una versión moderna del clásico juego Snake con:
- **Efectos visuales synthwave** con gradientes dinámicos y luces pulsantes
- **Sistema de puntuaciones altas** con nombres de jugadores
- **Efectos de sonido** para una experiencia inmersiva
- **Estética retro-futurista** estilo años 80

## 🚀 Instalación

### Requisitos
- Python 3.7 o superior
- Pygame 2.0 o superior

### Pasos de instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/snake-game-synthwave.git
   cd snake-game-synthwave
   ```

2. **Instala las dependencias:**
   ```bash
   pip install pygame
   ```

3. **Ejecuta el juego:**
   ```bash
   python main.py
   ```

## 🎯 Controles

- **Flechas** - Mover la serpiente
- **ESPACIO** - Empezar juego (menú principal)
- **H** - Ver puntuaciones altas
- **R** - Reiniciar juego
- **Q** - Salir
- **ENTER** - Confirmar nombre (puntuación alta)

## ✨ Novedades y Características

### 🎨 Efectos Visuales Synthwave
- **Fondo dinámico** con gradientes animados
- **Rayos de luz rotatorios** desde el centro
- **Partículas flotantes** en colores neón
- **Líneas de escaneo CRT** para efecto retro
- **Efectos glow** en serpiente y comida

### 🏆 Sistema de Puntuaciones Altas
- **Top 3** mejores puntuaciones
- **Nombres de jugadores** personalizables
- **Guardado persistente** en archivo JSON
- **Detección automática** de nuevos records

### 🔊 Sistema de Sonidos
- **Sonidos de comer comida**
- **Sonidos de game over**
- **Sonidos de puntuación alta**
- **Sistema modular** fácil de extender

### 🎮 Mejoras de Juego
- **Serpiente con ojos** y efecto glow
- **Comida pulsante** con centro brillante
- **Explosiones de partículas** al comer
- **FPS optimizado** para efectos fluidos

## 📁 Estructura del Proyecto

```
snake-game-synthwave/
├── main.py                 # Juego principal
├── snake.py               # Lógica de la serpiente
├── food.py                # Lógica de la comida
├── synthwave_effects.py   # Sistema de efectos visuales
├── sounds.py              # Sistema de sonidos
├── highscores.py          # Sistema de puntuaciones
├── highscores.json        # Archivo de puntuaciones (se crea automáticamente)
└── sounds/                # Carpeta para archivos de sonido
    ├── eat.wav           # Sonido de comer comida
    ├── game_over.wav     # Sonido de game over
    ├── high_score.wav    # Sonido de puntuación alta
    └── menu_select.wav   # Sonido de menú
```

## 🎵 Agregar Sonidos Personalizados

Para agregar tus propios sonidos:

1. Coloca archivos `.wav` en la carpeta `sounds/`
2. Nómbralos exactamente como se indica en la estructura
3. El juego los cargará automáticamente

**Formatos soportados:** WAV (recomendado), OGG

## 🛠️ Personalización

### Cambiar Colores
Edita las constantes en `main.py`:
```python
NEON_GREEN = (0, 255, 127)    # Serpiente
NEON_PINK = (255, 20, 147)   # Comida
NEON_CYAN = (0, 255, 255)    # UI
```

### Ajustar Velocidad
Modifica `clock.tick(15)` en `main.py` para cambiar la velocidad del juego.

### Agregar Más Efectos
Extiende la clase `SynthwaveEffects` en `synthwave_effects.py`.

## 🐛 Solución de Problemas

### Error de pygame
```bash
pip install pygame
```

### Sin sonidos
- Verifica que los archivos estén en la carpeta `sounds/`
- Asegúrate de que los nombres sean exactos
- El juego funciona perfectamente sin sonidos

### Rendimiento lento
- Reduce el número de partículas en `synthwave_effects.py`
- Disminuye el FPS en `clock.tick(15)`

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📞 Contacto

Si tienes preguntas o sugerencias, no dudes en abrir un issue o contactarme.

---

**¡Disfruta jugando Snake con estilo synthwave!** 🐍✨
