import fitz
from pipe import select, where

pdf_document = "Certicamara.pdf"
document = fitz.open(pdf_document)
print("Total pages:", document.pageCount)
print("Metadata:", document.metadata)

print("________________________________________________")
print("------------- Loading a specific page-----------")
page = document.load_page(2)  # the first page is 0
text = page.get_text().encode("utf8")
print(str(text))

print("________________________________________________")
print("------------- Reading all pages ----------------")
for page in document:  # iterate the document pages
    text = page.get_text().encode("utf8")  # get plain text (is in UTF-8)
    print(text)

print("________________________________________________")
print("------------- Reading all words ----------------")
document_words = []
for page in document:  # iterate the document pages
    words_by_page = page.get_text("words")
    words_with_index = [(str(x[4]),  i) for i, x in enumerate(words_by_page, start=len(document_words))]
    document_words = document_words+words_with_index

print("Total words in the document: ", len(document_words))
for i, word in enumerate(document_words):
    print(word)
    if i == 4:
        break

print("________________________________________________")
print("------------- Searching a word ----------------")
word_to_search = "REPRESENTANTE"
r = list(document_words
         | where(lambda item: item[0] == word_to_search )
         | select(lambda item: (document_words[item[1]], document_words[item[1]+1], document_words[item[1]+2],document_words[item[1]+3], document_words[item[1]+4])))

for word in r:
    print(word)
