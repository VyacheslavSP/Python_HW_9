import Calculations
import Valid_strring


def calc(input_string):
    string = input_string
    val_string = Valid_strring.valid_string(string)
    return (Calculations.Calc(val_string))
