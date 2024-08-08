# Strings are group of characters
name = "Daw Khin Thandar Thet Cho Pyone"

# string can count with index like array
print(name[0]) # D
print(name[1]) # a

# string slicing  [start:end] | [start:end:step]
print(name[4:10]) # Khin T
print(name[0:10:2]) # DwKi

# jumping
print(name[::2]) # DwKi hna htCoPoe

# -1 is last of string
print(name[-1]) # e

# reverse slicing
print(name[::-1]) # enoyP ohC tehT radnahT nihK waD
print(name[-1:-10:-1]) # enoyP ohC

# -1 in step is reverse jumping
print(name[-1:-8:-1]) # enoyP o
