#!/usr/bin/env python3
"""Alta3 Researcg || Autuhor: RZFeeser@alta3.com"""


def main():
    """ Run-time code"""
    # create a small string
    lilstring = "alta3 Research offers classes on Python coding"
    newlist = lilstring.split(" ") # this returms a list
    print(newlist)


    # create a list of strings
    myiplist = ["192", "168", "0", "12"]
    # set singleip result of joining the list myiplist around
    singleip = ".".join(myiplist)
    # display singleip
    print(singleip)


# call our main function
main()
