from Versioning import Versions


def main():
    try:

        version1 = Versions("1.0.0-ab+build.1")
        version2 = Versions("1.0.0+build.2")
        version3 = Versions("1.2.3")

        print(f"Is {version1} less than {version2}? {version1 < version2}")
        print(f"Are {version1} and {version2} equal? {version1 == version2}")
        print(f"Is {version3} greater than {version2}? {version3 > version2}")
        # <Versioning.Versions object at 0x10318f7d0>  - override __str__ method to print version nicely

        print("\nTesting an invalid version:")
        Versions("1.2")
    except ValueError as e:
        print(f"Caught expected error: {e}")


if __name__ == "__main__":
    main()
