import random


NNInput = []
NNOutput = []

for i in range(50):
    number1 = int(random.randint(0, 8))
    number2 = int(random.randint(0, 8))
    ans = "{0:b}".format(int(number1) * int(number2)).zfill(7)
    number1 = "{0:b}".format(int(number1)).zfill(7)
    number2 = "{0:b}".format(int(number2)).zfill(7)

    values = []
    for i in range(len(number1)):
        values.append(int(number1[i]))

    for j in range(len(number1)):
        values.append(int(number2[i]))

    answer = [int(ans[i]) for i in range(len(ans))]

    NNInput.append(values)
    NNOutput.append(answer)

print(NNInput)
print(NNOutput)
