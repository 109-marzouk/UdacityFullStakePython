import urllib
def read_text():
    quotes = open(r"C:\Users\Mohamed Marzouk\Desktop\movie_quotes.txt")
    contents_of_file = quotes.read()
    print contents_of_file
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    if output == "true":
        print "Profanity Alert!!"
    elif output == "false":
        print "This document has no curse words."
    else:
        print "Unable to scan the document."
read_text()