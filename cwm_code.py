import pandas as pd
import numpy as np
import json

f = open('cwm.json','r')
cwm = json.load(f)
f.close()

print(f'read {len(cwm.keys())} data items\n')

# cwm is a python dictionary; each entry is the "name" of a set of parameters, e.g. "CW(28,4)"
# note that the second parameter is s, not k = s^2
# the dictionary entries contain 
#          "status": either "All", "Yes", "Open" or "No", (all known, exist, open, or known not to exist),
#          "comment": information about how the status is known,
#          "sets": a list of each known circulant weighing matrix

# these functions help to access the dictionary

#status of parameters
def get_status(D):
    if 'status' in cwm[D]:
        return cwm[D]['status']
    return None

def get_comment(D):
    if 'comment' in cwm[D]:
        return cwm[D]['comment']
    return None


# get number of CW(n,s) sets, if any
def num_sets(cw):
    if 'sets' not in cw:
        return 0
    return len(cw['sets'])

# pull parameters out from name D
def get_n(D):
    S = D.split(',')
    return int(S[0].split('(')[1])

def get_k(D):
    s = get_s(D)
    return s*s

def get_s(D):
    S = D.split(',')
    return int(S[1].split(')')[0])

def get_cwm(n,s,i):
    cwmname = f'CW({n},{s})'
    if cwmname not in cwm:
        print(f'{cwmname} not in database')
        return

    C = cwm[cwmname]
    if ('sets' not in C) or (len(C['sets']) <= i):
        print('no such set')
        return

    return [n,s,C['sets'][i][0],C['sets'][i][1]]

# print out information about a given CWM
def get_cwm_data(n,s):
    cwmname = f'CW({n},{s})'
    if cwmname not in cwm:
        print(f'{cwmname} not in database')
        return

    C = cwm[cwmname]
    if C['status']=="All":
        if num_sets(C)>1:
            print(f'There are exactly {num_sets(C)} CW({n},{s}^2)')
        else:
            print(f'There is exactly {num_sets(C)} CW({n},{s}^2)')

    if C['status']=="Yes":
        if num_sets(C)>1:
            print(f'There are at least {num_sets(C)} CW({n},{s}^2)')
        else:
            if num_sets(C)>0:
                print(f'There is at least {num_sets(C)} CW({n},{s}^2)')
            else:
                print(f'There is at least one CW({n},{s}^2), but it is not in this dataset')

    if C['status']=="No":
            print(f'No CW({n},{s}^2) exists')

    if 'comment' in C:
        print(f'Reference: {C["comment"]}')

    for i in range(num_sets(C)):
        cw = C['sets'][i]
        print(f'{i}:\tP = {cw[0]}, N = {cw[1]}')

    print()

# show all the CWM in the database (not existence results, just actual circulant weighing matrices)
def all_sets():
    for c in cwm:
        if cwm[c]["status"] in ["All","Yes"] and num_sets(cwm[c])>0:
            print(c)
            str = c.split(',')
            n = int(str[0].split('(')[1])
            s = int(str[1].split(')')[0])
            get_cwm_data(n,s)
            print('')


# make a table, along the lines of Strassler's table (and Tan's 2018 update)
# I'm ignoring trivial cases n=1 or s=1
def cwm_table():

    for n in range(1,1000):

        if (n%40)==1:
            print('\nn\\s ',end='')
            for s in range(2,20):
                print(f'{s:2d}  ',end='')
            print('')
            if n==1:
                continue

        print(f'{n:3d}  ',end='')
        for s in range(2,20):
            cwmname = f'CW({n},{s})'
            if cwmname not in cwm:
                print('.   ',end='')
            else:
                status = cwm[cwmname]['status']
                if status=="All" or status=="Yes":
                    print('Y   ',end='')
                if status=="No":
                    print('.   ',end='')
                if status=="Open":
                    print('*   ',end='')
        print('')


# code to create tables for showing a list of circulant weighing matrices
def init_tab():
    T = {}
    T['n'] = []
    T['s'] = []
    T['k'] = []
    T['status'] = []
    T['comment'] = []
    return T

def add_tab_entry(T,M):
    n = int(M.split(',')[0].split('(')[1])
    s = int(M.split(',')[1].split(')')[0])
    k = s*s
    T['n'] += [n]
    T['s'] += [s]
    T['k'] += [k]
    T['status'] += [cwm[M]['status']]
    T['comment'] += [cwm[M]['comment']]

def show_tab(T):
    df = pd.DataFrame(T)
    df = df.style.hide(axis='index')
    return df


# simple-minded test to verify that M is a circulant weighing matrix
# there are much nicer ways to do it in Sage, but I'm keeping this
# repo to only minimal python code
def is_cwm(M):

    n = M[0]
    s = M[1]
    k = s*s
    P = M[2]
    N = M[3]

    A = [0]*n 

    for s1 in P:
        for s2 in P:
            s = (s1-s2) % n
            A[s] += 1

    for s1 in N:
        for s2 in N:
            s = (s1-s2) % n
            A[s] += 1

    for s1 in P:
        for s2 in N:
            s = (s1-s2) % n
            A[s] -= 1

    for s1 in N:
        for s2 in P:
            s = (s1-s2) % n
            A[s] -= 1

    if A[0] != k:
        return False
    for g in range(1,n):
        if A[g] != 0:
            return False
    return True


    
