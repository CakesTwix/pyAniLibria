from pydantic import BaseModel
from typing import Optional, Any, List


class Names(BaseModel):
    ru: str
    en: str
    alternative: Optional[str] = None


class Status(BaseModel):
    string: str
    code: int


class Poster(BaseModel):
    url: str
    updated_timestamp: int
    raw_base64_file: Any


class Type(BaseModel):
    full_string: str
    code: int
    string: Any
    series: int
    length: str


class Team(BaseModel):
    voice: List
    translator: List
    editing: List
    decor: List
    timing: List


class Season(BaseModel):
    season_string: str
    season_code: int
    year: int
    week_day: int


class Blocked(BaseModel):
    blocked: bool
    bakanim: bool


class Title(BaseModel):
    id: int
    names: Names
    announce: Any
    status: Status
    poster: Poster
    updated: int
    last_change: int
    type: Type
    genres: List
    team: Team
    season: Season
    description: str
    in_favorites: int
    blocked: Blocked
    # Доделай