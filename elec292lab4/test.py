

numbers = {
    "one": 1,
    "hundred": 100,
    "million": 1000000
}

string = "one hundred million"

sum = 1

for i in string.split():
    sum *= numbers[i]

print(sum)