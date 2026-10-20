import re


def slugify(text: str) -> str:
    cleaned = re.sub(r'[^a-zA-Z0-9]+', '-', text).strip('-')
    return cleaned.lower()
