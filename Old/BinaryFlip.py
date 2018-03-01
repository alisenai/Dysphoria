import random


NNInput = []
NNOutput = []

for i in range(50):
    num = "{0:b}".format(random.randint(0, 127)).zfill(7)
    ans = num[::-1]
    NNInput.append([int(num[i]) for i in range(len(num))])
    NNOutput.append([int(ans[i]) for i in range(len(ans))])

print(NNInput)
print(NNOutput)
