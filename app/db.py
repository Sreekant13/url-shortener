import boto3
from botocore.config import Config
from .config import settings

_ddb = boto3.resource("dynamodb", config=Config(retries={'max_attempts': 10, 'mode': 'standard'}))
_table = _ddb.Table(settings.DDB_TABLE)

def get_url(code: str) -> str | None:
    resp = _table.get_item(Key={'code': code})
    item = resp.get('Item')
    return item.get('long_url') if item else None

def put_url(code: str, long_url: str) -> None:
    _table.put_item(Item={'code': code, 'long_url': long_url})

def code_exists(code: str) -> bool:
    return get_url(code) is not None
