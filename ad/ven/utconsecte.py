# Define a function to read a file in chunks
def read_in_chunks(file_path, chunk_size=1024):
    """Lazy function to read a file piece by piece."""
    with open(file_path, 'r') as file:
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield data

# Usage example
for piece in read_in_chunks('your_file.txt'):
    process(piece)  # Replace with your actual processing code
