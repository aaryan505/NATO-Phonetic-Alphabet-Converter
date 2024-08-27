# NATO Phonetic Alphabet Converter

This Python script converts a user-input word into its corresponding NATO phonetic alphabet code words. 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/aaryan505/nato-phonetic-alphabet.git
    ```
2. Navigate to the project directory:
    ```bash
    cd nato-phonetic-alphabet
    ```
3. Install the required dependencies:
    ```bash
    pip install pandas
    ```

## Usage

1. Ensure you have a `nato_phonetic_alphabet.csv` file in the same directory. The CSV file should have two columns: `letter` and `code`.
   
2. Run the script:
    ```bash
    python phonetic_converter.py
    ```

3. Enter a word when prompted, and the script will output a list of the corresponding NATO phonetic code words.

## Example

If you enter the word `Hello`, the output will be:
```python
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
