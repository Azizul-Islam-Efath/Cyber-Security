poem = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
"""


'''Writing in the file'''

with open("file1.txt", "w") as f:
   f.write(poem)

print("Poem written to file successfully!\n")


'''Reading in the file'''
with open("file1.txt","r") as f:
   file=f.read()


'''Checking throung the file if twinkle exist
file=f.read()  it reads the file and store the text into variable "file"

in is a keyword which matches if a string twinkle is present in the file or not!
'''

if "twinkle" in file.lower():
   print("Yes. Twinkle is present in the file.")
else:
   print("Twinkle is not present in the file.")