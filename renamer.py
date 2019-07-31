import os
from datetime import datetime

folder = "/Users/maxwellvalentine/Desktop/Pics"
location = input("Photo location:")
files = os.listdir(folder)

number = 1
for filename in files:
    if not filename.startswith('.'):
        file = os.path.join(folder, filename)
        extension = os.path.splitext(file)
        m_time = os.path.getmtime(file)
        real_time = datetime.fromtimestamp(m_time)
        f_time = datetime.strftime(real_time, "%y-%B-%d %H-%M-%S")
        new_filename = str(number) + " " + f_time + " " + location + extension[1]
        new_file = os.path.join(folder, new_filename)
        os.rename(file, new_file)
        number += 1