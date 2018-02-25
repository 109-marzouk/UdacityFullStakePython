"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media

def main():
    MyLifeAsACourgette1 = media.Movie("My Life as a Courgette",
                          "After losing his mother, a young boy is sent to a foster home with other orphans his age where he begins to learn the meaning of trust and true love.",
                          "http://t3.gstatic.com/images?q=tbn:ANd9GcR8knLES7POmEl0MWOvNXMQ7yYBbrBew9w5dAXnksqOHt2nHX3y",
                          "https://www.youtube.com/watch?v=4d9N5Y_sN8Q",
                          "October 19, 2016")
    MyLifeAsACourgette2 = media.Movie("My Life as a Courgette",
                          "After losing his mother, a young boy is sent to a foster home with other orphans his age where he begins to learn the meaning of trust and true love.",
                          "http://t3.gstatic.com/images?q=tbn:ANd9GcR8knLES7POmEl0MWOvNXMQ7yYBbrBew9w5dAXnksqOHt2nHX3y",
                          "https://www.youtube.com/watch?v=4d9N5Y_sN8Q",
                          "October 19, 2016")
    MyLifeAsACourgette3 = media.Movie("My Life as a Courgette",
                          "After losing his mother, a young boy is sent to a foster home with other orphans his age where he begins to learn the meaning of trust and true love.",
                          "http://t3.gstatic.com/images?q=tbn:ANd9GcR8knLES7POmEl0MWOvNXMQ7yYBbrBew9w5dAXnksqOHt2nHX3y",
                          "https://www.youtube.com/watch?v=4d9N5Y_sN8Q",
                          "October 19, 2016")
    MyLifeAsACourgette4 = media.Movie("My Life as a Courgette",
                          "After losing his mother, a young boy is sent to a foster home with other orphans his age where he begins to learn the meaning of trust and true love.",
                          "http://t3.gstatic.com/images?q=tbn:ANd9GcR8knLES7POmEl0MWOvNXMQ7yYBbrBew9w5dAXnksqOHt2nHX3y",
                          "https://www.youtube.com/watch?v=4d9N5Y_sN8Q",
                          "October 19, 2016")
    MyLifeAsACourgette5 = media.Movie("My Life as a Courgette",
                          "After losing his mother, a young boy is sent to a foster home with other orphans his age where he begins to learn the meaning of trust and true love.",
                          "http://t3.gstatic.com/images?q=tbn:ANd9GcR8knLES7POmEl0MWOvNXMQ7yYBbrBew9w5dAXnksqOHt2nHX3y",
                          "https://www.youtube.com/watch?v=4d9N5Y_sN8Q",
                          "October 19, 2016")
    MyLifeAsACourgette6 = media.Movie("My Life as a Courgette",
                          "After losing his mother, a young boy is sent to a foster home with other orphans his age where he begins to learn the meaning of trust and true love.",
                          "http://t3.gstatic.com/images?q=tbn:ANd9GcR8knLES7POmEl0MWOvNXMQ7yYBbrBew9w5dAXnksqOHt2nHX3y",
                          "https://www.youtube.com/watch?v=4d9N5Y_sN8Q",
                          "October 19, 2016")
    movies = [MyLifeAsACourgette1, MyLifeAsACourgette2, MyLifeAsACourgette3, MyLifeAsACourgette4, MyLifeAsACourgette5, MyLifeAsACourgette6]

    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()