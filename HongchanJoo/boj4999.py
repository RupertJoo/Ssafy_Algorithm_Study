def boj4999():
    jh = input()
    doc = input()
    len_jh = len(jh)
    len_doc = len(doc)
    if len_jh >= len_doc:
        print("go")
    else:
        print("no")


if __name__ == "__main__":
    boj4999()