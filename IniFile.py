import re


class IniFile :
    def __init__(self , file:str):
        self.content:dict =  {}
        self.fileAsLines = file.splitlines()

        self.StoreInformation(0 , '')


    def StoreInformation(self, lineNumber:int , sectionName:str ):
        if lineNumber == len(self.fileAsLines):
            return
        line = self.fileAsLines[lineNumber]
        sectionInLine = re.search("\[(.*?)\]" , line)

        if sectionInLine != None:
            self.content[sectionInLine]={}
            self.StoreInformation(lineNumber +1 , sectionInLine)
        else :
            ind  = line.find('=')
            if ind  == -1 :
                self.StoreInformation(lineNumber +1 , sectionName)
            name = line[:ind]
            value = line[ind+1:]
            self.content[sectionName][name]=value
            self.StoreInformation(lineNumber+1 ,sectionName)

    def HasSection(self , section):
        try:
            self.content[section]
            return True
        except:
            return False

    def HasProperty(self,section , name):
        try :
            self.content[section][name]
            return True
        except:
            return False

    def sectionsCount(self):
        return len(self.content)

    def DeleteProperty(self , section , name ):
        if(self.HasProperty(section , name)):
            self.content[section].pop(name)
            return True
        else :
            return False

    def GetProperty(self , section ,name ):
        if self.HasProperty(section , name):
            return self.content[section][name]
        else:
            return None

    def GetSection(self , section):
        if self.HasSection(section):
            return self.content[section]
        else:
            return None

    def SetProperty(self ,section ,*property):
        if self.HasSection(section):
            self.content[section][property[0]] = property[1]
            return True
        else :
            False


    def ToIniString(self ):
        result:str =""
        for section in self.content.keys():
            str += f'[{section}]\n'
            for property in self.content[section].values():
                str += f'{property[0]}={property[1]}\n'
        return result




