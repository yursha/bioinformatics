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


def freq_words(text, k):
    """
    Finds the most frequent k-mers in a string.

    Input:
      A string text and an integer k.
    Output:
      All most frequent k-mers in text.

    Sample input:
      ACGTTGCATGTCGCATGATGCATGAGAGCT
      4
    Sample output:
      CATG GCAT
    """
    freq_map = {}
    max = 0
    for i in range(len(text) - k + 1):
        pattern = text[i : i + k]
        count = freq_map[pattern] if pattern in freq_map else 0
        count += 1
        if count > max:
            max = count
        freq_map[pattern] = count

    return [pattern for pattern in freq_map if freq_map[pattern] == max]


def pattern_count(text, pattern):
    """
    Computes the number of times that a k-mer pattern appears as a substring of text.

    Sample Input:
      GCGCG
      GCG
    Sample Output:
      2
    """
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        if pattern == text[i : i + len(pattern)]:
            count += 1
    return count
