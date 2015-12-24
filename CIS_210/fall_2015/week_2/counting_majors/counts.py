"""
Count the number of occurrences of each major code in a file.
Authors: #FIXME
Credits: #FIXME

Input is a file in which major codes (e.g., "CIS", "UNDL", "GEOG")
appear one to a line. Output is a sequence of lines containing major code
and count, one per major.
"""

import argparse

def count_codes(majors_file):
    """
    counts and outputs the unique major codes in a file
    args:
        majors_file: The file which holds the major codes to be counted
    returns:
        nothing
    """
    majors = [] # create a new empty list to hold the counts

    # remove newline character and append string to majors list
    for line in majors_file:
        majors.append(line.strip())

    majors = sorted(majors) # sort the major codes alphabetically

    count = 0
    temp = majors[0]
    for major in majors:
        if temp == major:
            count += 1
        else:
            print(temp, count)
            temp = major
            count = 1
    print(temp, count)

def main( ):
    """
    Interaction if run from the command line.
    Usage:  python3 counts.py  majors_code_file.txt
    """
    parser = argparse.ArgumentParser(description="Count major codes")
    parser.add_argument('majors', type=argparse.FileType('r'),
                        help="A text file containing major codes, one major code per line.")
    args = parser.parse_args()  # gets arguments from command line
    majors_file = args.majors
    count_codes(majors_file)
    
    
if __name__ == "__main__":
    main( )
