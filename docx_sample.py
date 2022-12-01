import csv
import docx
import pandas as pd
import os
import re
from docx import Document

text_1 = ""
text_2 = ""
text_3 = ""
text_4 = ""
text_5 = ""

dict = {
        "症例No.":[],
        "出典":[],
        "症例":[],
        "主訴":[],
        "現病歴":[],
}

columns_name = ["症例No.", "出典", "症例", "主訴", "現病歴"]

df = pd.DataFrame(dict)
df.columns = columns_name

def from_docx_to_csv(docx_file):
    document = Document(docx_file)
    text = ""
    index_num = 0

    global text_1
    global text_2
    global text_3
    global text_4

    #テキスト抽出
    for i, p in enumerate(document.paragraphs):
        re.sub("\n", "", p.text) #delete_\n
        p.text = ''.join(p.text.split()) #delete_space
        p.text = p.text.replace('\uff5e', '')
        p.text = p.text.replace('\xe8', '')
        p.text = p.text.replace('\xe9', '')
        p.text = p.text.replace('\uff0d', '')
        p.text = p.text.replace('\uf02d', '')
        p.text = p.text.replace('\u525d', '')
        p.text = p.text.replace('\u6414', '')
        p.text = p.text.replace('\u2022', '')
        p.text = p.text.replace('\u9830', '')
        p.text = p.text.replace('\u2014', '')
        p.text = p.text.replace('\u9ad9', '')
        p.text = p.text.replace('\xab', '')
        p.text = p.text.replace('\xad', '')
        if "出典" in p.text:
            index_num += 1
            text_1 = p.text
        elif "症例" in p.text:
            text_2 = p.text
        elif "主訴" in p.text:
            text_3 = p.text
        elif "現病歴" in p.text:
            text_4 = p.text
            df.at[index_num] =[index_num, text_1, text_2, text_3, text_4]
        else:
            if p.text == '':
                text_1 == None
            elif p.text == '':
                text_2 == None
            elif p.text == '':
                text_3 == None
            elif p.text == '':
                text_4 == None
        text += p.text
        print(i, index_num, p.text)
    df.to_csv("sample_3.csv", index=False, encoding="shift-jis") #出力ファイル名を変更する

#実行関数
from_docx_to_csv("sample_3.docx") #入力するファイルを変更する