"""Browse and verify the circulant weighing matrix database.

Requires only Python's standard library. Database keys CW(n,s) denote
mathematical CW(n,s**2); stored representatives are [P,N] support pairs.
Place cwm.json alongside this module.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / 'cwm.json'
with DATA_FILE.open(encoding='utf-8') as f:
    cwm = json.load(f)
print(f'read {len(cwm)} data items\n')


def get_status(D):
    return cwm[D].get('status')


def get_comment(D):
    return cwm[D].get('comment')


def num_sets(cw):
    """Number of representatives in a database entry (not necessarily exhaustive)."""
    return len(cw.get('sets', []))


def get_n(D):
    return int(D.split(',')[0].split('(')[1])


def get_s(D):
    return int(D.split(',')[1].split(')')[0])


def get_k(D):
    return get_s(D) ** 2


def get_cwm(n, s, i):
    """Return representative i as [n,s,P,N], or None if unavailable."""
    name = f'CW({n},{s})'
    if name not in cwm:
        print(f'{name} not in database')
        return None
    sets = cwm[name].get('sets', [])
    if not isinstance(i, int) or not 0 <= i < len(sets):
        print('no such set')
        return None
    return [n, s, sets[i][0], sets[i][1]]


def get_cwm_data(n, s):
    """Print status and recorded representatives for CW(n,s**2)."""
    name = f'CW({n},{s})'
    if name not in cwm:
        print(f'{name} not in database')
        return
    entry = cwm[name]
    count = num_sets(entry)
    status = entry.get('status')
    label = f'CW({n},{s**2})'
    if status == 'All':
        if count==1:
            print(f'{label} exists and is unique up to equivalence.')
        else:
            print(f'{label} exists: there are exactly {count} inequivalent representatives.')
    elif status == 'Yes':
        if count==0:
            print(f'{label} exists, but no representative is recorded here.')
        if count==1:
            print(f'{label} exists: {count} representative known.')
        if count>1:
            print(f'{label} exists: {count} representatives known.')
    elif status == 'No':
        print(f'No {label} exists.')
    elif status == 'Open':
        print(f'Existence of {label} remains open.')
    else:
        print(f'{label}: unrecognized or missing status {status!r}.')
    if entry.get('comment'):
        print(f'Reference: {entry["comment"]}')
    for i, (P, N) in enumerate(entry.get('sets', [])):
        print(f'{i}:\tP = {P}, N = {N}')
    print()


def all_sets():
    """Print entries that include at least one recorded representative."""
    for name, entry in cwm.items():
        if num_sets(entry) > 0:
            get_cwm_data(get_n(name), get_s(name))


def cwm_table():
    """Print the n<1000, 2<=s<20 status table.

    Y: recorded Yes/All; .: recorded No; *: recorded Open;
    """
    for n in range(2, 1000):
        if (n - 1) % 40 == 0 or n == 2:
            print('\nn\\s ' + ''.join(f'{s:2d}  ' for s in range(2, 20)))
        print(f'{n:3d}  ', end='')
        for s in range(2, 20):
            entry = cwm.get(f'CW({n},{s})')
            status = entry.get('status') if entry is not None else None
            if n < s*s:
                status = 'No'
            symbol = {'All': 'Y', 'Yes': 'Y', 'No': '.', 'Open': '*'}.get(status, '?')
            print(f'{symbol}   ', end='')
        print()


def init_tab():
    return {'n': [], 's': [], 'k': [], 'status': [], 'comment': []}


def add_tab_entry(T, M):
    n, s = get_n(M), get_s(M)
    T['n'].append(n)
    T['s'].append(s)
    T['k'].append(s * s)
    T['status'].append(cwm[M].get('status'))
    T['comment'].append(cwm[M].get('comment', ''))


def show_tab(T):
    """Return a styled pandas table if available, otherwise rows as dicts."""
    try:
        import pandas as pd
    except ImportError:
        return [dict(zip(T, row)) for row in zip(*(T[key] for key in T))]
    return pd.DataFrame(T).style.hide(axis='index')


def is_cwm(M):
    """Verify CW(n,s**2) for [n,s,P,N], including valid disjoint supports.

    The signs may be reversed, so |P|-|N| may be +s or -s.
    """
    if M is None:
        return False
    try:
        n, s, P, N = M
        if type(n) is not int or type(s) is not int or n <= 0 or s <= 0:
            return False
        P, N = list(P), list(N)
        positions = P + N
        if any(type(x) is not int or x < 0 or x >= n for x in positions):
            return False
        if len(set(positions)) != len(positions):
            return False
        if len(positions) != s*s or abs(len(P)-len(N)) != s:
            return False
        a = [0] * n
        for x in P:
            a[x] = 1
        for x in N:
            a[x] = -1
        for shift in range(1, n):
            if sum(a[j]*a[(j+shift) % n] for j in range(n)) != 0:
                return False
        return True
    except (TypeError, ValueError):
        return False
