def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'


def subtract(a, b):
    # Here was the mistake and now it is fixed.
    return a - b  # <--- fix this in step 8


# uncomment the following test in step 5
def test_subtract():
    assert subtract(2, 3) == -1
