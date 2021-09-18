from IniFile import Ini
class ParseIni:
    def __init__(self , file:str):
        self.fileAsLines = file.splitlines()
        self.iniResult = Ini()
        self.Parse(0, '')



    def Parse(self, lineNumber:int , sectionName:str ):
        if lineNumber == len(self.fileAsLines):
            return
        line = self.fileAsLines[lineNumber]

        if line.startsWith(';') or line.startsWith('#'):
            self.Parse(lineNumber +1 , sectionName)

        if line.startswith('[')  and line.endswith(']'):
            sectionInLine = line[1:len(line)-1]
            self.iniResult.SetSection(sectionInLine)

            self.Parse(lineNumber +1 , sectionInLine)

        if line.find('=')!=-1:
            ind  = line.find('=')
            if ind  == -1 :
                self.Parse(lineNumber +1 , sectionName)
            name = line[:ind]
            value = line[ind+1:]
            self.iniResult.SetProperty(sectionName , (name ,value))
            self.Parse(lineNumber+1 ,sectionName)
