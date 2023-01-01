# https://www.geeksforgeeks.org/coroutine-in-python/


def Searcher():
    import time
    book = "This is book."
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("your text is present in book.")
        else:
            print("text isnt present in book")


search = Searcher()
next(search)
search.send("Talwinder")
input("Press any key")
search.send("is")