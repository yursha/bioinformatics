import sys
import bio

with open(sys.argv[1]) as f:
    genome = f.readline().strip()
    params = next(f)
    dnaa_length = int(params[0])

    result = bio.frequences(genome, dnaa_length)
    print(" ".join([str(i) for i in result]))
