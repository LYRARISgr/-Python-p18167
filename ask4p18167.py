#!/usr/bin/python
#-*- coding: utf-8 -*-
print("Παρακαλώ δώστε την πράξη που επιθυμείται να γίνει,σε γράμματα της Αγγλικής στο τελος του προγράμματος με τη χρήση της εντολής print π.χ.:four(times(four())):")
def zero(*x):
    for g in x:
        return 0+g
    if True:
        return 0
def one(*x):
    for g in x:
        return 1+g
    if True:
        return 1
def two(*x):
    for g in x:
        return 2+g
    if True:
        return 2
def three(*x):
    for g in x:
        return 3+g
    if True:
        return 3
def four(*x):
    for g in x:
        return 4+g
    if True:
        return 4
def five(*x):
    for g in x:
        return 5+g
    if True:
        return 5
def six(*x):
    for g in x:
        return 6+g
    if True:
        return 6
def seven(*x):
    for g in x:
        return 7+g
    if True:
        return 7
def eight(*x):
    for g in x:
        return 8+g
    if True:
        return 8
def nine(*x):
    for g in x:
        return 9+g
    if True:
        return 9
def minus(k):
    return -k
def plus(k):
    return +k
def times(k):
    return k*k-k# Δουλευει μονο εαν ο αριθμός πολλαπλασιαστεί με τον ευατό του
print four(times(four()))
