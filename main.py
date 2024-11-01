def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        words = file_contents.split()
        wordnumber = len(words)

        #words is a list of all the words
        Char_count = {}
        

        for w in words:
            w_lower = w.lower()
            #print(list(w_lower))
            for letter in w_lower:
                if letter in Char_count:
                    Char_count[letter] +=1
                else:
                    Char_count[letter] = 1

        ## The if-else was needed to establish an initial value (?)

        #print(Char_count)

        Char_sorted = dict(sorted(Char_count.items(), key=lambda item: item[1], reverse=True))
        print(Char_sorted)

        ### TO UNDERSTAND/COMPARE WITH SOLUTION ON BOOTS:
        ### What is lambda and item[1] for?






        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{wordnumber} words found in the document")

        for k, v in Char_sorted.items():
            if str.isalpha(k)==True:
                print(f"The '{k}' letter was found {v} times")


        print("--- End report ---")

main ()