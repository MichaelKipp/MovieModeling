import timeit, sys, io

start_time = timeit.default_timer()

for filename in range(617):
    with open('SeparatedMovies/m' + str(filename) + '.txt', 'w') as movie:
        movie.write('')

with open('Data/movie_lines.txt') as data:
        for line in data:
            singleLine = line.split("+++$+++")
            with open('SeparatedMovies/' + singleLine[2].strip() + '.txt', 'a') as movie:
                movie.write(singleLine[4].strip() + '\n')

print ("Time taken: " + str(timeit.default_timer() - start_time))
