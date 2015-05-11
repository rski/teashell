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
    return executable


def get_britbong_alias(executable):
    alias = britbongise(executable)
    if alias is None:
        return []
    return [(executable, alias)]


def write_to_britbong_alias_file(britbongAliasFile, britbongAliases):
    with open(britbongAliasFile, 'w') as f:
        for alias in britbongAliases:
            f.write("alias " + alias[0] + "=" + alias[1] + "\n")


if __name__=='__main__':
    ospath = os.environ['PATH']
    ospathlist = ospath.split(':')

    print ("DOWN WITH THE YANKS")
    britbongAliasFile = join(os.environ['HOME'], ".britbongaliases")

    #print (ospathlist)

    executables = []
    for path in ospathlist:
        executables = executables + [f for f in listdir(path) if isfile(join(path,f)) ]
    #print (executables)

    britbongAliases = []
    for executable in executables:
        britbongAliases = britbongAliases + get_britbong_alias(executable)

    write_to_britbong_alias_file(britbongAliasFile, britbongAliases)
    print (britbongAliases)
    print ("The yanks got what was coming to them")
