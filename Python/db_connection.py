from sqlalchemy import create_engine
from config import DB_CONFIG

def get_engine():
    engine = create_engine(
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}"
        f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )
    return engine