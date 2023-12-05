from datetime import datetime


class Author:
    def __init__(self, fname: str, lname: str, biography: str):
        self._fname = fname
        self._lname = lname
        self._biography = biography

    @property
    def fname(self):
        return self._fname

    @property
    def lname(self):
        return self._lname

    @property
    def biography(self):
        return self._biography


categories = {"d": "drama", "t": "tech", "n": "news", "s": "sport"}


class Article:
    def __init__(
        self,
        title: str,
        content: str,
        category,
        authors: list[Author],
        date: datetime,
    ):
        self._title = title
        self._content = content
        self._category = category
        self._authors = authors
        self._date = date

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def category(self):
        return self._category

    @property
    def authors(self):
        return self._authors

    @property
    def date(self):
        return self._date

    def get_category(self):
        return categories.get(self.category)

    def title_html(self):
        return f"<h1>{self._title}</h1>"

    def content_html(self):
        return f"<p>{self._content}</p>"

    def category_html(self):
        return f"<p>{self.get_category()}</p>"

    def authors_html(self):
        authors_display = []
        for author in self._authors:
            fname = author.fname
            lname = author.lname
            biography = author.biography
            author_display = f"<b>{fname} {lname}</b> <br/> {biography}"
            authors_display.append(author_display)
        return "<br/>".join(authors_display)

    def date_html(self):
        return f"<h6>{str(self._date)}</h6>"

    def edit_content(self, new_content):
        self._content = new_content

    def change_date(self, new_date):
        if not isinstance(new_date, datetime):
            raise ValueError("New date has to be a datetime object")
        self._date = new_date

    def __lt__(self, other):
        return self.date < other.date

    def __str__(self):
        return f"{self.title}"
