#!/usr/bin/env python

import os
import sys
import nltk

# Download the necessary nltk resources (if not already downloaded)
nltk.download('punkt')
from nltk.tokenize import word_tokenize


def preprocess_text(text):
    """
    Preprocess the input text:
    - Remove empty lines
    - Tokenize the text into words
    """
    # Split text by lines and remove empty lines
    lines = [line for line in text.splitlines() if line.strip()]

    # Tokenize each line into words and join them into a string
    tokenized_text = [' '.join(word_tokenize(line)) for line in lines]

    # Join the tokenized lines back into a single string
    return '\n'.join(tokenized_text)


def walk_dir(input_dir, output_dir, topdown=True):
    files_list = []
    count = 0

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Walk through the input directory
    for root, dirs, files in os.walk(input_dir, topdown):
        for name in files:
            if name.endswith('.txt'):  # Now processing .txt files
                try:
                    input_file = os.path.join(root, name)
                    output_file = '%s/%d.processed.txt' % (output_dir, count)  # New output filenames
                    print(f"Processing: {output_file}")
                    count += 1

                    # Read the input file
                    with open(input_file, 'r', encoding='utf-8') as f:
                        text = f.read()

                    # Preprocess the text (remove empty lines and tokenize)
                    processed_text = preprocess_text(text)

                    # Write the processed text to the output file
                    with open(output_file, 'w', encoding='utf-8') as f_out:
                        f_out.write(processed_text)

                    # Add the processed file to the files list
                    files_list.append(input_file)

                except Exception as e:
                    print(f"Error processing file {input_file}: {str(e)}")
                    continue

    # Write file information to the output directory
    try:
        with open(f'{output_dir}/fileinfo.txt', 'w', encoding='utf-8') as fout:
            for i in range(len(files_list)):
                fout.write(f'{i}\t{files_list[i]}\n')
    except Exception as e:
        print(f"Error writing file info: {str(e)}")

    # Optionally, run any post-processing scripts if necessary
    try:
        os.system('./bin/write_line.py %s' % output_dir)
    except Exception as e:
        print(f"Error executing write_line.py script: {str(e)}")

    print('All files processed:', len(files_list))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('./walk.py input_dir output_dir\n')
        sys.exit()

    walk_dir(sys.argv[1], sys.argv[2])
