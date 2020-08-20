def PatternCount(Text, Pattern):
    count = 0
    for i in range(0, len(Text) - len(Pattern) + 1):
        if Pattern == Text[i : i + len(Pattern)]:
            count += 1
    return count
