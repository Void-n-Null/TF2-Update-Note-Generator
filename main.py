import markovify
with open("updateNotes.txt",'r',encoding="utf8") as f:
    text_model = markovify.Text(f.read())
    
