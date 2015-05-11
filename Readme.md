A python3 script to populate a file with british aliases for commands spelled in the american way, eg alias colourdiff=colordiff

How to use:
run the script

append 
if [ -f $HOME/.britbongaliases ]; then
  source $HOME/.britbongaliases
fi
to your .zshrc/.bashrc

source the shell rc file with source or by logging out and in again
