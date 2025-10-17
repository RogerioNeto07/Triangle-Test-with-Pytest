from triangulo import is_triangle

def test_valid_triangle():
    assert is_triangle(7, 7, 7) == True
    assert is_triangle(21, 28, 35) == True
    assert is_triangle(9, 9, 11) == True
    assert is_triangle(8, 16, 22) == True

def test_all_sides_zero():
    assert is_triangle(0, 0, 0) == False

def test_one_side_zero():
    assert is_triangle(8, 16, 0) == False

def test_one_side_equals_sum_of_the_others():
    assert is_triangle(8, 8, 16) == False

def test_one_side_equals_sum_of_the_others():
    assert is_triangle(8, 8, 16) == False

def test_side_shorter_sum__sides_divided_by2():
    assert is_triangle(5, 1, 2) == False