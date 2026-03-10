import os
Folder = "Assets"
File = os.path.join(Folder, "Data.py")
Data = {}
try:
    from Assets.Data import Data as olddata
    Data = olddata
except (ImportError, SyntaxError):
        print("ERROR: THE DATA PYTHON FILE WAS MISSING FROM ITS ORIGINAL FOLDER, THIS FILE WON'T WORK WITHOUT IT")
Index = len(Data)
nDel = int(input("Input the Serial No. of the entry you want to delete - \n (Serial No. and other info can be found using search) \t: "))
VerQ = input(('Is', Data[nDel][2], 'the entry to delete?(Y/N): '))
Data1 = []
if VerQ == 'Y':
    Data.pop(nDel)
    y = 1
    for x in Data.values():
        Data1[y] = x
        y = y+1
    Data.clear()
print(Data)

#with open(File, "w") as f:
    #f.write(f"Data = {repr(Data)}")
