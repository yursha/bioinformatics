def find(sequence, pattern):
    """
    Returns a list of positions where `pattern` is found in `sequence`.

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


def find_clupms(genome, dnaa_length, ori_length, min_freq):
    freq_map = {}
    reverse_map = {}
    result = set()
    for i in range(len(genome) - dnaa_length + 1):
        if i > ori_length - dnaa_length:
            for group in reverse_map.values():
                # if group:
                # print('Adding {} to result'.format(group))
                result |= group
            out_pattern = genome[
                i
                - ori_length
                + dnaa_length
                - 1 : i
                - ori_length
                + dnaa_length
                + dnaa_length
                - 1
            ]
            # print('slide out pattern {}'.format(out_pattern))
            cnt = freq_map[out_pattern]
            freq_map[out_pattern] = cnt - 1

            if cnt == min_freq:
                reverse_map[cnt].remove(out_pattern)
                # print('slide out forget {}'.format(out_pattern))
            elif cnt > min_freq:
                reverse_map[cnt].remove(out_pattern)
                # print('slide out forget {} = {}'.format(out_pattern, cnt))
                reverse_map[cnt - 1].add(out_pattern)
                # print('slide out remember {} = {}'.format(out_pattern, cnt - 1))

        pattern = genome[i : i + dnaa_length]
        # print('inspecting pattern {}'.format(pattern))
        count = freq_map[pattern] if pattern in freq_map else 0
        count += 1
        freq_map[pattern] = count
        # print('freq of pattern {} is {}'.format(pattern, count))

        if count == min_freq:
            if count not in reverse_map:
                reverse_map[count] = set()
            reverse_map[count].add(pattern)
            # print('remember {} = {}'.format(pattern, count))
        elif count > min_freq:
            if count not in reverse_map:
                reverse_map[count] = set()
            reverse_map[count - 1].remove(pattern)
            # print('forget {} = {}'.format(pattern, count - 1))
            reverse_map[count].add(pattern)
            # print('remember {} = {}'.format(pattern, count))

    for group in reverse_map.values():
        result |= group
    return sorted(result)


def pattern_to_number(pattern):
    M = {"A": 0, "C": 1, "G": 2, "T": 3}
    number = 0
    power = len(pattern) - 1
    for c in pattern:
        number += M[c] * (4 ** power)
        power -= 1
    return number
