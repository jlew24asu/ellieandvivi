# games/spelling/ellie_spelling.py
import random
from typing import Tuple

class EllieSpelling:
    def __init__(self):
        # Age-appropriate sentences with missing words for 8-12 year olds
        self.challenges = [
            ("The _______ was listening to classical music.", "orchestra"),
            ("Scientists made an important _______ about climate change.", "discovery"),
            ("The brave _______ climbed the tallest mountain.", "adventurer"),
            ("Many animals face _______ as their habitats disappear.", "extinction"),
            ("The _______ experiment taught us about chemical reactions.", "fascinating"),
            # Add more age-appropriate sentences
        ]
        self.current_challenge = None
        self.reset_challenge()

    def reset_challenge(self) -> None:
        self.current_challenge = random.choice(self.challenges)

    def get_current_sentence(self) -> str:
        return self.current_challenge[0]

    def check_answer(self, answer: str) -> bool:
        return answer.lower().strip() == self.current_challenge[1].lower()

    def get_correct_word(self) -> str:
        return self.current_challenge[1]