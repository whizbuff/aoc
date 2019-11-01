def part1(numbers):
    sum = 0
    for x in numbers:
        sum += int(x)
    print(sum)
    return sum

f = open("input.txt","r")
part1(f.readlines())