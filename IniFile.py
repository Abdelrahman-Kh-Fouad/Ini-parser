class Ini :
    def __init__(self):
        self.content = {}


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

    def SetSection(self , section):
        self.content[section]={}


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




