import enum
import re
from typing import Self

from dataclasses import dataclass
from functools import cached_property

from tic_tac_toe.logic.validatiors import validate_grid, validate_game_state


WINNING_PATTERNS = (
    "???......",
    "...???...",
    "......???",
    "?...?...?",
    "..?.?.?..",
    "?..?..?..",
    ".?..?..?.",
    "..?..?..?",
)


class Mark(enum.StrEnum):
    CROSS = "X"
    NAUGHT = "O"

    @property
    def other(self) -> Self:
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT
    

@dataclass(frozen=True)
class Grid:
    cells: str = " "*9

    def __post_init__(self) -> None:
        validate_grid(self)
        
    @cached_property
    def x_count(self) -> int:
        return self.cells.count('X')
    
    @cached_property
    def o_count(self) -> int:
        return self.cells.count('O')
    
    @cached_property
    def space_count(self) -> int:
        return self.cells.count(' ')
    
@dataclass(frozen=True)
class Move:
    mark: Mark
    cell_index: int
    before_state: "GameState"
    after_state: "GameState"

@dataclass(frozen=True)
class GameState:
    grid: Grid
    starting_mark: Mark = Mark("X")

    def __post_init__(self) -> None:
        validate_game_state(self)

    @cached_property
    def current_mark(self) -> Mark:
        return self.starting_mark if self.grid.x_count == self.grid.o_count \
        else self.starting_mark.other
    
    @cached_property
    def game_not_started(self) -> bool:
        return self.grid.space_count == 9
    
    @cached_property
    def game_pver(self) -> bool:
        return self.winner is not None or self.tie
    
    @cached_property
    def tie(self) -> bool:
        return self.winner is None and self.space_count == 0
    
    @cached_property
    def winner(self) -> list[int]:
        for pattern in WINNING_PATTERNS:
            for mark in Mark:
                if re.match(pattern.replace('?', mark), self.grid.cells):
                    return [
                        match.start()
                        for match in re.finditer(r"\?", pattern)
                    ]
        return []
