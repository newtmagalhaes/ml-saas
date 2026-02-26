from dataclasses import dataclass

@dataclass
class Question:
    id: int
    context: str
    objective: str
    about: str
