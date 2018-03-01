import models as models


# TODO: models.Reddit()
# --- Config ---
trainingFileOut = "train.to"  # Output for bot
trainingFileIn = "train.from"  # Input for bot
dataFile = "OtakuOnsen - general.txt"
dataDirectory = "C:\\Users\\calin\\Desktop\\Subs\\"
modelType = models.Anime(dataDirectory)
# modelType = models.Discord(dataFile)
generateModel = False
modelOutput = "OOModel"
generateTrainingFiles = True

# -- Run --
# Load based on config
if generateModel or generateTrainingFiles:
    print("[Generating files]")
    print("|\t[Model type: " + str(modelType) + "]")
    print("|\t[Generate training files: " + str(generateTrainingFiles) + "]")
    print("|\t[Generate model: " + str(generateModel) + "]")
    # Load the data if it will be used
    # Generate training files if asked to
    if generateTrainingFiles:
        modelType.genTrainFiles(trainingFileIn, trainingFileOut)
    # Generate model if asked to
    if generateModel:
        modelType.genModel(modelOutput)
else:
    # Nothing to do, just exit
    print("[Nothing to do]")
# EXIT
print("[EXIT]")
