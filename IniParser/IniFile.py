class Ini :
    def __init__(self):
        self.content = {}


    def HasSection(self , section:str):
        '''Check if ini file has section.

            Arguments:
                section:string -- name of the section we check.

            Returns:
                bool -- if the section in ini file or not.
        '''

        try:
            self.content[section]
            return True
        except:
            return False

    def HasProperty(self, section:str , name:str):
        '''Check if ini file has property in a particular section.

            Arguments:
                section:string -- name of the section of Property.\n
                name:string -- name of the property we check.

            Returns:
                bool -- if the property in section or not.
        '''

        try :
            self.content[section][name]
            return True
        except:
            return False

    def sectionsCount(self)->int:
        '''Number of sections in ini file.

            Returns:
                Intger -- Number of sections.
        '''
        return len(self.content)

    def DeleteProperty(self , section:str , name:str ):
        '''Delete a property from a particular name.

            Arguments:
                section:string -- name of the section of Property.\n
                name:string -- name of the property you want to delete.

            Returns:
                bool -- if the property exist from the beginning or not.
        '''
        if(self.HasProperty(section , name)):
            self.content[section].pop(name)
            return True
        else :
            return False

    def GetProperty(self , section:str , name:str ):
        '''Get the value of property in particular section.

            Arguments:
                section:string -- name of the section of Property.\n
                name:string -- name of the property.

            Returns:
                string -- value.
        '''
        if self.HasProperty(section , name):
            return self.content[section][name]
        else:
            return None

    def GetSection(self , section:str )->list:
        '''Get lsit of properties in particular section.

            Arguments:
                section:string -- name of the section.

            Returns:
                list -- properties in section.
        '''
        if self.HasSection(section):
            return list(self.content[section])
        else:
            return None

    def SetSection(self , section):
        '''Add section to data.

            Arguments:
                section:string -- name of the section you want add.

        '''
        self.content[section]={}


    def SetProperty(self ,section:str ,property):
        '''Add property to particular section.

            Arguments:
                section:string -- name of the section of Property.\n
                property:tuple -- property you want to add.

            Returns:
                bool -- if section exist and added property successfully or not.
        '''

        if self.HasSection(section):
            #print(property[0] , property[1])
            self.content[section][property[0]] = property[1]
            return True
        else :
            False

    def __str__(self):
        return self.ToIniString()

    def ToIniString(self ):
        '''Convert data to string.

            Returns:
                string -- data.
        '''

        result:str =""
        for section in self.content.keys():
            result += f'[{section}]\n'
            for propertyName , propertyValue in self.content[section].items():
                result += f'{propertyName}={propertyValue}\n'
        return result




