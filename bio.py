def find(sequence, pattern):
    """
    Returns a list of positions where `patterns` is found in `sequence`.

    Use this function to check if a presumed DnaA box sequence occurs
    outsite the ori region. If it does, the presumption may be wrong.
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
            raise RuntimeError("Unsupported sequence character: '%s'" % c)
    return reverse


def reverse_complement(sequence):
    return complement(sequence)[::-1]


def find_reverse_complements(patterns):
    groups = {}
    for pattern in patterns:
        compl = reverse_complement(pattern)
        if compl in groups:
            groups[compl] = pattern
        else:
            groups[pattern] = True
    return [(k,) if groups[k] == True else (k, groups[k]) for k in groups]


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
