def main():
    data = read_file('./data.txt') # read the data from the file
    find_occurrences(data)
    find_totaltime(data)
    find_green_active(data)
    find_cycles(data)
    find_mistakes(data)


def read_file(file):
    data = []
    with open(file, 'r') as f:
        for line in f:
            data.append(line.split(","))
        data.pop(0) # remove the header
    print(f"Read {len(data)} points of data")
    return data


def find_occurrences(data):
    occurrences = {
        "red": 0,
        "yellow": 0,
        "green": 0
    }
    for row in data:
        if row[0] == "1": # using regular ifs as it is possible that multiple colors are on at the same time
            occurrences["red"] += 1
        if row[1] == "1":
            occurrences["yellow"] += 1
        if row[2] == "1":
            occurrences["green"] += 1
    
    print("Occurances of each color:")
    print(f"    Red: {occurrences['red']}")
    print(f"    Yellow: {occurrences['yellow']}")
    print(f"    Green: {occurrences['green']}")


def find_totaltime(data):
    total_times = {
    "red": 0,
    "yellow": 0,
    "green": 0
    }
    for row in data:
        if row[0] == "1":  # using regular ifs as it is possible that multiple colors are on at the same time
            total_times["red"] += int(row[3])
        if row[1] == "1":
            total_times["yellow"] += int(row[3])
        if row[2] == "1":
            total_times["green"] += int(row[3])
    
    print("Total time active for each color:")
    print(f"    Red: {total_times['red']}")
    print(f"    Yellow: {total_times['yellow']}")
    print(f"    Green: {total_times['green']}")


def find_green_active(data):
    green_active = []
    for row in data:
        if row[2] == "1":
            green_active.append(row[4])
    print("Green was active at (printing only the first 10 times):")
    for element in green_active[:10]:
        print("    "+element.strip())


def find_cycles(data): 
    cycles = 0
    for i in range(0, len(data)-4, 4): # assuming that the data does not have cycles that end in the middle of it. The increment by 4 is done for performance reasons.
        if data[i][0] == "1" and data[i+1][1] == "1" and data[i+2][2] == "1" and data[i+3][1] == "1" and data[i+4][0] == "1":
            #print(f"Cycle {cycles} starts at {data[i][4]} and ends at {data[i+4][4]}")
            cycles += 1

    print(f"Total cycles: {cycles}")


def find_mistakes(data):
    mistakes = 0
    for row in data: 
        active_count = int(row[0]) + int(row[1]) + int(row[2])
        if active_count != 1:
            mistakes += 1

    print(f"Total mistakes: {mistakes}")



if __name__ == "__main__":
    main()
