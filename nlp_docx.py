import spacy
from spacy import displacy
import pandas as pd

def nlp_docx(self):
    nlp = spacy.load('ja_ginza')

    filename = "sample_2.csv"

    #テキスト読み込み
    df = pd.read_csv(filename, usecols=["現病歴"], encoding="shift-jis")
    # print(df)
    # print(len(df))
    # print(df["現病歴"][1])
    text = nlp(df["現病歴"][2])
    return text


# for i in len(df):
#     text = df[i]
#     doc = nlp(text)
#     displacy.render(doc, style="ent", jupyter=True)