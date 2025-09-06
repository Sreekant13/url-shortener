import string, random, re

_ALPHABET = string.ascii_letters + string.digits

def gen_code(n: int = 7) -> str:
    return ''.join(random.choice(_ALPHABET) for _ in range(n))

_URL_RE = re.compile(r"^https?://", re.I)
def normalize_url(url: str) -> str:
    return url if _URL_RE.search(url) else f"https://{url}"
