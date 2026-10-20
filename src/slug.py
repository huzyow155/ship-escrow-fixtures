import re

def slugify(text: str) -> str:
    cleaned = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '-', cleaned)

