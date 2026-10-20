# parser.py
def analyse_text(text):
    """ Takes a string of text and prints basic statistics. """
    words = text.split()
    total_words = len(words)
    unique_words = len(set(word.lower() for word in words))

    print ("--- Text Analysis Report ---")
    print (f"Total words: {total_words}")
    print (f"Unique words: {unique_words}")
    print ("-----------------------------")

if __name__ == "__main__":
    sample_text = (
        "In the beginning God created the heavens and the earth. "
        "Now the earth was formless and empty, darkness was over the surface of the deep, "
        "and the Spirit of God was hovering over the waters. "
        "And God said, 'Let there be light,' and there was light."
    )
    analyse_text(sample_text)
