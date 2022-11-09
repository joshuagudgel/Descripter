import movie_script as m

path = r"C:\Users\joshu\projects\Movie Scripts\knivesout-script.pdf"

knivesOutScript = m.MovieScript(path)
for castMember in knivesOutScript.cast:
    if castMember == 'WALT':
        print(knivesOutScript.dialogue[castMember])

f = open("knivesOutToText.txt","w+")
f.write(knivesOutScript.extractText())
f.close()