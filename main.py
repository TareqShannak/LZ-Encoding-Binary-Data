import math
import random


def generate_sequence(limit):
    string = ''
    for i in range(0, limit):
        x = random.random() * 100
        if x < 95:
            string = string + '1'
        else:
            string = string + '0'
    return string


def parse_data(sequence):
    k = 1
    temp = ''
    for i in sequence:
        if temp in lz_dict.values() or temp == '':
            temp = temp + i
            continue
        lz_dict[k] = temp
        k += 1
        temp = i


def find_phrases(num_of_bits):
    temp = {}
    for present_value in lz_dict.values():
        if len(present_value) == 1:
            temp[present_value] = '0'.rjust(num_of_bits, '0') + present_value[0]
        else:
            for past_key, past_value in lz_dict.items():
                if present_value[:len(present_value) - 1] == past_value:
                    temp[present_value] = str(bin(past_key).replace("0b", "")).rjust(num_of_bits, '0') \
                                          + present_value[len(present_value) - 1]
    return temp


summary_output = "***********************************************\n\tN\t\tNb\t\tNb/N\t# of bits/codeword\n"
# print("\tN\t\tNb\t\tNb/N\t# of bits per codeword")
for N in [100, 500, 1000, 1500, 2000, 2500, 3000, 5000, 10000, 20000]:
    print("\nN = " + str(N))
    lz_dict = {}
    seq = generate_sequence(N)
    parse_data(seq)
    bits = math.ceil(math.log2(len(lz_dict.items()))) + 1

    # print(lz_dict)
    codewords = find_phrases(bits)
    # print(codewords)
    print("Original Sequence: " + seq)
    encoded_sequence = ''.join([str(item) for item in codewords.values()])
    print("Encoded Sequence:  " + encoded_sequence + "\n")
    if N == 100:
        print("Dictionary Location\t\tDictionary Contents\t\tCodeword")
        for key, value in lz_dict.items():
            print("\t" + str(key).rjust(3) + " " + str(bin(key).replace("0b", "")).rjust(bits - 1, '0') + "\t\t"
                  + str(value).rjust(15) + "\t\t\t\t" + codewords[value][:len(codewords[value]) - 1] + " "
                  + codewords[value][len(codewords[value]) - 1])

    summary_output += str(N).rjust(5) + "\t" + str(len(encoded_sequence)).rjust(5) + "\t\t" + str(
        round((len(encoded_sequence) / N) * 100, 2)).rjust(5) + "%\t\t\t" + str(bits) + "\n"
print(summary_output)
