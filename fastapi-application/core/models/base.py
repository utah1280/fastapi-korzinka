from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped 
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import declared_attr
from sqlalchemy import DateTime, func

class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls):
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), nullable=False)
