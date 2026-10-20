import re

def slugify(text: str) -> str:
    return re.sub(r'[-\s]+', '-', re.sub(r'[^\w\s-]', '', text).strip().lower())

