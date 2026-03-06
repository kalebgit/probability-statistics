from sqlalchemy import create_engine
from config import settings
from sqlalchemy.orm import DeclarativeBase


# para despues cargar los modelso
class Base(DeclarativeBase):
    pass


engine = create_engine(
    url=settings.database_url,
    echo=True,
    # se puede agregar el pool_size y max_overflow
)
