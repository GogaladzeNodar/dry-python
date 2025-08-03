from Versioning import Versions


if __name__ == "__main__":

    print(Versions("1.0.0") < Versions("1.0.1"))  # True
    print(Versions("1.0.1-alpha") < Versions("1.0.1"))  # True
    print(Versions("1.0.1-beta") < Versions("1.0.1-alpha"))  # False
    print(Versions("1.0.1-alpha") == Versions("1.0.1-alpha"))  # True
    print(Versions("1.0.1-alpha.beta") < Versions("1.0.1-beta.1"))  # True
    print(Versions("1.0.1-beta.2") < Versions("1.0.1-beta.1"))  # False
