from dataclasses import dataclass


@dataclass
class Endpoint:
    host: str
    port: int
