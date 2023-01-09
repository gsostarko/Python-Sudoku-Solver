def find_next_empty(puzzle):
	"""
	Finds the next row, col on the puzzle that's not filled yet --> rep with -1
	Return roq, col tuple (or (None,None) if there is none)
	Keep in mind that we are using 0-8 for our indices
	"""
	for r in range(9):
		for c in range(9): #range(9) is 0,1,2...8
			if puzzle[r][c] == -1:
				return r,c

	return None, None # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
	# Figures out whether the guess at the row/col of the puzzle is a valid guess
	# Returns True if is valid, False otherwise

	# let's start with the row:
	row_vals = puzzle[row]
	if guess in row_vals:
		return False

	# now the columns
	col_vals = [puzzle[i][col] for i in range(9)]
	if guess in col_vals:
		return False

	# and then the square
	# we want to get where the 3x3 square starts
	# and iterate over the 3 values in the row/column

	row_start = (row // 3) * 3 # 1 // 3 = 0, 5 // 3 = 1, ...
	col_start = (col // 3) * 3

	for r in range(row_start, row_start + 3):
		for c in range(col_start, col_start + 3):
			if puzzle[r][c] == guess:
				return False

	# if we get here, these checkspass
	return True

def solve_sudoku(puzzle):
	"""
	Solve sudoku using backtracking!
	Our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
	return whether a solution exists
	Mutates puzzle to be the solution (if solution exists)
	"""
	#Step 1: chose somewhere on the puzzle to make a guess
	row, col = find_next_empty(puzzle)

	# Step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
	if row is None:
		return True

	# Step 2: if there is a place to put a number, then make a guess between 1 and 9
	for guess in range(1, 10):  # range(1,10) is 1,2,3...9

		# Step 3: check if this guess is valid
		if is_valid(puzzle, guess, row, col):

			# Step 3.1: if this is valid, then place that guess on the puzzle!
			puzzle[row][col] = guess

			# now tecurse using this puzzle!
			# Step 4: recursively call out function
			if solve_sudoku(puzzle):
				return True

		# Step 5: if not valid OR if our guess does not solve the puzzle, then we need to 
		# backtrack and try a new number
		puzzle[row][col] = -1 # reset the guess

	# Step 6. if none og the numbers that we try work, then this puzzle is UNSOLVABLE!!
	return False

if __name__ == '__main__':

	example_board = [
		[	3,	9,	-1,		-1,	5,	-1,		-1,	-1,	-1],
		[	-1,	-1,	-1,		2,	-1,	-1,		-1,	-1,	5],
		[	-1,	-1,	-1,		7,	1,	9,		-1,	8,	-1],
		
		[	-1,	5,	-1,		-1,	6,	8,		-1,	-1,	-1],
		[	2,	-1,	6,		-1,	-1,	3,		-1,	-1,	-1],
		[	-1,	-1,	-1,		-1,	-1,	-1,		-1,	-1,	4],

		[	5,	-1,	-1,		-1,	-1,	-1,		-1,	-1,-1],
		[	6,	7,	-1,		1,	-1,	5,		-1,	4,	-1],
		[	1,	-1,	9,		-1,	-1,	-1,		2,	-1,	-1]
	]

	print(solve_sudoku(example_board))
	print(example_board)