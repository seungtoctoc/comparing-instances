from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    import requests
    import time
    from bs4 import BeautifulSoup

    # 여러 웹사이트의 URL 리스트
    urls = ['https://github.com/koorukuroo',
            'https://github.com/godltjsdud',
            'https://github.com/sjun516',
            'https://github.com/gundolflee',
            'https://github.com/yeahh315',
            'https://github.com/Chaeniiiii',
            'https://github.com/Johyerin',
            'https://github.com/Woo-Shinyoung',
            'https://github.com/dbqudals',
            'https://github.com/kihyun1221',
            'https://github.com/seungtoctoc'
             ]

    result = ""
    start_time = time.time()

    for url in urls:
        # 각 웹사이트의 내용을 가져오기
        response = requests.get(url)

        # 가져온 내용을 BeautifulSoup을 사용하여 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # <article> 태그 찾기
        article_tag = soup.find('article')
        name = soup.find('div', class_="vcard-names-container float-left js-profile-editable-names col-12 py-3 js-sticky js-user-profile-sticky-fields")

        result += url + "<br>"

        if name.text:
            result += name.text + "<br>"

        if article_tag:
            result += article_tag.text
        result += "<br>--------------------------------------------------<br><br>"

    end_time = time.time()
    result += "t3a.large, x86_64<br>"
    result += "elapsed time : " + str(end_time - start_time)

    if result:
        return result

    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0')