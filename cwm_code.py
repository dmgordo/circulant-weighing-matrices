from IPython.display import display, Markdown, Math

# show existence status for given parameters
def get_status(cwparams,n,s):
    C = cwparams[(cwparams['n']==n) & (cwparams['s']==s)]
    if len(C)==0:
        print(f'no information about CW({n},{s}^2) found in database')
    else:
        stat = C.iloc[0]["Status"]
        ref = C.iloc[0]["Reference"]
        if stat.find("All")>=0:
            print(f'All CW({n},{s}^2)s are known\nReference: {ref}')
        else:
            if stat.find("No")>=0:
                print(f'No CW({n},{s}^2)s exist\nReference: {ref}')
            else:
                if stat.find("Yes")>=0:
                    print(f'CW({n},{s}^2)s are known to exist\nReference: {ref}')
                else:
                    if stat.find("Open")>=0:
                        print(f'It is an open question whether CW({n},{s}^2)s exist\n')
                    else:
                        print('should not get here')

# show known CW(n,s^2)
def show(cwlist,n,s):
    C = cwlist[(cwlist['n']==n) & (cwlist['s']==s)]
    if len(C)==0:
        print(f'no $CW({n},{s}^2)$ found')
    else:
        if False:  # MyST output, which works in notebook but not book
            display(Markdown(
                rf"""
    ${len(C)} \ CW({n},{s}^2)$s in database
    """))
            for i in range(len(C)):
                display(Markdown(
                    rf"""
    $P: \{{ {C.iloc[i]["P"]} \}},\ \ \  $
    $N: \{{ {C.iloc[i]["N"]} \}}$
    """))
                ref = C.iloc[i]["Reference"]
                if len(ref)>1:
                    print(f'Reference:{C.iloc[i]["Reference"]}')
        else:  # basic output, to look better in Jupyter book
            print(f'{len(C)} CW({n},{s*s})s in database')
            for i in range(len(C)):
                print(f'P: {{{C.iloc[i]["P"]}}},\tN: {{{C.iloc[i]["N"]}}}')
                ref = C.iloc[i]["Reference"]
                if len(ref)>1:
                    print(f'Reference:{C.iloc[i]["Reference"]}')

# show known CW(n,s^2)
def get_cw(cwlist,n,s,num=0):
    C = cwlist[(cwlist['n']==n) & (cwlist['s']==s)]
    if len(C)<num:
        print(f'no such $CW({n},{s}^2)$ in database')
    else:
        return C.iloc[num]

# check that a CW(n,k) is valid
def is_cw(C):
    n = C['n']
    s = C['s']
    k = s*s
    P = [int(s) for s in C["P"].split(',')]
    N = [int(s) for s in C["N"].split(',')]

    diffs = [0]*n

    for a in P:
        for b in P:
            g = (a-b)%n
            diffs[g] += 1
    for a in N:
        for b in N:
            g = (a-b)%n
            diffs[g] += 1
    for a in P:
        for b in N:
            g = (a-b)%n
            diffs[g] -= 1
    for a in N:
        for b in P:
            g = (a-b)%n
            diffs[g] -= 1

    print(f'P = {P},')
    print(f'N = {N}\n')

    for g in range(1,n):
        if diffs[g] != 0:
            print(f'is not a CW({n},{s}^2)')
            return False

    print(f'is a CW({n},{s}^2)')
    return True



