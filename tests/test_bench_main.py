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
def test_ackermann(benchmark, a, b, expected):
    benchmark(ackermann, a, b)
