import numpy as np

# 1. Create a NumPy array of zeros with shape (3, 4)
zeros_array = np.zeros((3, 4))
print("Zeros Array:")
print(zeros_array)

# 2. Generate an array of 20 random integers between 1 and 10 and reshape into 4x5 matrix
random_array = np.random.randint(1, 11, 20).reshape(4, 5)
print("\nRandom 4x5 Matrix:")
print(random_array)

# 3. Create a 5x5 identity matrix and extract the diagonal elements into a 1D array
identity_matrix = np.eye(5)
diagonal_elements = np.diag(identity_matrix)
print("\nIdentity Matrix:")
print(identity_matrix)
print("\nDiagonal Elements:")
print(diagonal_elements)

# 4. Create a 4x5 array of even numbers starting from 10
even_matrix = np.arange(10, 50, 2).reshape(4, 5)
print("\n4x5 Even Number Matrix:")
print(even_matrix)

# Extract third column
third_column = even_matrix[:, 2]
print("\nThird Column:")
print(third_column)

# Set fourth row to 1,2,3,4,5
even_matrix[3, :] = [1, 2, 3, 4, 5]
print("\nModified Matrix:")
print(even_matrix)

# 5. Consider two vectors
names = np.array(["Roxana", "Statira", "Roxana", "Statira", "Roxana"])
score = np.array([126, 115, 130, 141, 132])

# Extract all test scores that are smaller than 130
scores_below_130 = score[score < 130]
print("\nScores below 130:")
print(scores_below_130)

# Extract all test scores by Statira
scores_statira = score[names == "Statira"]
print("\nScores of Statira:")
print(scores_statira)

# Add 10 points to Roxana’s scores
score[names == "Roxana"] += 10
print("\nUpdated Scores:")
print(score)
