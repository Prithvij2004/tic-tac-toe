# tic_tac_toe.logic.models.py

import enum
from typing import Self

class Mark(enum.StrEnum):
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> Self:
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT

