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
nDel = int(input("Input the Serial No. of the entry you want to delete - \n (Index and other info can be found using search) \t: "))
VerQ = input(print("Is", Data[nDel][2],"the entry to delete?(Y/N)\t: ")).upper()
if VerQ == 'Y':
    Data.pop(nDel)
    for x in range(nDel, len(Data)+1):
        Data[x] = Data[x+1]
print(Data)
        
        
#with open(File, "w") as f:
    #f.write(f"Data = {repr(Data)}")
