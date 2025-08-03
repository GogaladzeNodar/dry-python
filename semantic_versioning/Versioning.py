import functools
from validators import is_valid_version


@functools.total_ordering
class Versions:
    """
    this class contains the version information for the semantic versioning system.
    """

    def __init__(self, version: str):
        self.major, self.minor, self.patch, self.pre_release = self.parser(version)

    def parser(self, version: str):

        if not is_valid_version(version):
            raise ValueError(f"Invalid semantic version string: '{version}'")

        if "-" in version:
            base_version, pre_release_part = version.split("-", 1)
            pre_release = [
                s for s in pre_release_part.split(".")
            ]  # this divides prerelease part
        else:
            base_version = version
            pre_release = []

        base_version_parts = base_version.split(".")
        major = int(base_version_parts[0])
        minor = int(base_version_parts[1])
        patch = int(base_version_parts[2])

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

        # here we compare pre-release versions

        if self.pre_release and not other.pre_release:
            return True
        if not self.pre_release and other.pre_release:
            return False

        # now if both of them have prerelease, we must compare pre_release list

        if self.pre_release and other.pre_release:
            # compare each part of pre_release
            for self_part, other_part in zip(self.pre_release, other.pre_release):
                is_self_num = self_part.isdigit()
                is_other_num = other_part.isdigit()

                if is_self_num and is_other_num:
                    if int(self_part) != int(other_part):
                        return int(self_part) < int(other_part)
                elif is_self_num and not is_other_num:
                    return False
                elif not is_self_num and is_other_num:
                    return True
                else:  # both are strings
                    if self_part != other_part:
                        return self_part < other_part

            return len(self.pre_release) < len(other.pre_release)

        return False
