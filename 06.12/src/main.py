from dataclasses import dataclass
from typing import List, Dict, Any
@dataclass
class Article:
    article_name: str
    author: str
    count_chars: int
    pubisher_name: str
    desc: str

class Articles_Repository:
    def __init__(self):
        self.articles = [
            Article("Python 2000", "Bill Gates", 567, "Microsoft", "Very nice"),
            Article("C++ 2020", "Tom Gates", 234, "Ubisoft", "Very interesting")
        ]

    def add_article(self, article: Article) -> None:
        self.articles.append(article)
    def get_articles(self) -> List[Article]:
        return self.articles
    

class View:
    def input_article(self) -> Article:
        a_n = input("Input article name: ")
        a = input("Input author name: ")
        ch = input("Input char count: ")
        p = input("Input publishe name: ")
        d = input("Input desc: ")
        return Article(a_n, a, int(ch), p, d)
    
    def show_articles(self, articles: List[Article]) -> None:
        for article in articles:
            print(
                f"{article}"
            )

    def show_menu(self) -> int:
        print("*"*50)
        print("1 - Add article\n" \
        "2 - Show articel\n" \
        "3 - Exit\n")
        result = int(input("Choose: "))
        print("*"*50)
        return result
    
class Controller:
    def __init__(self, model: Articles_Repository, view: View) -> None:
        self.model = model
        self.view = view
    
    def action_input_article(self):
        article = self.view.input_article()
        self.model.add_article(article)
    def action_show_articles(self):
        articles = self.model.get_articles()
        self.view.show_articles(articles)

obj_controller = Controller(Articles_Repository(), View())
while True:
    result = obj_controller.view.show_menu()
    match result:
        case 1:
            obj_controller.action_input_article()
        case 2:
            obj_controller.action_show_articles()
        case 3:
            print("Bye")
            break