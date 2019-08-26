import nltk.data
import random

transitions = {"": {}}

def buildTransitions(input_file, num_words):
    nltk.download('punkt')
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    fp = open(input_file)
    data = fp.read()
    sentences = [sentence.replace('\n', ' ') for sentence in tokenizer.tokenize(data)]


    for sentence in sentences:
        words = sentence.split()
        if len(words) < num_words:
            continue
        
        idx = num_words - 1
        prev_words = ""
        while idx < len(words):

            # Increment value for next words
            cur_words = " ".join([words[idx] for idx in range(idx + 1 - num_words, idx + 1)]) 
            if cur_words not in transitions[prev_words].keys():
                transitions[prev_words][cur_words] = 0    
            transitions[prev_words][cur_words] += 1

            # Move to next word group
            idx += 1
            prev_words = cur_words
 
            # Find row for prev words
            if prev_words not in transitions.keys():
                transitions[prev_words] = {}       

        if "" not in transitions[prev_words].keys():
            transitions[prev_words][""] = 0
        transitions[prev_words][""] += 1

if __name__ == "__main__":
    buildTransitions(".\\2701-0.txt", 2)
    cur_words = random.choices(list(transitions[""].keys()), list(transitions[""].values()))[0]
    sentence = cur_words
    while True:
        next_words = random.choices(list(transitions[cur_words].keys()), list(transitions[cur_words].values()))[0]
        if next_words == "":
            print(sentence)
            exit()
        sentence += " " + next_words.split()[-1]
        cur_words = next_words