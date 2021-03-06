#!/usr/bin/env python3

def patternCount(inputString, pattern):
  count = 0
  patternLength = len(pattern)
  inputLength = len(inputString)
  for i in range(inputLength - patternLength):
    if inputString[i:i+patternLength] == pattern:
      count += 1
  return count

def main():
  inputString = "CTTGGCCTCTTGGCCGCTACTTGGCCCCTTGGCCCGCTTGGCCCTTGGCCACTTGGCCAAGTGCCAGCTTGGCCGCTGGCTCTTGGCCTCTTGGCCACCTTGGCCCTTGGCCTAGCTTGGCCGGCCCTTGGCCAACTGACACGCCTTGGCCCTTGGCCACTTGGCCCTTGGCCCTTGGCCTTCGATGACTCATTACCTTGGCCGAGTCTTGGCCGGGCTTGGCCGTTAACTTGGCCCTTGGCCATTGCTTGGCCTGACTTGGCCACTTGGCCCGCTTGGCCCTTGGCCGCTTGGCCCCCCCCTTGGCCACTTGGCCCCCTTGGCCCTTGGCCCTTGGCCGGACTTGGCCACCTTGGCCTCTCTTGGCCAGGTCTTGGCCATCTTGGCCCTTGGCCCTTGGCCAGACTGCATATGTCCTTGGCCGGTATCTTGGCCTACTTGGCCCGAGCCCTCTTGGCCCTTGGCCCTTGGCCATGTTGTCTTGGCCCAAGTTACGCGATCTGCTTGGCCCTTGGCCCCTCTTGGCCACTTGGCCACTTGGCCAGCTTGGCCGCCACCTTGGCCCGCTTGGCCTCGACTTACTTGGCCATCGCTTGGCCTGTACCTTGGCCAATCATGTCTTGGCCCTTGGCCGGACCTTGGCCTCTTGGCCATGCGCAACTTGGCCGCTTGGCCCTTGGCCCTTGGCCGACTTGGCCGCTTGGCCCCTCTTGGCCCGCTTGGCCGCACGACTTGGCCGCTTGGCCATTGATCTTGGCCTTTCTTGGCCACTTGGCCTACTTGGCCCTTGGCCTCTCTTGGCCCTACTTGGCCAACGCCCTTGGCCTCGAACTTGGCCCTTGGCCCTTGGCCCTGGTCTTGGCCTCTTGGCCCTCTTGGCCACTTGGCCTCACTTGGCCTGGCTTGGCCCTTGGCCGGGCTTGGCCGACTTGGCCCGCCATTTCTTGGCCTAATCCTTGGCCTCTTGGCCACAGACCTTGGCCGCTCTTGGCCCGCTTGGCCATGCTTGGCCCGCCTTGGCCACCTTGGCCGGACTTGGCC"
  pattern = "CTTGGCCCT"
  print(patternCount(inputString, pattern))

if __name__ == '__main__':
  main()