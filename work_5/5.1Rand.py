import random
from pathlib import Path
import string

for i in range(10):
    symbols = string.ascii_lowercase + string.digits
    filename = ""
    for j in range(8):
        filename += random.choice(symbols)
    filename += ".txt"
    file = Path(filename)
    file.touch()
    print(file.absolute())