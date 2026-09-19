# Text Analyzer

🇪🇸 [Readme en Español](README_es.md)

This repository contains a small command-line text analyzer written in Python. It is the Day 3 project from Federico Garay's **Python TOTAL with AI: From Zero to Full Programmer in 16 Days** course.

The goal of the exercise is to combine the concepts introduced during the first three days of the course in a simple, fully functional program. For that reason, the solution intentionally uses only the material covered up to that point: basic data types, strings and their methods, lists, dictionaries, booleans, indexing, slicing, and built-in functions. It does not use loops or conditional statements.

## How the program works

The program first asks the user to enter any text, such as a sentence, paragraph, article, or poem. It then asks for exactly three letters separated by spaces.

Using those inputs, it performs five analyses:

1. **Letter frequency** - Counts how many times each of the three selected letters appears in the text. The comparison is case-insensitive, so uppercase and lowercase versions of a letter are counted together.
2. **Word count** - Splits the text into words and reports the total number of words.
3. **First and last characters** - Uses string indexing to display the first and last characters of the original text.
4. **Reversed word order** - Reverses the order of the words and joins them into a new string. The characters inside each word remain unchanged.
5. **Python check** - Reports whether the word sequence `python` appears anywhere in the text, regardless of capitalization. A boolean value is used as a dictionary key to select the appropriate message without an `if` statement.

## Concepts practiced

- Reading user input with `input()`
- String methods such as `lower()`, `count()`, `split()`, and `join()`
- List unpacking
- Measuring a list with `len()`
- Positive and negative indexing
- Slicing with a negative step to reverse a list
- Membership checks with `in`
- Booleans and dictionaries
- Formatted strings (f-strings)

## Requirements

- Python 3
- No third-party packages

## Running the program

From the project directory, run:

```bash
python3 main.py
```

When prompted, enter a non-empty text and then exactly three letters separated by spaces:

```text
Introduce un texto: Python makes text analysis simple
Ahora introduce 3 letras separadas por espacios: a t p
```

The program's prompts and results are currently displayed in Spanish.

## Program screenshot

<p align="center">
  <img src="text_analyzer.png" alt="Text Analyzer running in the terminal" width="1200">
</p>

## Input assumptions

This beginner-level solution assumes valid input:

- The text must not be empty because the program reads its first and last characters.
- The second response must contain exactly three space-separated values so they can be unpacked into three variables.

Input validation is intentionally outside the scope of the exercise because it would require concepts not included in the first three days of the course.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

## Contact

Created by Raul Estevez.

- Website: [raulesteveza.github.io](https://raulesteveza.github.io)
- LinkedIn: [linkedin.com/in/raulesteveza](https://www.linkedin.com/in/raulesteveza/)
