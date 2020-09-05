import sys
import bio

with open(sys.argv[1]) as f:
    genome = f.readline().strip()
    params = next(f).split()
    dnaa_length = int(params[0])
    ori_length = int(params[1])
    min_freq = int(params[2])

    result = bio.find_clupms(genome, dnaa_length, ori_length, min_freq)
    # print(" ".join(result))
    print("Total: {}".format(len(result)))
