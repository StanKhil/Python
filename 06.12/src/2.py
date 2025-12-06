from dataclasses import dataclass
from typing import List

@dataclass
class Actor:
    fullname: str
    role: str


@dataclass
class Film:
    title: str
    genre: str
    director: str
    year: int
    duration: int
    studio: str
    actors: List[Actor]


class FilmRepository:
    def __init__(self):
        self.films = [
            Film(
                "Inception",
                "Sci-Fi",
                "Christopher Nolan",
                2010,
                148,
                "Warner Bros",
                [
                    Actor("Leonardo DiCaprio", "Cobb"),
                    Actor("Joseph Gordon-Levitt", "Arthur")
                ]
            )
        ]

    def add_film(self, film: Film) -> None:
        self.films.append(film)

    def get_films(self) -> List[Film]:
        return self.films


class View:
    def input_actor(self) -> Actor:
        name = input("Enter actor name: ")
        role = input("Enter actor role: ")
        return Actor(name, role)

    def input_film(self) -> Film:
        title = input("Enter film name: ")
        genre = input("Enter genre: ")
        director = input("Enter director: ")
        year = int(input("Enter year: "))
        duration = int(input("Duration: "))
        studio = input("studio: ")

        actors = []
        print("Adding actors (0 – exit)")
        while True:
            add = input("Add actor? (1 – yes, 0 – no): ")
            if add == "0":
                break
            actors.append(self.input_actor())

        return Film(title, genre, director, year, duration, studio, actors)

    def show_films(self, films: List[Film]) -> None:
        for film in films:
            print("=" * 40)
            print(f"Name: {film.title}")
            print(f"Genre: {film.genre}")
            print(f"Ditrctor: {film.director}")
            print(f"Year: {film.year}")
            print(f"Duration: {film.duration} хв")
            print(f"Studio: {film.studio}")
            print("Actors:")
            for actor in film.actors:
                print(f"   {actor.fullname} — {actor.role}")
            print("=" * 40)

    def show_menu(self) -> int:
        print("*" * 50)
        print(
            "1 - Add film\n"
            "2 - show films\n"
            "3 - Exit\n"
        )
        result = int(input("Choose: "))
        print("*" * 50)
        return result


class Controller:
    def __init__(self, model: FilmRepository, view: View):
        self.model = model
        self.view = view

    def action_add_film(self):
        film = self.view.input_film()
        self.model.add_film(film)

    def action_show_films(self):
        films = self.model.get_films()
        self.view.show_films(films)


obj_controller = Controller(FilmRepository(), View())

while True:
    result = obj_controller.view.show_menu()

    match result:
        case 1:
            obj_controller.action_add_film()
        case 2:
            obj_controller.action_show_films()
        case 3:
            print("Bye!")
            break
        case _:
            print("Invalid input!")
