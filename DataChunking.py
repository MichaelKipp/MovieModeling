import timeit, sys, io

start_time = timeit.default_timer()

lines = [[] for x in range (670000)]
movies = {}
conjs = {}

# Create conjunction lookup
with open('conjunctions.csv') as conjunctions:
    for line in conjunctions:
        line = line.split(",")
        conjs[str(line[0])] = line[1].strip()

# Create movie lookup
with open('Data/movie_titles_metadata.txt') as movieList:
    for line in movieList:
        curLine = line.split('+++$+++')
        curLine[1] = curLine[1].strip()
        curLine[1] = curLine[1].replace(':', '')
        curLine[1] = curLine[1].replace('"', '')
        curLine[1] = curLine[1].replace('?', '')
        curLine[1] = curLine[1].replace('-', '')
        curLine[1] = curLine[1].replace(' ', '_')
        movies[str(curLine[0].strip())] = curLine[1]

# SPLITS MOVIE LINES INTO INDIVIDUAL FILES
# Creates empty files for each movie
for filename in range(617):
    if filename != 114:
        with open('LinesByMovie/' + movies['m' + str(filename)] + '.txt', 'w') as movie:
            movie.write('')

def handle_apostraphes(str):
    str = str.split(" ")
    for i in range(len(str)):
        if str[i] in conjs:
            str[i] = conjs[str[i]]
    return " ".join(str)

# Takes lines from data and adds to list
with open('Data/movie_lines.txt') as data:
        for line in data:
            singleLine = line.split("+++$+++")
            for i in range(len(singleLine)):
                singleLine[i] = singleLine[i].decode('utf-8', errors='ignore').encode('utf-8').strip()
                singleLine[i] = singleLine[i].lower()
                if "'" in singleLine[i]:
                    singleLine[i] = handle_apostraphes(singleLine[i])
                if "u>" in singleLine[i]:
                    singleLine[i] = singleLine[i].replace("<u>", "")
                    singleLine[i] = singleLine[i].replace("</u>", "")
            lines[int(singleLine[0][1:])] = singleLine

lines = filter(None, lines)

currentMovie = 0

while currentMovie < 617:
    if currentMovie != 114:
        with open('LinesByMovie/' + movies['m' + str(currentMovie)] + '.txt', 'a') as movie:
            for line in lines:
                if int(line[2][1:]) == currentMovie:
                    movie.write(line[4] + '\n')
    currentMovie += 1

print ("Time taken: " + str(timeit.default_timer() - start_time))
