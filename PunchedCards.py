def getData():
    with open("punched_cards_sample_ts1_input.txt") as infile:
        data = []
        rows = []
        cols = []
        for line in infile:
            if(len(line.split(" ")) > 1):
                numbers = line.strip("\n").split(" ")
                rows.append(int(numbers[0]))
                cols.append(int(numbers[1]))

            elif(len(line.split(" ")) == 1):
                t = int(line)

        return t, rows, cols

def printCard(card):
    for i in range(0, len(card)):
            for j in range(0, len(card[i])):
                print(card[i][j], end ="")
            print("\n", end ="")
    print("\n", end ="")


if __name__ == "__main__":
    t, r, c = getData()
    # outer loop iterates over all test cases
    for k in range(0,t):
        print(f"Case #{k+1}:")
        total_rows = 2*r[k] + 1
        total_cols = 2*c[k] + 1
        art = [[0 for i in range(total_cols)] for j in range(total_rows)]

        for i in range(0, total_rows):
            for j in range(0, total_cols):
                if (i in range(0,2) and j in range(0,2)):
                    for x in range(0, 2):
                        art[i][j] = '.'
                else:
                    if i % 2 == 0:
                        if j % 2 == 0:
                            art[i][j] = '+'
                        else:
                            art[i][j] = '-'
                    else:
                        if j % 2 == 0:
                            art[i][j] = '|'
                        else:
                            art[i][j] = '.'                    


        printCard(art)