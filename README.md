# bookGenreCrawler
책 제목과 작가 정보를 받아 장르 태그를 보여줍니다.


![교보문고_결과](https://user-images.githubusercontent.com/8681323/149776162-27f181aa-5bb5-4cad-b9b4-cb50cb21ba3f.png)

교보문고 웹사이트에서 제공하는 책 태그를 크롤링해서 받아옵니다.

_교보문고 웹사이트 데이터를 이용하기 때문에, 장르가 검색되지 않는 책들도 있을 수 있습니다._



## 사용법

### 책 제목 직접 검색하기
1. bookGenreCrawler.py 를 실행하고,
2. `i` 를 입력합니다.
3. 책 제목과 작가를 입력하면 장르 태그를 보여줍니다.

### 책 리스트 csv로 일괄 검색하기
[books.csv](https://github.com/yerimpark103/bookGenreCrawler/files/7882112/books.csv)
1. 위의 템플렛의 Title / Author 부분에 책 제목과 작가를 넣어주세요! 
2. `books.csv`를 bookGenreCrawler 폴더에 넣습니다
3. bookGenreCrawler.py 를 실행하고,
4. `m`을 입력합니다.
5. 같은 폴더에 장르가 추가된 `books_with_genre.csv` 파일이 생성됩니다.
