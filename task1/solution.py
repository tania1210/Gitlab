import csv

k = []
ukraine = []
usa = []
paris = []
india = []
countUk = 0
countUSA = 0
countP = 0
countI = 0

with open("data.csv", "r", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        k = row
        i = 0
        if k[i] == 'Ukraine':
            ukraine.append(k[i+1])
            countUk += 1
        elif k[i] == "USA":
            usa.append(k[i+1])
            countUSA += 1
        elif k[i] == "Paris":
            paris.append(k[i+1])
            countP += 1
        elif k[i] == "India":
            india.append(k[+1])
            countI += 1
        i += 1

print("{\n  Ukraine: {\n", "  \"people\":" , ukraine, "\n   \"count\":", countUk, "\n }")
print("  USA: {\n", "  \"people\":", usa, "\n   \"count\":", countUSA, "\n }")
print("  Paris: {\n", "  \"people\":", paris, "\n   \"count\":", countP, "\n }")
print("  India: {\n", "  \"people\":", india, "\n   \"count\":", countI, "\n }")