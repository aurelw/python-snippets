#!/usr/bin/python

#
# Copyright 2015, Aurel Wildfellner.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#

import sys


def loadListFromFile(filename):
    """Loads text from a filename and returns a list of strings."""
    l = []

    #TODO use with statement for newer versions of python
    try:
        f = open(filename, 'r')
        while True:
            line = f.readline()
            if line == '':
                break
            l.append(line.strip('\n'))
    except IOError:
        #FIXME
        pass
    finally:
        f.close()

    return l




class TemplateMatcher:

    def __init__(self, template, landscape):
        self.template = template
        self.landscape = landscape
        pass


    def countTemplate(self):
        """Returns the number of occurrences of the template in the landscape."""
        positions = matchTemplate()
        return len(positions)


    def matchTemplate(self):
        """Matches the template to the landscape and returns a list of positions."""
        positions = []

        # if the template is larger than the landscape, there is no match.
        heightT = len(self.template)
        heightL = len(self.landscape)
        if (heightT > heightL):
            return positions

        # iterate over the landscape
        for y, row in enumerate(self.landscape[:-(heightT-1)]):
            for x, field in enumerate(row):
                # check the template
                def match():
                    for ty, trow in enumerate(self.template):
                        for tx, tfield in enumerate(trow):
                            # the template extends the border of the landscape
                            if (tx+x > len(row)-1):
                                return False
                            # a space matches to every field
                            if (tfield == " "):
                                continue
                            # mismatch of a field
                            if (tfield != self.landscape[y+ty][tx+x]):
                                return False
                    return True

                if (match()):
                    positions.append((x,y))

            # end for
        #end for

        return positions

                


def printUsage():
    """Prints the command line usage of the program."""
    print("find_bug <template> <landscape>")


def main():
    
    # handle command line options
    if (len(sys.argv) != 3):
        printUsage()
        exit(1)
    templateFile = sys.argv[1]
    landscapeFile = sys.argv[2]

    # load data
    template = loadListFromFile(templateFile)
    landscape = loadListFromFile(landscapeFile)
    if (template == [] or landscape == []):
        exit(1)

    tm = TemplateMatcher(template, landscape)

    


if __name__ == "__main__":
    main()
