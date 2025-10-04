################################################################################
# ライブラリのインストール
################################################################################
from bs4 import BeautifulSoup
import requests as req
from wordcloud import WordCloud
from janome.tokenizer import Tokenizer
import matplotlib.pyplot as plt

################################################################################
# URLから本文を取得
################################################################################
# 青空文庫の目的の作品のXHTMLファイルのURLを指定（複数選択可能）
urls = ['https://www.aozora.gr.jp/cards/000148/files/773_14560.html']  # ①
htmls = []
soups = []
texts = []
for i in range(len(urls)):
    url = urls[i]
    htmls.append(req.get(url).content)
    html = htmls[i]
    soups.append(BeautifulSoup(html, 'html.parser'))
    soup = soups[i]
    # 青空文庫の目的の作品のXHTMLファイル本文の要素を選択
    texts.append(soup.find(class_='main_text').get_text())  # ②
text = ' '.join(texts)

################################################################################
# 本文を分割
################################################################################
t = Tokenizer()
tokens = t.tokenize(text)

words = []

for token in tokens:
    word = token.surface
    part_of_speech = token.part_of_speech.split(',')[0]
    part_of_speech2 = token.part_of_speech.split(',')[1]
    if part_of_speech == "形容詞":
        if(part_of_speech2 != "非自立") and (part_of_speech2 != "代名詞"):
            words.append(word)

word_list=" ".join(words)

################################################################################
# ワードクラウドを描画
################################################################################
wordcloud = WordCloud(
    font_path='C:\Windows\Fonts\meiryo.ttc',
    width=1000, height=500, 
    background_color="white",
).generate(word_list)

plt.figure(figsize=(100,50))
plt.imshow(wordcloud)
plt.axis("off")
# ワードクラウド画像を保存
plt.savefig("こころ.png", format="png", dpi=300)  # ③
plt.show()