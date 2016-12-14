# This imports media module which has Movie class which is used further in this file. Also the fresh_tomatoes module
import media
import fresh_tomatoes

# Creating objects of movies with 4 arguments
Purano_dunga = media.Movie("Purano Dunga",
                      "Dramatical Story of Dayang Rai. A superb nepali \
                      two brother struggle movie", 
                      "http://www.eventscalendar.org.au/wp-content/uploads/2016/10/purano-portrait_858808.png",  # noqa
                      "https://www.youtube.com/watch?v=75zgt7e1Y4g")

resham_filili = media.Movie("Resham Filili",
                      "Superb Romanian comedy",
                      "http://thecinematimes.com/wp-content/uploads/2015/03/Resham-Filili-character-poster-release-3-thecinematimes.com_.jpg",  # noqa
                      "https://www.youtube.com/watch?v=pzev9CB3vuM")

ae_dil = media.Movie("Ae Dil Hai Mushkil",
                      "Matured Karan Johar Movie",
                      "http://timesofindia.indiatimes.com/img/54479240/Master.jpg",
                      "https://www.youtube.com/watch?v=CvPdtf8Ijj4")

befikre = media.Movie("Befikre",
                      "Kiss, Kiss,Kiss. I think that's all they have in this movie.",
                      "http://st1.bollywoodlife.com/wp-content/uploads/photos/ranveer-singh-and-vaani-kapoor-put-their-kissathon-to-rest-in-latest-still-of-befikre-201611-829698.jpg",  # noqa
                      "https://www.youtube.com/watch?v=p7X7mwcEJ-w")

movie_list = [Purano_dunga,resham_filili, ae_dil, befikre]
# calls fresh_tomatoes module to executes the movie_list 
fresh_tomatoes.open_movies_page(movie_list)
