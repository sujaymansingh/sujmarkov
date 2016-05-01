"""Read lines from a file, feed them into the markov generator, and then
generate a few lines.

Usage:
    sujmarkov.py generate <n> lines from <input-filename> [--n-value=<nv>]

Options:
    -h --help          Show this screen.
    --n-value=<nv>     The size of n-grams to use in the markov generator. [Default: 2]
"""
from __future__ import print_function

import docopt

import sujmarkov


def generate(input_filename, num_lines, ngram_value):
    generator = sujmarkov.Markov(n=ngram_value)

    with open(input_filename, "r") as input_file:
        for sentence in extract_sentences(input_file):
            generator.add(sentence)

    for i in range(num_lines):
        generated_sentence = " ".join(generator.generate())
        print(generated_sentence)


def extract_sentences(input_file):
    # Each line is a sentence.
    #
    for raw_line in input_file:
        line = raw_line.lower().strip()

        # For now, ignore punctuation.
        #
        line = line.replace(",", "").replace("-", "").replace('"', '')

        for sub_line in line.split("."):
            raw_sentence = sub_line.split(" ")

            sentence = [word for word in raw_sentence if word and word.strip() != ""]
            if sentence:
                yield sentence


if __name__ == "__main__":
    args = docopt.docopt(__doc__)

    if args.get("generate"):
        num_lines = int(args["<n>"])
        n_value = int(args["--n-value"])
        input_filename = args["<input-filename>"]

        generate(input_filename, num_lines, n_value)
