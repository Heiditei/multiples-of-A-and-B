import sys


def assign_files():
    verified_input_file = 'inputfile.txt'
    if len(sys.argv) > 1:
        verified_input_file = sys.argv[1]

    verified_output_file = 'outputfile.txt'
    if len(sys.argv) > 2:
        verified_output_file = sys.argv[2]

    verified_files = [verified_input_file, verified_output_file]
    return verified_files


def initiate_file_content(infile, outfile):
    open(outfile, 'w').close()
    with open(infile) as inp:
        input_rows = [line.rstrip('\n').split() for line in inp]
    return input_rows


def sort_n_print(outfile):
    with open(outfile, 'r') as resultFile:
        outcomes = sorted(resultFile.readlines(), key=len)
        for line in outcomes:
            print(line.strip())

    with open(outfile, 'w') as res:
        res.write(' '.join(outcomes)+'\n')


def check_for_multiples(infile, outfile):
    input_rows = initiate_file_content(infile, outfile)

    with open(outfile, 'a') as appendingOutFile:
        for row in input_rows:
            row = list(map(int, row))
            a = row[0]
            b = row[1]
            goal = row[-1]
            multiples_of_row = [str(goal)+':']
            i = 1
            while i < goal:
                if i % a == 0 or i % b == 0:
                    multiples_of_row.append(str(i))
                i += 1
            appendingOutFile.write(' '.join(multiples_of_row)+'\n')
            appendingOutFile.flush()
    sort_n_print(outfile)


if __name__ == "__main__":
    files = assign_files()
    check_for_multiples(files[0],files[1])
