# text2json
text2json is a python project created to aide in conversion from text files to json objects.

## Installation

Run converter.py

```bash
py converter.py
```

## Usage

Right now, the converter only accepts single and key value pairs. Hopefully I will add some more freedom into the mixture.

## Examples:

input.txt
```bash
one
two
three
four
five
```

output.json
```json
[
    "one",
    "two",
    "three",
    "four",
    "five"
]
```

input.txt
```bash
one two
three four
five six
```

output.json
```json
{
    "one": "two",
    "three": "four",
    "five": "six"
}
```

## Contributing
Feel free to submit pull requests. For any major changes submit an issue form with as much detail as possible.
