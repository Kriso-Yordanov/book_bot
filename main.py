import string


with open("github.com/Kriso-Yordanov/Book_bot/Books/frankenstein.txt") as f:
    file_contents = f.read()

def book_report():

    print("---Begin report of {f} ---s")
    print(f"{amount_words} words were found in the document")

    for i in d:
        print(f"The {i} character was found {d[i]} times")
        
    print("--- End of report ---")

d = dict.fromkeys(string.ascii_lowercase, 0)

words = file_contents.split()
file_lower = file_contents.lower()

for i in d:
    count = file_lower.count(i)
    d.update({i : count})
amount_words = (len(words))
book_report()