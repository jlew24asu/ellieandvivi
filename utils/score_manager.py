# utils/score_manager.py
import json
from datetime import date
from pathlib import Path
from typing import Dict, Any

class ScoreManager:
    def __init__(self, player: str, game_type: str):
        self.player = player
        self.game_type = game_type
        self.save_file = Path(f"saves/{player}_{game_type}_scores.json")
        self.today = str(date.today())
        self._load_scores()

    def _load_scores(self):
        if self.save_file.exists():
            with open(self.save_file, 'r') as f:
                self.scores = json.load(f)
        else:
            self.scores = {
                'lifetime_score': 0,
                'best_day_score': 0,
                'best_day_date': '',
                'daily_scores': {}
            }
            self._save_scores()

    def _save_scores(self):
        with open(self.save_file, 'w') as f:
            json.dump(self.scores, f, indent=4)

    def add_points(self, points: int):
        # Update today's score
        if self.today not in self.scores['daily_scores']:
            self.scores['daily_scores'][self.today] = 0
        self.scores['daily_scores'][self.today] += points

        # Update lifetime score
        self.scores['lifetime_score'] += points

        # Update best day if necessary
        today_score = self.scores['daily_scores'][self.today]
        if today_score > self.scores['best_day_score']:
            self.scores['best_day_score'] = today_score
            self.scores['best_day_date'] = self.today

        self._save_scores()

    def get_today_score(self) -> int:
        return self.scores['daily_scores'].get(self.today, 0)

    def get_stats(self) -> Dict[str, Any]:
        return {
            'today_score': self.get_today_score(),
            'lifetime_score': self.scores['lifetime_score'],
            'best_day_score': self.scores['best_day_score'],
            'best_day_date': self.scores['best_day_date']
        }