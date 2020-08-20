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
