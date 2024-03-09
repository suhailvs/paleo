import pandas as pd


def paleo_to_hebrew(paleo):
    # from word2word import Word2word # pip install word2word
    # he2en = Word2word('he','en')
    # print(he2en(hebrew_word))
    HLETTERS = [
        "\u05d0",
        "\u05d1",
        "\u05d2",
        "\u05d3",
        "\u05d4",
        "\u05d5",
        "\u05d6",
        "\u05d7",
        "\u05d8",
        "\u05d9",
        "\u05db",
        "\u05dc",
        "\u05de",
        "\u05e0",
        "\u05e1",
        "\u05e2",
        "\u05e4",
        "\u05e6",
        "\u05e7",
        "\u05e8",
        "\u05e9",
        "\u05ea",
    ]
    PLETTERS = "abgdefzhjiklmnxopsqrct"
    hebrew = ""
    for word in paleo.split(" "):
        hebrew_word = "".join([HLETTERS[PLETTERS.index(l)] for l in word])
        hebrew += f"{hebrew_word} "
    return hebrew[::-1]  # reverse it because hebrew is right to left


def get_verse(book, chapter, verse):
    df = pd.read_csv("torah.csv")
    df2 = pd.read_csv("trans.csv")
    trans = ""
    paleo = df[(df["b"] == book) & (df["c"] == chapter) & (df["v"] == verse)].iloc[0,3]
    print(paleo)
    print(paleo_to_hebrew(paleo))
    for word in paleo.split(" "):
        trans += f'{df2[df2["p"] == word].iloc[0,1]} '
    print(trans)


if __name__ == "__main__":
    get_verse(1, 1, 1)
