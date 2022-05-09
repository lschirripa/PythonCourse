# LOOK BEFORE YOU LEAP

import os 

p = '../python4begginers'

if os.path.exists(p):     #what if the file exist but contains garbage? or is it only a dir and not a file? also could exist race condition here
    process_file(p)
else:
    print(f'no such file as {p}')


# EASIER TO ASK FORGIVENESS THAN PERMISSION

p = '../python4begginers'

try:
    process_file(p)
except OSError as e:           #with OSError we cath al manner of conditions such as file not found
    print(f'error: {e}')

