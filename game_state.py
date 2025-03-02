class GameState:
    def __init__(self):
        self.lives_left = 3
        self.current_score = 0

    def update_score(self, points):
        """Оновлює рахунок"""
        self.current_score += points