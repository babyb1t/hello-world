def divisions_function(x:int, y:int) -> float:
	""""""
	try:
		return x/y
	except ZeroDivisionError:
		return -1


if __name__ == '__main__':
	divisions_function(3,5)