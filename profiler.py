#!/usr/bin/env/python
"""Takes a plaintext representation of a NYTimes article and calculates the
corpora length and lexical diversity. Stores it with the article title."""

from __future__ import division
import nltk
import os

def lex_div(tokens):
    return len(set(tokens)) / len(tokens)

if __name__ == "__main__":
    pwd = os.getcwd()
    f = open(pwd+"/testfile","r")
    raw = f.read()
    tokens = nltk.word_tokenize(raw)
    print "Length of text: %f" % len(tokens)
    print "Lexical diversity (my def.): %f" % lex_div(tokens)
