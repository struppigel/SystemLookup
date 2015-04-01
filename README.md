## SystemLookup

Get results from SystemLookup.com via command line.

### Installation:

```
pip install systemlookup
```

### Usage:

```
usage: systemlookup.py [-h] [-l SL_LIST] -t SEARCHTYPE searchitem

SystemLookup.com Command Line Tool

positional arguments:
  searchitem

optional arguments:
  -h, --help            show this help message and exit
  -l SL_LIST, --list SL_LIST
                        The list that is used to lookup the entry. Possible
                        values: SEH, O16, FF, FIREFOX, O9, R3, O21, DRIVERS,
                        O10, STARTUP, O23, O20, O18, ACTIVE, CLSID, SERVICES,
                        O4, O3, O2, O22, LSP
  -t SEARCHTYPE, --type SEARCHTYPE
                        The type of the search item. Possible values: name,
                        clsid, filename
```

Example command for global search:

```
systemlookup -t name lsasss
```

Example command for search in startup list:

```
systemlookup --list O4 --type filename "explore.exe"
```
