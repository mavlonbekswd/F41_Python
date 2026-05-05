darslar = ["Matematika", "Fizika", "Ingliz", "Python"]

baholar = {
    "Matematika": 85,
    "Fizika": 90,
    "Ingliz": 78,
    "Python": 95
}
#import statistics
#convert = list(baholar.items())

#avg = statistics.mean(convert)
#print(avg)

avg = sum(baholar.values()) / len(baholar)

print(avg)

maxson = max(baholar)

minson = min(baholar, key=baholar.get)
print(minson)



for x in baholar:
    if baholar[x] < 80:

        print(x)

