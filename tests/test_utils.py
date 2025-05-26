import innertube.utils


def test_removeNoneValues() -> None:
    assert innertube.utils.removeNoneValues({"a": None, "b": "b", "c": "c"}) == {
        "b": "b",
        "c": "c",
    }
