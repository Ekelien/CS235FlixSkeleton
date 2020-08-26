from domainmodel.movie import Movie
from domainmodel.review import Review


class User:
    def __init__(self, name, password):
        self.user_name = name
        self.password = password
        self.watched_movies = []
        self.reviews = []
        self.time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self.__name

    @user_name.setter
    def user_name(self, other):
        if type(other) is str:
            self.__name = other.strip().lower()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, other):
        if type(other) is str:
            self.__password = other

    @property
    def watched_movies(self):
        return self.__watched_movies

    @watched_movies.setter
    def watched_movies(self, other):
        if type(other) is list and all((type(x) is Movie) for x in other):
            self.__watched_movies = other

    @property
    def reviews(self):
        return self.__reviews

    @watched_movies.setter
    def reviews(self, other):
        if type(other) is list and all((type(x) is Review) for x in other):
            self.__reviews = other

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, other):
        if other >= 0:
            self.__time_spent = other
            return

    def __repr__(self):
        return f"<User {self.user_name}>"

    def __eq__(self, other):
        if type(other) is User:
            return self.user_name == other.user_name
        return False

    def __lt__(self, other):
        if type(other) is User:
            return self.user_name < other.user_name

    def __hash__(self):
        return hash(self.user_name)

    def watch_movie(self, movie):
        if type(movie) is Movie:
            if movie not in self.watched_movies:
                self.watched_movies.append(movie)
            self.time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if type(review) is Review:
            self.reviews.append(review)


