import bs4
import urllib.request

'''
Reads the top 100 movies of 2016 and puts the information into a csv file
'''


class Movie:
    def __init__(self, rank, title, studio, gross):
        self.rank = rank
        self.title = title
        self.studio = studio
        self.gross = gross

    def __str__(self):
        output = "rank: " + self.rank + "title: " + self.title + "studio: " + self.studio + "gross: " + self.gross
        return output

    def csv(self):
        output = self.rank + "," + self.title + "," + self.studio + "," + self.gross
        return output


def main():
    mojo_site = urllib.request.urlopen("http://www.boxofficemojo.com/yearly/chart/?yr=2016&p=.htm").read()
    mojo_soup = bs4.BeautifulSoup(mojo_site, 'html.parser')
    tables = mojo_soup.find_all('table', recursive=True)

    year_table = tables[6]
    table_rows = year_table.find_all('tr')
    # removes headers of table
    del table_rows[0:2]

    j = 0
    movie_info = ["", "", "", ""]
    movies = []

    # create an object for each of the 100 top movies
    for i in range(0, 100):

        for string in table_rows[i].strings:
            if j == 4:
                break
            string = string.replace(",", "")
            movie_info[j] = string
            j += 1

        rank = movie_info[0]
        name = movie_info[1]
        studio = movie_info[2]
        gross = movie_info[3]
        new_movie = Movie(rank, name, studio, gross)
        movies.append(new_movie)

        j = 0

    # Put data into csv file
    labels = "rank,title,studio,gross \n"
    with open('mojo_top_movies.csv', 'w') as csv_file:
        csv_file.write(labels)
        for movie in movies:
            csv_file.write(movie.csv())
            csv_file.write('\n')
if __name__ == '__main__':
    main()
