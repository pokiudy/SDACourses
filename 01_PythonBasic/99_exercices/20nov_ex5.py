#Context manager - libraria os-operating system

import os

with os.scandir("/Users/klaudiapoka/PycharmProjects/pythonremotero19-exercises/Klaudia/SDACourses") as entries:  # afisare director curent
     for entry in entries:
          print(entry.name, "->", entry.stat().st_size, "bytes")

