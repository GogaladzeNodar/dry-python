import pytest
from Versioning import Versions


def test_basic_semantic_tag():
    """
    Test basic semantic versioning comparisons.
    """
    assert Versions("1.0.0") < Versions("1.0.1")
    assert Versions("1.0.1") > Versions("1.0.0")
    assert Versions("1.0.0") < Versions("1.1.0")
    assert Versions("1.1.0") > Versions("1.0.0")
    assert Versions("1.0.0") < Versions("2.0.0")
    assert Versions("2.0.0") > Versions("1.0.0")
    assert Versions("1.2.3") == Versions("1.2.3")


def test_pre_release_vs_normal():
    """
    Test pre-release versions against normal versions.
    """
    assert Versions("1.0.0-alpha") < Versions("1.0.0")
    assert Versions("1.0.0-beta") < Versions("1.0.0")
    assert Versions("1.0.0-beta") != Versions("1.0.0")


def test_pre_release_string_comparison():
    """
    test pre-release versions with string comparisons.
    """
    assert Versions("1.0.0-alpha") < Versions("1.0.0-beta")
    assert Versions("1.0.0-beta") < Versions("1.0.0-rc")
    assert Versions("1.0.0-alpha.1") < Versions("1.0.0-alpha.beta")
    assert Versions("1.0.0-beta") != Versions("1.0.0-rc")
    assert Versions("1.0.0-alpha.1") != Versions("1.0.0-alpha.beta")


def test_pre_release_numeric_vs_string():
    """
    Test pre-release versions with numeric and string components.
    """
    assert Versions("1.0.0-alpha.1") < Versions("1.0.0-alpha.2")
    assert Versions("1.0.0-alpha.2") < Versions("1.0.0-alpha.beta")
    assert Versions("1.0.0-beta.1") < Versions("1.0.0-beta.2")
    assert Versions("1.0.0-beta.1") < Versions("1.0.0-rc.2")
    assert Versions("1.0.0-beta.1") < Versions("1.0.0-rc.beta.alpha")
    assert Versions("1.0.0-9") < Versions("1.0.0-a")
    assert Versions("1.0.0-beta.1") != Versions("1.0.0-rc.beta.alpha")
    assert Versions("1.0.0-9") != Versions("1.0.0-a")


def test_pre_release_length_and_numeric_comparison():
    assert Versions("1.0.0-alpha.2") > Versions("1.0.0-alpha.1")
    assert Versions("1.0.0-alpha.10") > Versions("1.0.0-alpha.2")
    assert Versions("1.0.0-rc.1") < Versions("1.0.0-rc.1.1")
    assert Versions("1.0.0-alpha.beta.1") > Versions("1.0.0-alpha.2")
    assert Versions("1.0.0-rc.1") != Versions("1.0.0-rc.1.1")


def test_equality_with_pre_release():
    """
    Test equality with pre-release versions.
    """
    assert Versions("1.0.0-alpha") == Versions("1.0.0-alpha")
    assert Versions("1.0.0-beta") == Versions("1.0.0-beta")
    assert Versions("1.2.3-alpha.1") == Versions("1.2.3-alpha.1")
    assert Versions("2.0.0-rc.1") != Versions("2.0.0-rc.2")


def test_build_metadata_is_ignored():
    assert Versions("1.0.0-ab+build.1") < Versions("1.0.0+build.2")
    assert Versions("1.0.0-rc+build.2") < Versions("1.0.0+build.1")


def build_is_not_priority_but_make_difference_in_equality():
    assert Versions("1.0.0+build.1") != Versions("1.0.0+build.2")
    assert Versions("1.0.0-alpha+build.1") == Versions("1.0.0-alpha+build.1")
    assert Versions("1.0.0-rc+build") != Versions("1.0.0-rc+build.2")


def test_invalid_versions_which_can_be_parsed_as_semantic_version():
    """
    Test invalid versions that can be parsed as semantic versions.
    """
    assert Versions("1ab.0c...0+build.1") > Versions("1..0.0alpha.2")
    assert Versions("1.0.0alpha") == Versions("1.0.0-alpha")
    assert Versions("1.0.0alpha.beta.2") > Versions("1.0.0-alpha.beta.1+build.1")
    assert Versions("1.0.0alpha.beta.1") != Versions("1.0.0-alpha.beta+a.1")
    assert Versions("1.0.0-rc+build") != Versions("1.0.0-rc+build.2")


def test_invalid_versions():
    with pytest.raises(ValueError):
        Versions("1.2")

    with pytest.raises(ValueError):
        Versions("a.b.c")

    with pytest.raises(ValueError):
        Versions("1.2.c")

    with pytest.raises(ValueError):
        Versions("v1.v.vv3")

    with pytest.raises(ValueError):
        Versions("1.0.a0-alpha")
