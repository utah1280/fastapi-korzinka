from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base

class Categories(Base):
    label: Mapped[str] = mapped_column(unique=True, nullable=False)