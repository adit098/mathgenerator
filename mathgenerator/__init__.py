import sys
import traceback
genList = []


class Generator:
    def __init__(self, title, id, generalProb, generalSol, func):
        self.title = title
        self.id = id
        self.generalProb = generalProb
        self.generalSol = generalSol
        self.func = func

        (filename, line_number, function_name, text) = traceback.extract_stack()[-2]
        funcname = filename[filename.rfind('/'):].strip()
        funcname = funcname[1:-3]
        # print(funcname)
        genList.append([id, title, self, funcname])

    def __str__(self):
        return str(
            self.id
        ) + " " + self.title + " " + self.generalProb + " " + self.generalSol

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


def getGenList():
    correctedList = genList[-1:] + genList[:-1]
    return correctedList
