
# A little script to make a load of posts

for a in range(1,10):
    markd = f"---\ntitle: Post Number {a}\ndate: 2018-01-01\nauthor: MartBot\n---\n\n# Post Number {a}\n\nThis is a test post"
    fName = f"./posts/post-{a}.md"
    with open(fName, 'w') as file:
        file.write(markd)