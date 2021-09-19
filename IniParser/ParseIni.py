from IniParser.IniFile import Ini
class ParseIni:
    def __init__(self , file:str):
        self.fileAsLines = file.splitlines()
        self.iniResult = Ini()
        self.Parse(0, '')



    def Parse(self, lineNumber:int , sectionName:str ):
        '''Parsing ini file line by line.

            Arguments:
                lineNumber:intger -- line number we process in ini file.\n
                sectionName:string -- section name if the line we in included in section.

        '''

        if lineNumber == len(self.fileAsLines):
            return
        line = self.fileAsLines[lineNumber]
        line = line.strip()

        if line == '' or line.startswith(";") or line.startswith("#"):
            self.Parse(lineNumber +1 , sectionName)

        if line.startswith("[")  and line.endswith("]"):
            self.Parse(lineNumber +1 , self.ReadSection(line))

        if line.find('=')!=-1:
            ind  = line.find('=')
            if ind  == -1 :
                self.Parse(lineNumber +1 , sectionName)
            self.ReadProperty(line , sectionName)
            self.Parse(lineNumber+1 ,sectionName)

    def ReadSection(self , line:str ):
        '''
        Read Section name from line
        Arg:
            line:string -- line
        '''
        sectionInLine = line[1:len(line) - 1]
        self.iniResult.SetSection(sectionInLine)
        return sectionInLine


    def ReadProperty(self ,line:str , sectionName:str):
        '''
        Read Property from line.
        Argument:
            line:string -- line.
            sectionName:string -- particular section to add our property.

        '''
        ind = line.find('=')
        name = line[:ind].strip()
        value = line[ind + 1:].strip()

        self.iniResult.SetProperty(sectionName, (name, value))