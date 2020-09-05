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
