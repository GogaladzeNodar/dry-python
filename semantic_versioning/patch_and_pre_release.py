import re


def parse_patch_and_pre_release(value):
    """
    Parses the patch and pre-release part of a semantic version string.
    Returns a tuple of (patch, pre_release+build).
    """
    patch, remainder = extract_leading_digits(
        value
    )  # remainder can be pre_release or build or both of them

    pre_release = None
    build = None

    if not remainder:
        return (
            patch,
            pre_release,
            build,
        )  # if remainder is empty, we have no pre_release and build

    pre_release, build = split_by_value(remainder, "+")
    # at this moment if + is not in remainder, pre_release is remainder and build is None
    return (
        patch,
        pre_release,
        build,
    )  # if + is in remainder, pre_release is before + and build is after +


def extract_leading_digits(value):
    """
    Extracts the leading digits from a patch_and_pre_release string.
    Returns the leading digits as an integer and last part as string.
    If leading digits are not found, returns valuerror
    """
    match = re.match(r"(\d+)(.*)", value)
    if match:
        digits = int(match.group(1))
        remainder = match.group(2)
        if remainder.startswith("-"):
            remainder = remainder[1:]
        return digits, remainder
    raise ValueError(f"pattch is not found")


def split_by_value(value, character):
    """
    if character is not in value, returns value and None
    """
    if character in value:
        parts = value.split(character, 1)
        return parts[0], parts[1]
    else:
        return value, None
