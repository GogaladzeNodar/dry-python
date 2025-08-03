import functools


@functools.total_ordering
class Versions:
    """
    this class contains the version information for the semantic versioning system.
    """

    def __init__(self, version: str):
        self.major, self.minor, self.patch, self.pre_release = self.parser(version)

    def parser(self, version: str):

        parts = version.split("-", 1)  # split into version and pre-release
        base_version = parts[0]
        pre_release = parts[1] if len(parts) > 1 else None

        major, minor, patch = map(
            int, base_version.split(".")
        )  # map is lazy, so it won't evaluate until needed

        return major, minor, patch, pre_release

    def __eq__(self, other):
        if not isinstance(other, Versions):
            return NotImplemented
        return (
            self.major == other.major
            and self.minor == other.minor
            and self.patch == other.patch
            and self.pre_release == other.pre_release
        )

    def __lt__(self, other):
        if not isinstance(other, Versions):
            return NotImplemented
        if self.major != other.major:
            return self.major < other.major
        if self.minor != other.minor:
            return self.minor < other.minor
        if self.patch != other.patch:
            return self.patch < other.patch
        return (self.pre_release or "") < (other.pre_release or "")
