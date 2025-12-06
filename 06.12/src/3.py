from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
import sqlite3

@dataclass
class Article:
    article_name: str
    author: str
    count_chars: int
    publisher_name: str
    desc: str

class Articles_Repository:
    def __init__(self, db_path: str = "articles.db") -> None:
        self.db_path = db_path
        self.__create_table()
    def __connect(self):
        return sqlite3.connect(self.db_path)
    def __create_table(self):
        conn = self.__connect()
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                char_count INTEGER NOT NULL,
                publisher TEXT,
                desc TEXT
            );
            """
        )
        conn.commit()
        conn.close()
    
    def add_article(self, article: Article) -> None:
        conn = self.__connect()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO articles (title, author, char_count, publisher, desc)
            VALUES (?, ?, ?, ?, ?);
            """,
            (
                article.article_name,
                article.author,
                article.count_chars,
                article.publisher_name,
                article.desc,
            ),
        )
        conn.commit()
        conn.close()

    def get_articles(self) -> List[Article]:
        conn = self.__connect()
        cur = conn.cursor()
        cur.execute(
            "SELECT title, author, char_count, publisher, desc FROM articles"
        )
        rows = cur.fetchall()
        conn.close()

        return [
            Article(
                article_name=row[0],
                author=row[1],
                count_chars=row[2],
                publisher_name=row[3],
                desc=row[4]
            ) for row in rows
        ]

class ArticleTemplate(ABC):
    @abstractmethod
    def render(self, articles: List[Article]) -> str:
        pass

class ArticleTemplateTable(ArticleTemplate):
    def render(self, articles: List[Article]) -> str:
        result = "\n" + 110 * "-" + "\n"
        for article in articles:
            result += f"| {article.article_name:20} | {article.author:20} | {article.count_chars:6} | {article.publisher_name:15} | {article.desc:25} |\n"
        result  += "\n" + 110 * "-" + "\n"
        return result
    
class ArticleTemplateSimple(ArticleTemplate):
    def render(self, articles: List[Article]) -> str:
        result = ""
        for article in articles:
            result += f"{article.article_name} by {article.author}\n"
        result  += "\n"
        return result
    
class ArticleView:
    def __init__(self, model: Articles_Repository) -> None:
        self.model = model
    def render(self, template: ArticleTemplate) -> str:
        articles = self.model.get_articles()
        return template.render(articles)
    
def input_article() -> Article:
    a_n = input("Input article name: ")
    a = input("Input author name: ")
    ch = input("Input char count: ")
    p = input("Input publishe name: ")
    d = input("Input desc: ")
    return Article(a_n, a, int(ch), p, d)

def show_menu() -> int:
    print("*"*50)
    print("1 - Add article\n" \
    "2 - Show table\n" \
    "3 - Show similar\n" \
    "4 - Exit\n")
    result = int(input("Choose: "))
    print("*"*50)
    return result

obj_model = Articles_Repository()
obj_view = ArticleView(obj_model)
obj_table = ArticleTemplateTable()
obj_simple = ArticleTemplateSimple()

while True:
    result = show_menu()
    match result:
        case 1:
            obj_model.add_article(input_article())
        case 2:
            print(obj_view.render(obj_table))
        case 3:
            print(obj_view.render(obj_simple))
        case 4:
            print("Bye")
            break