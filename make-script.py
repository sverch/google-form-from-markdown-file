#!/usr/bin/env python

import sys
import re

def generateTop(title):
    code ="function createForm() {\n"
    code+="  var title = \"%s\";\n" % title
    code+="  var form = FormApp.create(title)\n"
    code+="      .setTitle(title);\n"
    return code

def generateSection(title, choices):
    code = ""
    code = "%s\ntitle = \"%s\"" % (code, title)
    code = "%s\nchoices = %s" % (code, str(choices))
    code = "%s\nform.addCheckboxItem()" % code
    code = "%s\n    .setTitle(title)" % code
    code = "%s\n    .setChoiceValues(choices);" % code
    return code

def generateBottom():
    return "\n}"

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <markdown_file>")
        sys.exit(1)
    markdown = sys.argv[1]
    title = None
    choices = []
    with open(markdown) as f:
        for line in f.readlines():
            mainTitlePattern = re.compile("# (.*)")
            titlePattern = re.compile("## (.*)")
            choicePattern = re.compile("- (.*)")
            mainTitleMatch = mainTitlePattern.match(line)
            titleMatch = titlePattern.match(line)
            choiceMatch = choicePattern.match(line)
            if mainTitleMatch:
                print(generateTop(mainTitleMatch.group(1)))
            if titleMatch:
                if title:
                    print(generateSection(title, choices))
                title = titleMatch.group(1)
                choices = []
            if choiceMatch:
                choices.append(choiceMatch.group(1))
        print(generateSection(title, choices))
    print(generateBottom())
main()
