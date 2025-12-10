
import html
import re

def Validate(form):
    for input in form:
        input = html.escape(input)
        input = re.sub(r'[^a-zA-Z0-9+\-*\/\(\)\s]', '', input)
    if int(form["eDim"][0]) not in range(1, 6):
        raise ValueError("E-Dimension must be in the range [1,5]")
    if len(form["aList"])//3 not in range(0, 21):
        raise ValueError("A-Variable count may not exceed 20")
    if len(form["genFam"]) not in range(0, 800):
        raise ValueError("Genfam contains too many characters. To bypass, edit LPGd.py Validation().")
    if float(form["granularity"][0]) < .0005:
        raise ValueError("Granularity has a minimum value of .0005")