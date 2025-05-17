def make_hangman(secret_word):
    guesses=[]
    def hangman_closure(guess):
        guesses.append(guess[0])
        out_list = []
        done = True
        for c in secret_word:
            if c in guesses:
                out_list.append(c)
            else:
                done = False
                out_list.append("_")
        print("".join(out_list))
        return done
    return hangman_closure

secret = input("What is the secret word? ")
hc = make_hangman(secret)
done = False
while not done:
    guess = input("What letter do you guess? ")
    done = hc(guess)
        