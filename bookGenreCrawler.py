from bs4 import BeautifulSoup as bs
import urllib
import urllib.request
from csv import writer, reader


def genre_generator(keyword):
    if keyword == 'Title Author':
        return 'Genre'

    search_string = urllib.parse.quote(keyword).replace('%', '%25')

    url = 'https://search.kyobobook.co.kr/web/search?vPstrKeyWord=' + \
        search_string + '&orderClick=LAG'

    html = urllib.request.urlopen(url).read()

    soup = bs(html, 'html.parser')

    tags = soup.find(class_='tag')

    result = []

    if tags != None:
        print('Grabbing tags for ' + keyword)
        for tag in tags:
            result.append(tag.text.strip())

    result_sanitized = list(filter(None, result))
    return ' '.join(result_sanitized)


def multiple_book_csv_generator():
    with open('./books.csv', 'r') as read_obj, \
            open('books_with_genre.csv', 'w', newline='') as write_obj:
        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)
        line_count = 0
        for row in csv_reader:
            row.append(genre_generator(row[0] + ' ' + row[1]))
            csv_writer.writerow(row)


mode = input('Individual search (i) or Multiple CSV search? (m) : ')
if mode == 'i':
    keyword = input('Provide book title : ')
    print(genre_generator(keyword))
elif mode == 'm':
    multiple_book_csv_generator()
