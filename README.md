# Harvard CS50P - Programming with Python 🚀

This repository tracks my progress, implementation logic, and key takeaways as I complete Harvard University's introduction to computer science using Python.


## 🛠️ Problem Set 0: Functions & Variables

### 1. Indoor Voice
* **Objective:** Automatically clean user strings by converting any vocal shouting/caps lock input into standard lowercase text.
* **Key Concept:** Practiced standard input stream sanitization using Python's built-in `.lower()` string method.

### 2. Playback Speed
* **Objective:** Simulate a slower media playback speed (0.75x) by programmatically inserting structural pauses (`...`) between phrase segments.
* **Key Concept:** Used token replacement logic via the `.replace()` string method to change delimiter spaces seamlessly.

### 3. Making Faces
* **Objective:** Build a parsing function that scans a string for legacy text-based emoticons (`:)`, `:(`) and dynamically swaps them out for unified modern emojis.
* **Key Concept:** Structured modular code using explicit code architecture (`main()` and helper functions) and handled string manipulations.

### 4. Einstein ($E = mc^2$)
* **Objective:** Create a lightweight physics computational engine that takes a mass input in kilograms and outputs the Joules equivalent based on the speed of light.
* **Key Concept:** Handled user input conversions from string to integer types (`int()`) and calculated values using the exponentiation operator (`**`).

### 5. Tip Calculator
* **Objective:** Process raw alphanumeric currency values (stripping symbols like `$` and `%`) to compute precise percentage layouts for standard tip handling.
* **Key Concept:** Mastered data casting, clearing explicit text patterns, and returning localized floating-point data arrays (`float`).



🛠️ **Problem Set 1: Conditionals**

1. **Deep Thought**
**Objective**: Prompt the user for the answer to the Great Question of Life, the Universe, and Everything, accepting numeric or text variations.
**Key Concept**: Implemented case-insensitive string matching and checked multiple valid conditions using the `in` operator and `.lower().strip()` sanitization.

2. **Home Federal Savings Bank**
**Objective**: Emulate a bank greeting penalty system that outputs $0 for "hello", $20 for greetings starting with "h", and $100 otherwise.
**Key Concept**: Leveraged conditional branching (`if`/`elif`/`else`) combined with the `.startswith()` string method to evaluate prefix patterns.

3. **File Extensions**
**Objective**: Read a filename from the user and output its official MIME/media type based on its suffix.
**Key Concept**: Extracted file trailing substrings using `.endswith()` or `.split()`, mapping user variations to standardized web media types.

4. **Math Interpreter**
**Objective**: Build a basic CLI calculator that parses an arithmetic expression formatted as a string (e.g., `1 + 1`) and outputs the floating-point result.
**Key Concept**: Applied string tokenization via `.split()` to unpack variables, followed by data type casting and conditional math operations.

5. **Meal Time**
**Objective**: Program a schedule checker that inputs a time string (24-hour format) and outputs whether it falls within breakfast, lunch, or dinner intervals.
**Key Concept**: Authored custom parsing logic to convert time strings into a unified floating-point hours system ($hours + \frac{minutes}{60}$) to handle numeric range comparisons.


# CS50P - Problem Set 2: Loops

This repository contains my solutions to the problems from Problem Set 2 of [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/). 

## 🚀 Problems Overview

### 1. camelCase (`camel.py`)
A program that prompts the user for the name of a variable in camelCase and outputs the corresponding name in snake_case.
* **Concepts:** String manipulation, loops, conditional statements.
* **Example:** `firstName` $\rightarrow$ `first_name`

### 2. Coke Machine (`coke.py`)
A program that simulates a vending machine selling a bottle of Coca-Cola for 50 cents. It only accepts coins in denominations of 25, 10, and 5 cents, informs the user of the amount due, and calculates any change owed.
* **Concepts:** `while` loops, arithmetic operations, user input validation.

### 3. Just setting up my twttr (`twttr.py`)
A program that prompts the user for a string of text and then outputs that same text but with all vowels (A, E, I, O, U) omitted, whether inputted in uppercase or lowercase.
* **Concepts:** String filtering, member checking (`in` operator).
* **Example:** `Twitter` $\rightarrow$ `Twttr`

### 4. Vanity Plates (`plates.py`)
A program that validates requirements for custom license plates based on specific rules (must start with at least two letters, maximum of 6 characters, numbers must come at the end and cannot start with a '0', no periods or spaces).
* **Concepts:** Functions, custom validation logic, string methods (`.isalpha()`, `.isdigit()`, `.isalnum()`).

### 5. Nutrition Facts (`nutrition.py`)
A program that prompts users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, matching the official FDA guidelines for the 20 most common fruits.
* **Concepts:** Dictionaries (`dict`), case-insensitive lookups, dictionary key checking.
* **Example:** `Apple` $\rightarrow$ `Calories: 130`

---
*Progress tracking logged manually as tasks are verified and submitted via check50.*




