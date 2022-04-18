 # INI-parser 
 ini parser and manipulator you can do:

- Add section, property in particular section.
- get section, property,
- delete any sections.

## Example 
`file.ini`:
```ini
[general]
appname = configparser
version = 0.1
[author]
name = xmonader
email = notxmonader@gmail.com

```
We can make some changes like:
```python
file = open('file.ini', 'r')
x = ParseIni(file.read())
x = x.iniResult
x.DeleteProperty('general' , 'appname')
x.SetSection('newSec')
x.SetProperty('newSec' , ('salute' , 'saba7oo'))
```
and file will be:
```ini
[general]
version=0.1
[author]
name=xmonader
email=notxmonader@gmail.com
[newSec]
salute=saba7oo
```