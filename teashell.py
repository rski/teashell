#! /usr/bin/env python

import os
from os import listdir
from os.path import isfile, join
import re



def britbongise(executable):
    americlapExecutable = executable

    executable = re.sub("color", "colour", executable)
    executable = re.sub("theater", "theatre", executable)
    executable = re.sub("center", "centre", executable)
    if executable == americlapExecutable: #nothing to britbongise
        return None
    return [(executable, americlapExecutable)]


def write_to_britbong_alias_file(britbongAliasFile, britbongAliases):
    with open(britbongAliasFile, 'w') as f:
        for alias in britbongAliases:
            f.write("alias " + alias[1] + "=" + alias[0] + "\n")


if __name__=='__main__':
    ospath = os.environ['PATH']
    ospathlist = ospath.split(':')

    britbongAliasFile = join(os.environ['HOME'], ".britbongaliases")

    #print (ospathlist)

    executables = []
    for path in ospathlist:
        executables = executables + [f for f in listdir(path) if isfile(join(path,f)) ]
    #print (executables)

    britbongAliases = map(britbongise, executables)
    britbongAliases = [x for x in britbongAliases if x is not None]

    #write_to_britbong_alias_file(britbongAliasFile, britbongAliases)
    print (*britbongAliases)
