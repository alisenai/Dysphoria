import re
# class Cat:
#     def __init__(self):
#         return
#
#     def something(self):
#         print("2")
#
#     def other(self):
#         print("1")
#         self.something()
#
#
# class Dog(Cat):
#     def __init__(self):
#         super().__init__()
#
#     def something(self):
#         print("3")
#
#     def other(self):
#         print("4")
#
#
# Dog().other()

# line = "asdfg897atrg43i5t$%RTSWETG[] ][.srt"
line = "Dialogue: 0,0:22:22.19,0:22:27.94,Song Subtitles,,0000,0000,0000,,You said, \"I never want to see your face again,\" when you left me"
# pattern = re.compile(r".*\.srt")
assPattern = r"Dialogue: ([0-9]*(,|:|\.))*(([a-zA-Z0-9_ \/])*,){0,2}([0-9]*(,|:|\.))*({[\a-zA-Z0-9]*})*"
if re.compile(assPattern).match(line):
    print(re.sub(assPattern, '', line))
