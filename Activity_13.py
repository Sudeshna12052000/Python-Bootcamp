start = int(input("Enter the start of number: "))
end = int(input("Enter the stop number: "))
for num in range(start, end + 1):
	if num % 2 != 0:
		print(num,",", end = " ")
