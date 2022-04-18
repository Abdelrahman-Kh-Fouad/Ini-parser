from turtle import pen
from IniParser.ParseIni import ParseIni
if __name__ == '__main__':
    file = open('file.ini', 'r')
    x = ParseIni(file.read())
    x = x.iniResult
    x.DeleteProperty('general' , 'appname')
    x.SetSection('newSec')
    x.SetProperty('newSec' , ('salute' , 'saba7oo'))
    print(x)
