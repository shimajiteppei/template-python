import pytest
from template.main import ackermann


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (0, 0, 1),
        (0, 1, 2),
        (3, 4, 125),
        # (4, 1, 65533),
    ],
)
def test_ackermann(a, b, expected):
    assert ackermann(a, b) == expected
