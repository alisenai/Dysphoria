import io
import gensim

# --- Config ---
generateTrainingFiles = True
generateModel = False
dataFile = "OtakuOnsen - general.txt"  # Must be a generated file format ( See "OtakuOnsen - general.txt" for format )
trainingFileIn = "train.from"  # Input
trainingFileOut = "train.to"  # Output
modelOutput = "OOModel"

# --- Vars ---
sentences = []


def loadData():
    print("[Loading: " + dataFile + "]")
    # -- Open data file provided by the config
    data = io.open(dataFile, encoding="utf8")
    parseNext = False
    for i in data:
        if parseNext:
            if i == "\n":
                parseNext = False
                continue
            # -- Clean up the cluttered lines
            tidyLine = i.translate(str.maketrans('', '', "!.?,\n")).lower().split(" ")
            sentences.append([i for i in tidyLine])
        else:
            parseNext = True
    # -- Close io and finish --
    data.close()
    print("[Done loading data]")


def genTrainFiles():
    print("[Saving input data to: " + trainingFileIn + "]")
    fromFile = io.open(trainingFileIn, "w", encoding="utf8")
    print("[Saving output data to: " + trainingFileOut + "]")
    toFile = io.open(trainingFileOut, "w", encoding="utf8")
    # -- Loop through and save data alternating between in / out --
    for i in range(len(sentences)):
        sentence = ""
        for j in range(len(sentences[i])):
            sentence += sentences[i][j] + " "
        if i % 2 == 0:
            toFile.write(sentence + "\n")
        else:
            fromFile.write(sentence + "\n")
    # -- Close io and finish --
    fromFile.close()
    toFile.close()
    print("[Done saving training data]")


def genModel():
    print("[Generating model]")
    # -- Generate Word2Vec model --
    model = gensim.models.Word2Vec(sentences, workers=4, size=300, min_count=1)  # size=100 by default
    print("[Saving model as " + modelOutput + "]")
    # -- Save the Word2Vec model and finish --
    model.save(modelOutput)
    print("[Done saving model]")


# -- Load based on config --
if generateModel or generateTrainingFiles:
    print("[Generate training files: " + str(generateTrainingFiles) + "]")
    print("[Generate model: " + str(generateModel) + "]")
    # -- Load the data if it will be used
    loadData()
    # -- Generate training files if asked to --
    if generateTrainingFiles:
        genTrainFiles()
    # -- Generate model if asked to --
    if generateModel:
        genModel()
else:
    # -- Nothing to do, just exit --
    print("[Nothing to do]")
# -- EXIT ---
print("[EXIT]")
