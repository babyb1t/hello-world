from variables2 import divisions_function


def test_division():

	assert divisions_function(1/0) == -2


if __name__ == '__main__':
	test_division()