import re


# TODO: Fix HAVING to have separate files
def removeLinks(fromFileInName, toFileInName, fromFileOutName, toFileOutName):
    filterByRegex(fromFileInName, toFileInName, fromFileOutName, toFileOutName,
                  "((http(s|):\/\/)(([a-zA-Z0-9-_:]*(\.|))*)((\/[a-zA-Z0-9-\._:%+#]*)*(\/|))(((\?|&|;)[\c]*=[a-zA-Z0-9-\._:%+#]*)|)*((\/[a-zA-Z0-9-\._:%+#]*)*(\/|)))")


def filterByRegex(fromFileInName, toFileInName, fromFileOutName, toFileOutName, regex):
    fromFileIn = open(fromFileInName, "r", encoding="utf8")
    toFileIn = open(toFileInName, "r", encoding="utf8")
    fromFileOut = open(fromFileOutName, "w+", encoding="utf8")
    toFileOut = open(toFileOutName, "w+", encoding="utf8")

    for fromLine in fromFileIn:
        toLine = toFileIn.readline()
        fromMatches = checkRe(regex, fromLine)
        toMatches = checkRe(regex, toLine)

        if len(fromMatches) == 0 and len(toMatches) == 0:
            fromFileOut.write(fromLine)
            toFileOut.write(toLine)


def checkRe(regex, line):
    matches = re.findall(regex, line)
    return matches


# removeLinks('TRAININGFROM.from', 'TRAININGTO.to', 'train.from', 'train.to')
