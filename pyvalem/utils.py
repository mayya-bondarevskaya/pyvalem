def parse_fraction(s):
    """
    Parse an integer or fraction as a pyparsing.ParseResults object resulting
    from a match to '2', '3/2', etc. into a float. If s is None or the empty
    string, return None.

    """

    if not s:
        return None
    if len(s) == 2:
        num, det = s
        return float(num) / int(det)
    elif len(s) == 1:
        if s:
            return float(s[0])

    raise ValueError(s, 'does not parse to an integer or fraction')
