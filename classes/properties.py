#!/usr/bin/python3

###
# Copyright 2014, Aurel Wildfellner.
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

import math


class Circle(object):

    def __init__(self, radius):

        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        if (r < 0):
            r *= -1
        self._radius = r

    @property
    def pi(self):
        return math.pi



def main():
    c = Circle(10)
    c.radius = -4
    c.pi
    # this fails
    #c.pi = 12
    print(c.radius)


if __name__ == "__main__":
    main()

