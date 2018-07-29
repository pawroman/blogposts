from pytest import raises, approx

from pyproject.calculations.running import running_sum


def test_running_sum_empty_input():
    assert list(running_sum([])) == []


def test_running_sum_range_100():
    numbers = range(100)
    result_list = list(running_sum(numbers))

    assert len(result_list) == len(numbers)
    assert result_list[0] == 0
    assert result_list[-1] == sum(numbers)

    assert result_list[49] == sum(numbers[:50])


def test_running_sum_invalid_types():
    invalid_input_str = [1, 2, "42"]
    invalid_input_list = [[1], 2, 3]

    with raises(TypeError):
        list(running_sum(invalid_input_str))

    with raises(TypeError):
        list(running_sum(invalid_input_list))


def test_running_sum_floats():
    assert list(running_sum([1.0, 3.11, 5.33])) == approx([1.0, 4.11, 9.44])
