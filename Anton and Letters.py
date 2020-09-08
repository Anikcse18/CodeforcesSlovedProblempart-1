letters = list(map(str, input()))
st = set()

for i in letters:
    if i.isalpha():
        st.add(i)
print(len(st))
