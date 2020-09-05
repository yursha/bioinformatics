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
