def encode(source_numbers, max_length):
    out = []
    for current_number in source_numbers:
        binary = []
        digit_counter = 0
        for k in range(current_number.bit_length()):
            binary.append(current_number%2)
            current_number = current_number//2
            digit_counter += 1
        binary.extend([0 for _ in range(max_length - digit_counter)])
        binary.reverse()
        out.append(binary)
    return out


def decode(source_numbers):
    out = []
    gene_length = source_numbers[0]
    for current_gene in source_numbers:
        number = 0
        current_gene.reverse()
        for i in range(gene_length):
            number += current_gene[i]*pow(2, i)
        out.append(number)
    return out
