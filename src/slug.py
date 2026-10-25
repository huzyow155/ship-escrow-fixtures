def slugify(text: str) -> str:
    import re
    return re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
