import os

dataDirectory = "C:\\Users\\calin\\Desktop\\Subs\\"
match = "m 816 379 b 829 378 846 379 870 381 905 378 958 382 978 384 999 384 1015 382 1030 384 1029 395 1029 418 1027 439 1029 459 1025 494 1025 514 1025 522 1025 537 1026 545 991 542 947 544 906 544 868 542 831 543 815 543 811 518 815 506 811 476 812 450 814 414 814 396"

for filename in os.listdir(dataDirectory):
    # Open that each file, one by one
    subFile = open(dataDirectory + filename, encoding='latin-1')
    for line in subFile:
        if match in line:
            print(filename)