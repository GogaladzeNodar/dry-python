from Versioning import Versions


if __name__ == "__main__":

    def main():
        versions = [
            Versions("1.0.0"),
            Versions("1.0.1"),
            Versions("1.0.1-alpha"),
            Versions("1.0.1-beta"),
        ]

    print(Versions("1.0.0") < Versions("1.0.1"))  # True
    print(Versions("1.0.1-alpha") < Versions("1.0.1"))  # True
