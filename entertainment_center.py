import media
import fresh_tomatoes

""" Initialize all the movie objects that should be displayed
    in the movie listing page """
threeIdiots = media.Movie(
    "3 Idiots",
    "2009",
    "Two friends search for their long lost companion.",
    "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
    "https://www.youtube.com/watch?v=xvszmNXdM4w")
bobby = media.Movie(
    "Bobby",
    "1973",
    "The story is about the love between two Mumbai teenagers of different"
    "classes.",
    "https://upload.wikimedia.org/wikipedia/en/6/6c/Bobby_film_poster.jpg",
    "https://www.youtube.com/watch?v=DXvv6xokD6U")
ddlj = media.Movie(
    "Dilwale Dulhaniya Le Jayenge",
    "1995",
    "When Raj meets Simran in Europe, it isn't love at first sight but when "
    "Simran moves to India for an arranged marriage, love makes its presence "
    "felt.",
    "https://upload.wikimedia.org/wikipedia/en/8/80/Dilwale_Dulhania_Le_Jayenge_poster.jpg",    # NOQA
    "https://www.youtube.com/watch?v=c25GKl5VNeY")
hddcs = media.Movie(
    "Hum Dil De Chuke Sanam",
    "1999",
    "Nandini has to choose between Sameer, the man who taught her to fall in "
    "love; and Vanraj, the man from whom she learnt how to abide and fulfill "
    "promises of love.",
    "https://upload.wikimedia.org/wikipedia/en/a/a3/HDDCS.jpg",
    "https://www.youtube.com/watch?v=njs8UBO7qHc")
jjpk = media.Movie(
    "Jab Jab Phool Khile",
    "1965",
    "Raja, a Kashmiri boatman and Rita, a beautiful heiress from the city, "
    "fall in love.",
    "https://upload.wikimedia.org/wikipedia/en/8/8e/Jab_Jab_Phool_Khile_film_poster.jpg",   # NOQA
    "https://www.youtube.com/watch?v=1M0QOQ02dts")
loveStory = media.Movie(
    "1942: A Love Story",
    "1993",
    "A young Indian couple, both from wealthy backgrounds, find themselves "
    "caught up in the 1940's Indian revolutionary movement against their "
    "families whom are under the thumb a sadistic British general.",
    "https://upload.wikimedia.org/wikipedia/en/d/d8/1942_A_Love_Story_1994_film_poster.jpg",    # NOQA
    "https://www.youtube.com/watch?v=aDXubcMwqJo")
randDB = media.Movie(
    "Rang De Basanti",
    "2006",
    "This story is about six friends who help an English filmmaker "
    "create a documentary about Indian freedom struggle.",
    "https://upload.wikimedia.org/wikipedia/en/5/5f/RDB_poster.jpg",
    "https://www.youtube.com/watch?v=9U5gGXvJxO8")
kkkg = media.Movie(
    "Kabhi Khushi Kabhie Gham",
    "2001",
    "Rahul, the adopted son of business magnate Yash Raichand, "
    "feels eternal gratitude to his father for rescuing him from "
    "a life of poverty.",
    "https://upload.wikimedia.org/wikipedia/en/0/0d/KabhiKhushiKabhiGham_Poster.jpg",   # NOQA
    "https://www.youtube.com/watch?v=7uY1JbWZKPA&vl=en")
knph = media.Movie(
    "Kaho Naa... Pyaar Hai",
    "2000",
    "A young girl meets the doppelganger of her deceased boyfriend"
    " and now has a chance to find the people who have murdered him.",
    "https://upload.wikimedia.org/wikipedia/en/7/7e/KahoNaaPyaarHai.jpg",   # NOQA
    "https://www.youtube.com/watch?v=yQYN9YxCXSc")
devdas = media.Movie(
    "Devdas",
    "2002",
    "After his wealthy family prohibits him from marrying the woman "
    "he is in love with, Devdas Mukherjee's life spirals further and"
    " further out of control as he takes up alcohol and a life of "
    "vice to numb the pain.",
    "https://upload.wikimedia.org/wikipedia/en/6/6d/Devdas.jpg",
    "https://www.youtube.com/watch?v=8tuHQWGMQwY")
taareZP = media.Movie(
    "Taare Zameen Par",
    "2007",
    "An eight-year-old boy is thought to be a lazy trouble-maker,"
    "until the new art teacher has the patience and compassion to "
    "discover the real problem behind his struggles in school.",
    "https://upload.wikimedia.org/wikipedia/en/b/b4/Taare_Zameen_Par_Like_Stars_on_Earth_poster.png",   # NOQA
    "https://www.youtube.com/watch?v=tn_2Ie_jtX8")
sholay = media.Movie(
    "Sholay",
    "1975",
    "After his family is murdered by a notorious and ruthless bandit, "
    "a former police officer enlists the services of two outlaws to "
    "capture the bandit.",
    "https://upload.wikimedia.org/wikipedia/en/5/52/Sholay-poster.jpg",
    "https://www.youtube.com/watch?v=EwT6RdS-Nac")
dostana = media.Movie(
    "Dostana",
    "2008",
    "Two straight guys pretend to be gay in order to secure a Miami "
    "apartment.",
    "https://upload.wikimedia.org/wikipedia/en/1/16/Dostana%2C_2008_film_poster.jpg",   # NOQA
    "https://www.youtube.com/watch?v=gcEE4F-9qP8")
kkhh = media.Movie(
    "Kuch Kuch Hota Hai",
    "1998",
    "During their college years, Anjali was in love with her "
    "best-friend Rahul, but he had eyes only for Tina. Years later, "
    "Rahul and the now-deceased Tina's eight-year-old daughter attempts "
    "to reunite her father and Anjali.",
    "https://upload.wikimedia.org/wikipedia/en/0/07/Kuch_Kuch_Hota_Hai_poster.jpg",     # NOQA
    "https://www.youtube.com/watch?v=05i3eIuJLaU")
