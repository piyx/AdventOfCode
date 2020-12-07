for i in range(7, 26):
    comment = '# reading the input\n'
    withopen = f"with open('input{i}.txt', 'r') as f:\n"
    with open(f'day{i}.py', 'w') as f:
        f.write(comment)
        f.write(withopen)
        f.write('\tpass')
