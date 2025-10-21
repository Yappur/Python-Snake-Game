import json
import os

class HighScores:
    def __init__(self, filename="highscores.json"):
        self.filename = filename
        self.scores = self.load_scores()
    
    def load_scores(self):
        """Carga las puntuaciones desde el archivo JSON"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        # Si no existe el archivo o hay error, retorna lista vacía
        return []
    
    def save_scores(self):
        """Guarda las puntuaciones en el archivo JSON"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.scores, file, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error al guardar puntuaciones: {e}")
    
    def add_score(self, name, score):
        """Añade una nueva puntuación y mantiene solo las 3 mejores"""
        self.scores.append({"name": name, "score": score})
        # Ordenar por puntuación descendente
        self.scores.sort(key=lambda x: x["score"], reverse=True)
        # Mantener solo las 3 mejores
        self.scores = self.scores[:3]
        self.save_scores()
    
    def is_high_score(self, score):
        """Verifica si la puntuación es suficientemente alta para estar en el top 3"""
        if len(self.scores) < 3:
            return True
        return score > self.scores[-1]["score"]
    
    def get_scores(self):
        """Retorna la lista de puntuaciones"""
        return self.scores