lagaan = media.Movie(
    "Lagaan",
    "2001",
    "The people of a small village in Victorian India stake their future "
    "on a game of cricket against their ruthless British rulers.",
    "https://upload.wikimedia.org/wikipedia/en/b/b6/Lagaan.jpg",
    "https://www.youtube.com/watch?v=oSIGQ0YkFxs")
lrmb = media.Movie(
    "Lage Raho Munna Bhai",
    "2006",
    "Munna Bhai embarks on a journey with Mahatma Gandhi in order to "
    "fight against a corrupt property dealer.",
    "https://upload.wikimedia.org/wikipedia/en/3/35/Lage_raho_munna_bhai.JPG",
    "https://www.youtube.com/watch?v=OE6f1oHgeDg")
mohabbatein = media.Movie(
    "Mohabbatein",
    "2000",
    "Two stubborn men with opposing beliefs battle each other - three love "
    "stories are at stake.",
    "https://upload.wikimedia.org/wikipedia/en/9/94/Mohabbatein.jpg",
    "https://www.youtube.com/watch?v=OjlZFIY7VHU")
taal = media.Movie(
    "Taal",
    "1999",
    "On a sight-seeing road trip of India, U.K. based Manav Mehta meets "
    "Mansi, the daughter of a singer, Tarababu.",
    "https://upload.wikimedia.org/wikipedia/en/8/83/Taal_film_poster.jpg",
    "https://www.youtube.com/watch?v=QrYruzg4iJY")
dilse = media.Movie(
    "Dil Se",
    "1998",
    "The clash between love and ideology is portrayed in this love story "
    "between a radio executive and a beautiful revolutionary.",
    "https://upload.wikimedia.org/wikipedia/en/7/7a/Dil_Se_poster.jpg",
    "https://www.youtube.com/watch?v=VLo60HGioAg")
mughalEAzam = media.Movie(
    "Mughal-E-Azam",
    "1960",
    "A 16th century prince falls in love with a court dancer and battles "
    "with his emperor father.",
    "https://upload.wikimedia.org/wikipedia/en/1/16/Mughal-e-Azam.jpg",
    "https://www.youtube.com/watch?v=rXz_vWzMh_U")
amarAkbarAnthony = media.Movie(
    "Amar Akbar Anthony",
    "1977",
    "Three brothers are separated and united after many years - one is "
    "brought up a Hindu, another a Muslim and the last a Christian.",
    "https://upload.wikimedia.org/wikipedia/en/0/09/Amar_Akbar_Anthony_1977_film_poster.jpg",   # NOQA
    "www.youtube.com/watch?v=Ee275ya4JMI")
myNameisKhan = media.Movie(
    "My Name Is Khan",
    "2010",
    "An Indian Muslim man with Asperger's syndrome takes a challenge to speak "
    "to the President seriously, and embarks on a cross-country journey.",
    "https://upload.wikimedia.org/wikipedia/en/5/5d/My_Name_Is_Khan_film_poster.jpg",   # NOQA
    "https://www.youtube.com/watch?v=_uNDm6YfN2k")
peepliLive = media.Movie(
    "Peepli Live",
    "2010",
    "An impoverished farmer's threat to end his life invites attention from "
    "politicians and media.",
    "https://upload.wikimedia.org/wikipedia/en/5/55/Peeplilive.jpg",
    "https://www.youtube.com/watch?v=ht0-gqvFor0")
qsqt = media.Movie(
    "Qayamat Se Qayamat Tak",
    "1988",
    "A young man and young woman fall in love against their feuding fathers' "
    "wishes in this version of 'Romeo and Juliet' set in contemporary India.",
    "https://upload.wikimedia.org/wikipedia/en/a/a7/Qayamat_Se_Qayamat_Tak1.jpg",   # NOQA
    "https://www.youtube.com/watch?v=_PBJxulzCas")
rnbj = media.Movie(
    "Rab Ne Bana Di Jodi",
    "2008",
    "A breathtaking, goose flesh igniting, awe inspiring love journey of an "
    "ordinary man Suri and his 'total opposite' love Taani.",
    "https://upload.wikimedia.org/wikipedia/en/a/ab/Rab_Ne_Bana_Di_Jodi.jpg",
    "https://www.youtube.com/watch?v=eBi8syxPd14")
chakDeIndia = media.Movie(
    "Chak De! India",
    "2007",
    "Kabir Khan is the coach of the Indian Women's National Hockey Team and "
    "his dream is to make his all girls team emerge victorious against all "
    "odds.",
    "https://upload.wikimedia.org/wikipedia/en/0/0c/Chak_De%21_India.jpg",
    "https://www.youtube.com/watch?v=6a0-dSMWm5g")
paa = media.Movie(
    "Paa",
    "2009",
    "A father tries to help his son cope with a rare condition that causes "
    "the young boy to age beyond his years.",
    "https://upload.wikimedia.org/wikipedia/en/1/17/Paaposter.jpg",
    "https://www.youtube.com/watch?v=mTjEWy4InQ4")


"""Add the movie objects initialized to the 'movies' list below."""
movies = [
    threeIdiots, bobby, ddlj, hddcs, jjpk, loveStory, randDB, kkkg, knph,
    devdas, taareZP, sholay, dostana, kkhh, lagaan, lrmb, mohabbatein, taal,
    dilse, mughalEAzam, amarAkbarAnthony, myNameisKhan, peepliLive, qsqt, rnbj,
    chakDeIndia, paa]
fresh_tomatoes.open_movies_page(movies)
