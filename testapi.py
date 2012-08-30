__author__ = 'thomas'

from pycaffeine import CafDeque

cd = CafDeque()
print cd.is_empty()
print cd.length()
print cd.pop()

print cd.push("one")
print cd.push("two")
print cd.push("three")

print cd.is_empty()
print cd.length()

print cd.pop()
print cd.pop()
print cd.pop()

print cd.is_empty()
print cd.length()

print cd.pop()

print cd.is_empty()
print cd.length()

print cd.pop()

print cd.is_empty()
print cd.length()