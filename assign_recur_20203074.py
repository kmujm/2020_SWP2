import time
import random


def seqsearch(nbrs, target):
    for i in range(0, len(nbrs)):
        if (target == nbrs[i]):
            return i
    return -1

def recbinsearch(L, l, u, target):
    if l > u:
        return -1
        
    mid = (l + u) // 2

    if (target == L[mid]):
        return mid
    elif (L[mid] > target):
        return recbinsearch(L, l, mid - 1, target)
    else:
        return recbinsearch(L, mid + 1, u, target)


numofnbrs = int(input("Enter a number: "))
numbers = []
for i in range(numofnbrs):
    numbers += [random.randint(0, 999999)]

numbers = sorted(numbers)

print(numbers)

numoftargets = int(input("Enter the number of targets: "))
targets = []
for i in range(numoftargets):
    targets += [random.randint(0, 999999)]

print(targets)


ts = time.time()

# binary search - recursive
cnt = 0
results = []
for target in targets:
    idx = recbinsearch(numbers, 0, len(numbers) - 1, target)
    if idx == -1:
        cnt += 1
    else:
        results.append(numbers[idx])
ts = time.time() - ts
print("\n>> recbinsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
print("recbinsearch found %d results :" %(numoftargets - cnt), results)

ts = time.time()

# sequential search
cnt = 0
results = []
for target in targets:
    idx = seqsearch(numbers, target)
    if idx == -1:
        cnt += 1
    else:
        results.append(numbers[idx])

ts = time.time() - ts
print("\n>> seqsearch %d: not found %d time %.6f" % (numoftargets, cnt, ts))
print("seqsearch found %d results : " %(numoftargets - cnt), results)
