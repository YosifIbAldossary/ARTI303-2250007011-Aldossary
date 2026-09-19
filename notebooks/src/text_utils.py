"""Module for text processing utilities."""

def clean_name(raw):
    """Tidy a messy name string.

    Strips surrounding whitespace, collapses repeated inner spaces
    into one, and converts the result to title case.
    """
    return " ".join(raw.split()).title()

