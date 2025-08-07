import re


def is_something_like_semantic_version(version):
    """
    Checks if the given version string is similar to a semantic version.
    """
    version = normalize_dots(version)
    pattern = r"^.+?\..+?\..*"
    if re.match(pattern, version):
        return version  # if true, at last we have two dots to split major, minor and pactch or patch and pre-release
    raise ValueError("Invalid semantic version string: '{}'".format(version))


def normalize_dots(version):
    """
    Normalize the version string by replacing multiple dots with a single dot.
    Also removes leading dots.
    This is useful for ensuring consistent formatting of version strings.
    for example, "abc..def...ghi" -> "abc.def.ghi"
                 "...hello..world...again" -> "hello.world.again"
    """
    version = re.sub(r"^\.+", "", version)
    version = re.sub(r"\.{2,}", ".", version)
    return version


def extract_int_from_string(version):
    """
    Extracts the sequences of digits from a string and returns them as an integer.
    """

    digits = re.findall(r"\d+", version)
    if digits:
        return int("".join(digits))
    raise ValueError(f"No digits found in the input: '{version}'")


def split_on_first_two_dots(version):
    """
    Splits the version string on the first two dots.
    Returns a tuple of (major, minor, patch_and_pre_release).
    """

    parts = version.split(".", 2)

    major, minor, patch_and_pre_release = parts[0], parts[1], parts[2]
    return major, minor, patch_and_pre_release


def split_on_dots(version, delimiter=".", count=None, as_tuple=False):
    """
    Splits the version string by the given delimiter.
    If `count` is None, splits on all occurrences.
    Returns a tuple or list based on `as_tuple`.
    """
    if count is None:
        result = version.split(delimiter)
    else:
        result = version.split(delimiter, count)
    if as_tuple:
        return tuple(result)
    else:
        return result
