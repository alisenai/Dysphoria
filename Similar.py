from difflib import SequenceMatcher
import io


# -- Config --
dataSet = "OOSnippet.txt"


# -- Return how similar two files are
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# -- Accept input until user exits --
while True:
    # -- Load data set --
    responseSet = io.open(dataSet, encoding="utf8")
    prompt = input("> ")
    bestResponse = ""
    # -- Loop through each line and find the most similar line --
    for line in responseSet:
        if similar(line.replace("\n", "").lower(), prompt) > similar(bestResponse, prompt):
            bestResponse = line.lower()
    # -- Close io --
    responseSet.close()
    # -- Print that line (NOT the next one / etc) --
    print(bestResponse)
