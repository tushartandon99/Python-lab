def filter_noise(matrix):
    """Filters out negative numbers from each row using filter() and lambda."""
    return [list(filter(lambda x: x >= 0, row)) for row in matrix]

def transform_data(matrix):
    """Applies a mathematical transformation (squaring) using map() and lambda."""
    return [list(map(lambda x: x ** 2, row)) for row in matrix]

def sort_matrix(matrix):
    """Sorts rows based on the sum of their elements using sorted() and a custom lambda key."""
    return sorted(matrix, key=lambda row: sum(row), reverse=True)

# Sample 2D data suite (mixing lists and tuples)
raw_matrix = [
    [3, -1, 4],
    (-5, 2, 8),
    [0, -9, 1]
]

print("Original Data:", raw_matrix)

# 1. Filter out negative matrix noise
clean_matrix = filter_noise(raw_matrix)
print("Filtered (No Negatives):", clean_matrix)

# 2. Transform the clean data sequence
transformed_matrix = transform_data(clean_matrix)
print("Transformed (Squared):", transformed_matrix)

# 3. Sort entries using custom keys (Descending row sum)
sorted_matrix = sort_matrix(transformed_matrix)
print("Sorted (By Row Sum):", sorted_matrix)