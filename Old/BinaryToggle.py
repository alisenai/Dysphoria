import random


NNInput = []
NNOutput = []

for i in range(50):
    # num = "{0:b}".format(random.randint(0, 127)).zfill(7).replace("0", "a")
    # ans = num.replace("a", "b").replace("1", "a").replace("b", "1")
    # NNInput.append([int(num[i].replace("a", "-1")) for i in range(len(num))])
    # NNOutput.append([int(ans[i].replace("a", "-1")) for i in range(len(ans))])

    num = "{0:b}".format(random.randint(0, 127)).zfill(7)
    ans = num.replace("1", "a").replace("0", "1").replace("a", "0")
    NNInput.append([int(num[i]) for i in range(len(num))])
    NNOutput.append([int(ans[i]) for i in range(len(ans))])


print(NNInput)
print(NNOutput)
