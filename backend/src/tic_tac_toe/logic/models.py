# tic_tac_toe.logic.models.py

import enum
import re
from typing import Self

from dataclasses import dataclass
from functools import cached_property


class Mark(enum.StrEnum):
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> Self:
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT
    

@dataclass(frozen=True)
class Grid:
    cells: str = " "*9

    def __post_init__(self):
        if not re.match(r"^[ OX]{9}", self.cells):
            raise ValueError("Must contain 9 cells of: X, O or space")
        
    @cached_property
    def x_count(self) -> int:
        return self.cells.count('X')
    
    @cached_property
    def o_count(self) -> int:
        return self.cells.count('O')
    
    @cached_property
    def space_count(self) -> int:
        return self.cells.count(' ')
