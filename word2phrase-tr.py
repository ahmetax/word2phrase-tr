# -*- coding: utf-8 -*-
"""
Some small revisions are required for lowercase conversion of Turkish characters.
Also single quote characters are removed from the words.
Output written to a file.
Türkçe karakterlerin küçük harfe dönüşümü için küçük revizyonlar gerekiyor.
Ayrıca tek tırnak işaretleri de sözcüklerden temizlendi.
Sonuçlar bir dosyaya kaydedildi
Original code Author: Travis Brady 2015-10-18
Revision for Turkish: Ahmet Aksoy 20160715
"""
import word2phrase
from textblob import TextBlob

def read_sentences():
    book_txt = open('alice.txt',encoding="utf-8").read()
    """
    string.lower() can not convert Turkish 'İ' and 'I' characters correctly.
    So, we should change these characters prior to the lower() method application.
    string.lower() Türkçe İ ve I harflerini hatalı dönüştürüyor.
    O yüzden öncelikle bu harfleri kendimiz küçük harfe dönüştürüyoruz.
    """
    book_txt_lower = book_txt.replace('İ','i')
    book_txt_lower = book_txt_lower.replace('I','ı')
    book_txt_lower = book_txt_lower.lower()
    book_tb = TextBlob(book_txt_lower)
    return [s.words for s in book_tb.sentences if s]


def main():
    book_sentences = read_sentences()
    phrased1 = word2phrase.train_model(book_sentences, min_count=4)
    phrased2 = word2phrase.train_model(phrased1, min_count=4)
    new_text = ''
    for sentence in phrased2:
        for word in sentence:
            # Replace all single quotes with space
            # Tek tırnak işaretlerini boşluk ile değiştir
            word = word.replace("'"," ")
            new_text += word+' '
    ofile = open("alice-phrases","w",encoding="utf-8")
    print (new_text,file=ofile)
    ofile.close()


if __name__ == '__main__':
    main()
