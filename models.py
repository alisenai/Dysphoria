import io
import os
import re
import gensim

# TODO: Don't load all the data into memory

# -- Vars --
genModelSplit = "!.?,\n"
genTrainSplit = "\n"
# assCheckPattern = r"Dialogue: (([a-zA-Z]*=)|)([0-9]*(,|:|\.))*([a-zA-Z0-9_ \/{}\-@$%^&*()]*,(\*|)){0,2}([0-9a-z@ ]*(
# ,|:|\.))*({[\a-zA-Z0-9]*})*"


# Used to clean up lines and split them for use
def tidyUp(line, mode):
    tidyLine = ""
    if mode == 'train':
        tidyLine = line.translate(str.maketrans('', '', genTrainSplit)).split(" ")
    elif mode == 'model':
        tidyLine = line.translate(str.maketrans('', '', genModelSplit)).split(" ")
    return tidyLine


# -- Classes --
class Model:
    # Init for all models
    def __init__(self):
        self.sentences = []

    # Generates alternating inputs and responses
    def genTrainFiles(self, trainingFileIn, trainingFileOut):
        self.loadData('train')
        print("|\t[Generating training files]")
        print("|\t|\t[Saving input data to: " + trainingFileIn + "]")
        fromFile = io.open(trainingFileIn, "w", encoding="utf8")
        print("|\t|\t[Saving output data to: " + trainingFileOut + "]")
        toFile = io.open(trainingFileOut, "w", encoding="utf8")
        print("|\t|\t[Saving training data]")
        # Loop through and save data alternating between in / out
        for i in range(len(self.sentences)):
            # Join a all words in each word list within "sentences", adding spaces in between
            sentence = ("".join([(self.sentences[i][j] + " ") for j in range(len(self.sentences[i]))]))[:-1]
            if i % 2 == 0:
                fromFile.write(sentence + "\n")
            else:
                toFile.write(sentence + "\n")
        # Close io and finish
        fromFile.close()
        toFile.close()
        print("|\t[Done saving training data]")

    # Generates the Word2Vec model
    def genModel(self, modelOutput):
        self.loadData('model')
        print("|\t[Generating model]")
        # Generate Word2Vec model
        model = gensim.models.Word2Vec(self.sentences, workers=4, size=300, min_count=1)  # size=100 by default
        print("|\t|\t[Saving model as " + modelOutput + "]")
        # Save the Word2Vec model and finish
        model.save(modelOutput)
        print("|\t[Done saving model]")

    # Default load data -- Should never be called
    def loadData(self, mode):
        raise NotImplementedError("This model can't load data?")

    # Print default model info
    def __str__(self):
        return "Default Model"


# Discord Model
class Discord(Model):
    # -- Functions --
    def __init__(self, dataFile):
        super().__init__()
        self.dataFile = dataFile

    # Parses data and load it into memory
    def loadData(self, mode):
        self.sentences = []
        print("|\t[Loading data]")
        print("|\t|\t[Loading: " + self.dataFile + "]")
        print("|\t|\t[Loading mode: " + mode + "]")
        # Open data file provided by the config
        data = io.open(self.dataFile, encoding="utf8")
        parseNext = False
        currentIndex = 0
        for line in data:
            if parseNext:
                if line == "\n":
                    parseNext = False
                    currentIndex += 1
                    continue
                # Clean up the cluttered lines
                tidyLine = tidyUp(line, mode)
                if len(self.sentences) - 1 == currentIndex and currentIndex != 0:
                    self.sentences[currentIndex] = self.sentences[currentIndex] + tidyLine
                else:
                    self.sentences.append(tidyLine)
            else:
                parseNext = True
        # Close io and finish
        data.close()
        print("|\t[Done loading data]")

    # Returns the string from of this discord model
    def __str__(self):
        return "Discord Model"


# Anime Model
# TODO: Add more file compatibility (other than .srt & .ass)
class Anime(Model):
    # -- Vars --
    assCheckPattern = r"((Dialogue: )([\d\w_.:= !-]*,){9})"
    assCleanPatterns = assCheckPattern + "|" + r"(\{\\[^}]*\})" + "|" + r"(\\(N|n))"

    # -- Functions --
    def __init__(self, dataDirectory):
        super().__init__()
        self.dataDirectory = dataDirectory

    # TODO: Add mode for model generation
    # Parses data and load it into memory
    def loadData(self, mode):
        self.sentences = []
        # Create Regex patterns to check if file extension is .srt or .ass
        srtPatternComp = re.compile(r".*\.srt")
        assPatternComp = re.compile(r".*\.ass")
        # Create Regex pattern for .ass file parsing
        assCheckPatternComp = re.compile(self.assCheckPattern)
        assCleanPatternComp = re.compile(self.assCleanPatterns)
        # Load every file from given directory
        for filename in os.listdir(self.dataDirectory):
            # Open that each file, one by one
            subFile = open(self.dataDirectory + filename, encoding='latin-1')
            # Check if it's a .srt
            if srtPatternComp.match(filename):
                # If the file has a .srt extension
                skip = 2
                for line in subFile:
                    if skip == 0:
                        if line == '\n':
                            skip = 2
                        else:
                            # Append the useful lines, but tidy
                            self.sentences.append(tidyUp(line, mode))
                    else:
                        skip -= 1
                    continue
            # Check if it's a .ass
            elif assPatternComp.match(filename):
                # If the file has a .ass extension
                for line in subFile:
                    # Check if each line is useful for subtitle cleaning
                    if assCheckPatternComp.match(line):
                        # Clean up tidy it based on sentence building mode, and append it
                        self.sentences.append(tidyUp(assCleanPatternComp.sub('', line), mode))
            # Close file O/I when done parsing it
            subFile.close()

    # Returns the string from of this anime model
    def __str__(self):
        return "Anime Model"
