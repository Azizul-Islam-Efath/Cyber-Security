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

with open("file4.txt", "w") as f:
   f.write(poem)

print("Poem written to file successfully!\n")


'''Reading in the file'''
with open("file4.txt","r") as f:
   file=f.read()

Replace=file.replace("twinkle","Uncle")


with open("file4.txt","w") as f:
   f.write(Replace)

print(f"twinkle Replaced with Uncle Successfully!.")
