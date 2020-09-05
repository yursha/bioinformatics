import sys

from bio import reverse_complement

with open(sys.argv[1]) as f:
    read_data = f.read().strip()
    print(reverse_complement(read_data))
