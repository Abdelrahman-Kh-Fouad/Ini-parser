from IniParser.ParseIni import ParseIni
if __name__ == '__main__':
    x = ParseIni( """
    
    [general]
    appname = configparser
    version = 0.1
    
    [author]
    name = xmonader
    email = notxmonader@gmail.com
    
    
    """)
    x = x.iniResult
    x.DeleteProperty('general' , 'appname')
    x.SetSection('newSec')
    x.SetProperty('newSec' , ('salute' , 'saba7oo'))
    print(x)
