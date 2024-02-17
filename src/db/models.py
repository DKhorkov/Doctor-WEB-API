from typing import AnyStr, List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True,  nullable=False, autoincrement=True)
    username: Mapped[AnyStr] = mapped_column(String(),  nullable=False, unique=True)

    files: Mapped[List["Files"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class Files(Base):
    __tablename__ = "files"
    id: Mapped[int] = mapped_column(primary_key=True,  nullable=False, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"),  nullable=False)
    filename: Mapped[AnyStr] = mapped_column(String(), nullable=False, unique=True)
    hashed_filename: Mapped[AnyStr] = mapped_column(String(), nullable=False, unique=True)
    filename_prefix: Mapped[AnyStr] = mapped_column(String(), nullable=False)
    full_hashed_filename: Mapped[AnyStr] = mapped_column(String(), nullable=False, unique=True)

    user: Mapped["Users"] = relationship(back_populates="files")
