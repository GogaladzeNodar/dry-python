class Versions:
    """
    this class contains the version information for the semantic versioning system.
    """

    def __init__(self, version: str):
        pass

    def parser(self, version: str):

        parts = version.split("-", 1)  # split into version and pre-release
        base_version = parts[0]
        pre_release = parts[1] if len(parts) > 1 else None

        major, minor, patch = map(
            int, base_version.split(".")
        )  # map is lazy, so it won't evaluate until needed

        return major, minor, patch, pre_release
