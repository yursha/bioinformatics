def find(sequence, pattern):
    """
  Returns a list of positions where `patterns` is found in `sequence`.
  """
    positions = []
    for i in range(len(sequence) - len(pattern) + 1):
        if pattern == sequence[i : i + len(pattern)]:
            positions.append(i)
    return positions


def complement(sequence):
    reverse = ""
    for c in sequence:
        if c == "A":
            reverse += "T"
        elif c == "T":
            reverse += "A"
        elif c == "G":
            reverse += "C"
        elif c == "C":
            reverse += "G"
        else:
            raise Error("Unsupported sequence character")
    return reverse


def reverse_complement(sequence):
    return complement(sequence)[::-1]


def FrequentWords(Text, k):
    """
    Finds the most frequent k-mers in a string.

    Input:
      A string Text and an integer k.
    Output:
      All most frequent k-mers in Text.

    Sample input:
      ACGTTGCATGTCGCATGATGCATGAGAGCT
      4
    Sample output:
      CATG GCAT
    """
    freqMap = {}
    max = 0
    for i in range(len(Text) - k + 1):
        pattern = Text[i : i + k]
        count = freqMap[pattern] if pattern in freqMap else 0
        count += 1
        if count > max:
            max = count
        freqMap[pattern] = count

    return [pattern for pattern in freqMap if freqMap[pattern] == max]


def PatternCount(Text, Pattern):
    """
    Computes the number of times that a k-mer Pattern appears as a substring of Text.

    Sample Input:
      GCGCG
      GCG
    Sample Output:
      2
    """
    count = 0
    for i in range(0, len(Text) - len(Pattern) + 1):
        if Pattern == Text[i : i + len(Pattern)]:
            count += 1
    return count
