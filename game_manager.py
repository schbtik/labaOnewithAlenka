from game_state import GameState
from pacman import PacMan
from ghost import Ghost

class GameManager:
    def __init__(self, maze):
        self.pacman = PacMan(1, 1)
        self.ghosts = [Ghost(6, 5), Ghost(8, 5), Ghost(10, 5)]
        self.maze = maze
        self.game_state = GameState()
        self.game_over = False

    def update_game(self):
        """Оновлення гри після кожного кроку"""
        if self.game_over:
            return

        for ghost in self.ghosts:
            ghost.move(self.maze)

        # Перевірка зіткнення Pac-Man з привидами
        if any(g.x == self.pacman.x and g.y == self.pacman.y for g in self.ghosts):
            self.pacman.lives -= 1
            print(f"❌ Pac-Man з'їдений! Життів залишилось: {self.pacman.lives}")
            if self.pacman.lives <= 0:
                self.game_over = True
                print("❌ ГРА ЗАКІНЧЕНА! Pac-Man програв!")
                return

        # Перевірка перемоги
        if self.check_win_condition():
            self.game_over = True
            print("🎉 ВІТАЄМО! Pac-Man виграв!")

    def check_win_condition(self):
        """Перевіряє, чи всі точки зібрані"""
        for row in self.maze.grid:
            if '.' in row or 'O' in row:
                return False
        return True
