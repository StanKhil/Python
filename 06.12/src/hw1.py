from dataclasses import dataclass
from typing import List
import sqlite3


@dataclass
class Film:
    title: str
    genre: str
    director: str
    year: int
    duration: int
    studio: str
    actors: str


class FilmRepository:
    def __init__(self, db_path: str = "films.db") -> None:
        self.db_path = db_path
        self.__create_table()

    def __connect(self):
        return sqlite3.connect(self.db_path)

    def __create_table(self):
        conn = self.__connect()
        cur = conn.cursor()

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS films (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                genre TEXT NOT NULL,
                director TEXT NOT NULL,
                year INTEGER NOT NULL,
                duration INTEGER NOT NULL,
                studio TEXT,
                actors TEXT
            );
            """
        )

        conn.commit()
        conn.close()

    def add_film(self, film: Film) -> None:
        conn = self.__connect()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO films (title, genre, director, year, duration, studio, actors)
            VALUES (?, ?, ?, ?, ?, ?, ?);
            """,
            (
                film.title,
                film.genre,
                film.director,
                film.year,
                film.duration,
                film.studio,
                film.actors
            ),
        )

        conn.commit()
        conn.close()

    def get_films(self) -> List[Film]:
        conn = self.__connect()
        cur = conn.cursor()

        cur.execute(
            "SELECT title, genre, director, year, duration, studio, actors FROM films"
        )
        rows = cur.fetchall()
        conn.close()

        return [
            Film(
                title=row[0],
                genre=row[1],
                director=row[2],
                year=row[3],
                duration=row[4],
                studio=row[5],
                actors=row[6]
            )
            for row in rows
        ]

class FilmTemplate:
    @staticmethod
    def render_film(film: Film) -> str:
        return (
            "====================================\n"
            f"Name: {film.title}\n"
            f"Genre: {film.genre}\n"
            f"Director: {film.director}\n"
            f"Year: {film.year}\n"
            f"Duration: {film.duration} min\n"
            f"Studio: {film.studio}\n"
            f"Actors: {film.actors}\n"
            "===================================="
        )

    @staticmethod
    def render_list(films: List[Film]) -> str:
        return "\n\n".join(FilmTemplate.render_film(film) for film in films)



class View:
    def __init__(self, model: FilmRepository):
        self.model = model

    def show_menu(self):
        print("*" * 50)
        print(
            "1 - Add film\n"
            "2 - Show films\n"
            "3 - Exit\n"
        )
        print("*" * 50)

    def add_film(self):
        title = input("Enter film name: ")
        genre = input("Enter genre: ")
        director = input("Enter director: ")
        year = int(input("Enter year: "))
        duration = int(input("Duration (min): "))
        studio = input("Studio: ")
        actors = input("Actors (comma separated): ")

        film = Film(title, genre, director, year, duration, studio, actors)
        self.model.add_film(film)

    def show_films(self):
        films = self.model.get_films()
        output = FilmTemplate.render_list(films)
        print(output)


repo = FilmRepository()
view = View(repo)

while True:
    view.show_menu()
    choice = input("Choose: ")

    match choice:
        case "1":
            view.add_film()
        case "2":
            view.show_films()
        case "3":
            print("Bye!")
            break
        case _:
            print("Invalid choice!")
