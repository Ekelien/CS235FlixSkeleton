from domainmodel.movie import Movie
from domainmodel.director import Director
from domainmodel.actor import Actor
from domainmodel.genre import Genre
import csv
class MovieFileCSVReader:
    def __init__(self,filename):
        self.filename=filename
        self.dataset_of_movies=[]
        self.dataset_of_actors=[]
        self.dataset_of_directors=[]
        self.dataset_of_genres=[]

    def read_csv_file(self):
        csv_file=open(self.filename,encoding='utf-8')
        csv_reader=csv.DictReader(csv_file)
        ls=[]
        for row in csv_reader:
            temp=dict(row)

            movie=Movie(temp['Title'], temp['Year'])
            if movie not in self.dataset_of_movies:
                self.dataset_of_movies.append(movie)

            for i in temp['Actors'].split(","):
                actor=Actor(i.strip())
                if actor not in self.dataset_of_actors:
                    self.dataset_of_actors.append(actor)

            direct=Director(temp['Director'])
            if direct not in self.dataset_of_directors:
                self.dataset_of_directors.append(direct)

            for i in temp['Genre'].split(","):
                genre=Genre(i.strip())
                if genre not in self.dataset_of_genres:
                    self.dataset_of_genres.append(genre)

