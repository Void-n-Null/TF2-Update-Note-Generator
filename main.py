import markovify
with open("updateNotes.txt",'r',encoding="utf8") as f:
    text_model = markovify.Text(f.read())
    
if __name__ == '__main__':
    print(text_model.make_short_sentence(150))