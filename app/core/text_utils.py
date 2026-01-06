import re
from typing import List

_word = re.compile(r"[A-Za-z0-9_./-]+")

def tokenize(text: str) -> List[str]:
    # Keeps tokens like "S3", "PCI-DSS", "v1.2", "PAY-1234"
    return [t.lower() for t in _word.findall(text)]

def normalize_ws(s: str) -> str:
    return " ".join(s.split())
