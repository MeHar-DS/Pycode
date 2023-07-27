from urllib.request import urlopen

story = urlopen("http://sixty-north.com/c/t.txt")
story_words = []

# to convert to and from bytes - encode decode methods are used
for line in story:
    line_words = line.split()  # Always the http content is transferred in bytes hence this will result in byte strings
    line_words = line.decode('utf8').split()  # This decode('utf8') will convert the bytes to strings
    for word in line_words:
        story_words.append(word)

story.close()

print(story_words)