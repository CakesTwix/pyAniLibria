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
    full_string: Optional[str] = None
    code: int
    string: Any
    series: int
    length: Optional[str] = None


class Team(BaseModel):
    voice: List
    translator: List
    editing: List
    decor: List
    timing: List


class Season(BaseModel):
    season_string: Optional[str] = None
    season_code: int
    year: int
    week_day: int


class Blocked(BaseModel):
    blocked: bool
    bakanim: bool

class Hosts(BaseModel):
    hls: str

class Series(BaseModel):
    first: int
    last: int
    string: str

class Hls(BaseModel):
    fhd: Optional[str] = None
    hd: Optional[str] = None
    sd: str

class Playlist(BaseModel):
    id: int
    hls: Hls


class Player(BaseModel):
    alternative_player: Optional[str] = None
    hosts: Hosts
    series: Series
    playlist: dict

class Quality(BaseModel):
    string: str
    type: str
    resolution: int
    encoder: str
    lq_audio: bool

class List_(BaseModel):
    torrent_id: int
    series: Series
    quality: Quality
    leechers: int
    seeders: int
    downloads: int
    total_size: int
    url: str
    uploaded_timestamp: int
    metadata: Optional[int] = None
    raw_base64_file: Any

class Torrents(BaseModel):
    series: Series
    list: List[List_]
    

class Title(BaseModel):
    id: int
    names: Names
    announce: Any
    status: Status
    poster: Poster
    updated: Optional[int] = None
    last_change: int
    type: Type
    genres: List
    team: Team
    season: Season
    description: Optional[str] = None
    in_favorites: int
    blocked: Blocked
    player: Player
    torrents: Torrents