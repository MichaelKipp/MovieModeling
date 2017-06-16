import timeit, sys, io

start_time = timeit.default_timer()

lines = [[] for x in range (670000)]
movies = {}

# Create movie lookup
with open('Data/movie_titles_metadata.txt') as movieList:
    for line in movieList:
        curLine = line.split('+++$+++')
        movies[str(curLine[0].strip())] = curLine[1].strip()

# SPLITS MOVIE LINES INTO INDIVIDUAL FILES
# Creates empty files for each movie
for filename in range(617):
    with open('LinesByMovie/' + movies['m' + str(filename)] + '.txt', 'a') as movie:
        movie.write('')

# Takes lines from data and adds to list
with open('Data/movie_lines.txt') as data:
        for line in data:
            singleLine = line.split("+++$+++")
            for i in range(len(singleLine)):
                singleLine[i] = singleLine[i].strip()
                singleLine[i] = singleLine[i].lower()
                lines[int(singleLine[0][1:])] = singleLine

lines = filter(None, lines)

currentMovie = 0

while currentMovie < 617:
    with open('LinesByMovie/' + movies['m' + str(currentMovie)] + '.txt', 'a') as movie:
        for line in lines:
            if int(line[2][1:]) == currentMovie:
                if currentMovie == 3:
                    movie.write(line[4] + '\n')
        currentMovie += 1


print ("Time taken: " + str(timeit.default_timer() - start_time))