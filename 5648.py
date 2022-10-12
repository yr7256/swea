dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
T = int(input())
for t in range(T):
    N = int(input())
    atoms = []
    for i in range(N):
        x, y, d, e = map(int, input().split())
        x = (x+1000) * 2
        y = (y+1000) * 2
        atoms.append([x, y, d, e])
    ans = 0
    while atoms:
        new_atoms = set()
        new_atoms_location = set()
        pop_list = set()
        for atom in atoms:
            x0, y0, d, e = atom
            x1 = x0 + dx[d]
            y1 = y0 + dy[d]
            if 0 <= x1 < 4001 and 0 <= y1 < 4001:
                if (x1, y1) in new_atoms_location:
                    pop_list.add((x1, y1))
                else:
                    new_atoms_location.add((x1, y1))
                new_atoms.add((x1, y1, d, e))
        atoms.clear()
        for new_atom in new_atoms:
            x, y, d, e = new_atom
            if (x, y) in pop_list:
                ans += e
            else:
                atoms.append((x, y, d, e))
    print(f'#{t+1} {ans}')