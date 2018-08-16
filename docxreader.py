
from docx import Document
import os

dict = {}
for filename in os.listdir("documents"):
    if filename.endswith(".docx") :
        print("reading :" + filename)
        document = Document("documents/" + filename)

        docText = '\n\n'.join([
            paragraph.text for paragraph in document.paragraphs
        ])
        #print(docText)


        words = docText.split()
        for word in words:
            if (word in dict.keys()):
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1

        #for word in dict.keys():
           # print(word + ":" + "\n")
           #print(dict[word])

        k = 0
    else:
        continue

s = [(k, dict[k]) for k in sorted(dict, key=dict.get, reverse=True)]
for k, v in s:
    print(k, v)


