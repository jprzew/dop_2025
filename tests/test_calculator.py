import sys
from pathlib import Path

src_dir = str(Path(__file__).parent.parent / 'src')

sys.path.insert(0, src_dir)

from calculator import add

print(sys.path)
print(add(3, 4))
