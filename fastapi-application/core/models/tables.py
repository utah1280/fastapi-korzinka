from .base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship

class Categories(Base):
    label: Mapped[str] = mapped_column(nullable=False, unique=True)

    contacts: Mapped["Contacts"] = relationship("Contacts", back_populates="category")

class Contacts(Base):
    name: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    address: Mapped[str] = mapped_column(nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    category: Mapped[Categories] = relationship("Categories", back_populates="contacts")