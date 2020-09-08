perticipent,pen,note_book = input().split(" ")
perticipent = int(perticipent)
pen = int(pen)
note_book = int(note_book)
if perticipent<=pen and perticipent<=note_book:
    print("Yes")
else:
    print("No")
