"""TODO: this module is for giving the students their grades base on there GPAS."""


def letter_grade(gpa):
    """TODO: calculate the grade base on the GPAS."""
    # TODO: your if/elif chain here
    if gpa >= 4.50:
        return "A"
    elif gpa >= 3.50:   
        return "B"
    elif gpa >= 2.50:
        return "C"
    elif gpa >= 1.50:
        return "D"
    else:
        return "F"
