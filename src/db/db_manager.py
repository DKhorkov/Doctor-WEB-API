from typing import AnyStr, Optional, Type
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session, sessionmaker, Query

from .models import Base, Users, Files
from .exceptions import InvalidFileOwnerError
from ..configs import DATABASE_URL


class DBManager:

    def __init__(self) -> None:
        self.__engine: Engine = create_engine(
            url=DATABASE_URL,
            echo=False
        )

        self.__session_maker = sessionmaker(
            self.__engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False
        )

        self.__create_db_and_tables()

    def __create_db_and_tables(self) -> None:
        with self.__engine.begin() as conn:
            Base.metadata.create_all(conn)

    def __get_session(self) -> Session:
        """
            Creates Session instance, return it for use and closes after.
        """
        with self.__session_maker() as session:
            return session

    def save_user(self, username: AnyStr) -> Type[Users]:
        with self.__get_session() as session:
            query: Query = session.query(
                Users
            ).filter(
                Users.username == username
            )

            exists: bool = session.query(query.exists()).scalar()
            if not exists:
                user = Users(username=username)
                session.add(user)
                session.commit()
                session.refresh(user)
            else:
                user = query.one()

        return user

    def save_file(
            self,
            filename: AnyStr,
            hashed_filename: AnyStr,
            filename_prefix: AnyStr,
            full_hashed_filename: AnyStr,
            user: Type[Users]
    ) -> Type[Files]:

        with self.__get_session() as session:
            query: Query = session.query(
                Files
            ).filter(
                Files.hashed_filename == hashed_filename
            ).filter(
                Files.user_id == user.id
            )

            exists: bool = session.query(query.exists()).scalar()
            if not exists:
                file = Files(
                    filename=filename,
                    hashed_filename=hashed_filename,
                    filename_prefix=filename_prefix,
                    full_hashed_filename=full_hashed_filename,
                    user_id=user.id
                )
                session.add(file)
                session.commit()
                session.refresh(file)
            else:
                file = query.one()

        return file

    def select_file(self, hashed_filename: AnyStr) -> Optional[Type[Files]]:
        with self.__get_session() as session:
            query: Query = session.query(
                Files
            ).filter(
                Files.hashed_filename == hashed_filename
            )

            exists: bool = session.query(query.exists()).scalar()
            if exists:
                file = query.one()
                return file

    def delete_file(self, hashed_filename: AnyStr, user: Type[Users]) -> None:
        with self.__get_session() as session:
            query: Query = session.query(
                Files
            ).filter(
                Files.hashed_filename == hashed_filename
            ).filter(
                Files.user_id == user.id
            )

            exists: bool = session.query(query.exists()).scalar()
            if exists:
                query.delete()
                session.commit()
            else:
                raise InvalidFileOwnerError(f'{hashed_filename} does not belong to {user.username}!')

    def close_connection(self) -> None:
        self.__session_maker.close_all()
        self.__engine.dispose()

