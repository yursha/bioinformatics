import sys
import bio

with open(sys.argv[1]) as f:
    pattern = f.readline().strip()
    genome = f.readline().strip()

    positions = bio.find(genome, pattern)
    print(" ".join([str(p) for p in positions]))
