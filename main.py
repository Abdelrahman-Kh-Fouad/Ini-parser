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
    print(x.iniResult)
