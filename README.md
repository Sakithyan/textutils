# textutils

A lightweight Python library for common text-processing operations.

## Features

- Word counting
- Character counting
- Reversing text
- Capitalizing words
- Text statistics

## Installation

pip install textutils

## Usage

from textutils import word_count

count = word_count("Homework 1 Open Source !")

from textutils import text_statistics

stats = text_statistics("You are the most incredible person.")
print(stats["word_count"])  

## Contributing

Contributions are welcome!

## License

MIT License