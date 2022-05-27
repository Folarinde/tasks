# Read text from a file, and count the occurence of words in that text

from string import punctuation

def read_file_content(filename):
    with open(filename) as f:
        lines=f.read()
    for p in punctuation:
        if p in lines:
            lines=lines.replace(p,'')
    return lines

print(read_file_content("./story.txt"))

def count_words():
    text = read_file_content("./story.txt")
    words=text.split()    
    new_dict={}
    for w in words:
        if w in new_dict:
            new_dict[w]=new_dict[w]+1
        else:
            new_dict[w]=1
    return new_dict

print(count_words())
