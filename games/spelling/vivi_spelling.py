# games/spelling/vivi_spelling.py

import random
from typing import Tuple


class ViviSpelling:
    def __init__(self):
        # Age-appropriate sentences with missing words for 6-8 year olds
        self.challenges = [
            ("The happy _______ jumped over the fence.", "rabbit"),
            ("I like to eat _______ and jelly sandwiches.", "peanut"),
            ("The _______ is shining brightly today.", "sun"),
            ("My favorite _______ is purple.", "color"),
            ("The _______ cat played with the yarn.", "little"),
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