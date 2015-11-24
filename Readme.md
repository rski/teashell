A python3 script to populate a file with british aliases for commands spelled in the american way, eg alias colourdiff=colordiff

How to use:
```
$ python3 teashell.py
```

append these lines to your shell config file: 
```
if [ -f $HOME/.britbongaliases ]; then
  source $HOME/.britbongaliases
fi
```

Source the shell config file or log out and in again.
