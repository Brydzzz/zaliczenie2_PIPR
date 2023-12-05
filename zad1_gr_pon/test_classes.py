from classes import Author, Article
from datetime import datetime


def test_create_author():
    author = Author(
        "John", "Smith", "John is a 70 year old bartender from Luton"
    )
    assert author.fname == "John"
    assert author.lname == "Smith"
    assert author.biography == "John is a 70 year old bartender from Luton"


def test_create_article():
    author1 = Author(
        "John", "Smith", "John is a 70 year old bartender from Luton"
    )
    author2 = Author(
        "Jack", "Smith", "Jack is a 50 year old taxi driver from Manchester"
    )
    content = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat."
    )
    date = datetime(2023, 12, 5, 11, 50, 11)
    article = Article("Lorem ipsum", content, "d", [author1, author2], date)
    assert article.title == "Lorem ipsum"
    assert article.content == content
    assert article.category == "d"
    assert article.authors == [author1, author2]
    assert article.date == date


def test_article_title_html():
    author1 = Author(
        "John", "Smith", "John is a 70 year old bartender from Luton"
    )
    author2 = Author(
        "Jack", "Smith", "Jack is a 50 year old taxi driver from Manchester"
    )
    content = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat."
    )
    date = datetime(2023, 12, 5, 11, 50, 11)
    article = Article("Lorem ipsum", content, "d", [author1, author2], date)
    assert article.title_html() == "<h1>Lorem ipsum</h1>"


def test_article_content_html():
    author1 = Author(
        "John", "Smith", "John is a 70 year old bartender from Luton"
    )
    author2 = Author(
        "Jack", "Smith", "Jack is a 50 year old taxi driver from Manchester"
    )
    content = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat."
    )
    date = datetime(2023, 12, 5, 11, 50, 11)
    article = Article("Lorem ipsum", content, "d", [author1, author2], date)
    assert article.content_html() == (
        "<p>"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat."
        "</p>"
    )


def test_article_category_html():
    author1 = Author(
        "John", "Smith", "John is a 70 year old bartender from Luton"
    )
    author2 = Author(
        "Jack", "Smith", "Jack is a 50 year old taxi driver from Manchester"
    )
    content = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat."
    )
    date = datetime(2023, 12, 5, 11, 50, 11)
    article = Article("Lorem ipsum", content, "d", [author1, author2], date)
    assert article.category_html() == "<p>drama</p>"


def test_article_authors_html():
    author1 = Author(
        "John", "Smith", "John is a 70 year old bartender from Luton"
    )
    author2 = Author(
        "Jack", "Smith", "Jack is a 50 year old taxi driver from Manchester"
    )
    content = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat."
    )
    date = datetime(2023, 12, 5, 11, 50, 11)
    article = Article("Lorem ipsum", content, "d", [author1, author2], date)
    assert article.authors_html() == (
        "<b>John Smith</b> <br/> "
        "John is a 70 year old bartender from Luton<br/>"
        "<b>Jack Smith</b> <br/> "
        "Jack is a 50 year old taxi driver from Manchester"
    )


def test_article_date_html():
    author1 = Author(
        "John", "Smith", "John is a 70 year old bartender from Luton"
    )
    author2 = Author(
        "Jack", "Smith", "Jack is a 50 year old taxi driver from Manchester"
    )
    content = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
        "nisi ut aliquip ex ea commodo consequat."
    )
    date = datetime(2023, 12, 5, 11, 50, 11)
    article = Article("Lorem ipsum", content, "d", [author1, author2], date)
    assert article.date_html() == "<h6>2023-12-05 11:50:11</h6>"
