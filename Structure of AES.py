# Function to convert a 16-byte array into a 4x4 matrix
def bytes_to_matrix(text):
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

# Function to convert a 4x4 matrix into a 16-byte array
def matrix_to_bytes(matrix):
    return bytes(sum(matrix, []))

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

# Convert the matrix into bytes and decode as UTF-8
resulting_text = matrix_to_bytes(matrix).decode('utf-8')
print(resulting_text)
