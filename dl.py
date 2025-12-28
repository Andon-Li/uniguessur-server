'''algorithm DL-distance is
    input: strings a[1..length(a)], b[1..length(b)]
    output: distance, integer
    
    da := new array of |Σ| integers
    for i := 1 to |Σ| inclusive do
        da[i] := 0
    
    let d[-1..length(a), -1..length(b)] be a 2-d array of integers, dimensions length(a)+2, length(b)+2
    // note that d has indices starting at -1, while a, b and da are one-indexed.
    
    maxdist := length(a) + length(b)
    d[-1, -1] := maxdist
    for i := 0 to length(a) inclusive do
        d[i, -1] := maxdist
        d[i, 0] := i
    for j := 0 to length(b) inclusive do
        d[-1, j] := maxdist
        d[0, j] := j
    
    for i := 1 to length(a) inclusive do
        db := 0
        for j := 1 to length(b) inclusive do
            k := da[b[j]]
            ℓ := db
            if a[i] = b[j] then
                cost := 0
                db := j
            else
                cost := 1
            d[i, j] := minimum(d[i-1, j-1] + cost,  //substitution
                               d[i,   j-1] + 1,     //insertion
                               d[i-1, j  ] + 1,     //deletion
                               d[k-1, ℓ-1] + (i-k-1) + cost + (j-ℓ-1)) //transposition
        da[a[i]] := i
    return d[length(a), length(b)]'''

# Translated from Wikipedia psudocode

# alphabet: size of alphabet
def distance(a: str, b: str, alphabet=26) -> int:

    # Long input strings result in relatively expensive computation
    if len(a) > 100 or len(b) > 100:
        raise ValueError('Damerau-Levenshtein distance strings exceeded 100 characters.')
    
    da = [0]*alphabet

    d = [[0]*(len(a)+2)]*(len(b)+2)

    maxdist = len(a)+len(b)

    d[0][0] = maxdist

    for i in range(1, len(a)+2):
        d[i][0] = maxdist
        d[i][1] = 1
    
    for i in range(1, len(b)+2):
        d[0][i] = maxdist
        d[1][i] = i

    for i in range(2, len(a)+2):
        db = 0
        for j in range(2, len(b)+2):
            k = da[b[j-2]]
            l = db
            if a[i-2] == b[j-2]:
                cost = 0
                db = j
            else:
                cost = 1
            d[i][j] = min(d[i-1][j-1] + cost,  # substitution
                            d[i][j-1] + 1,  # insertion
                            d[i-1][j] + 1,  # deletion
                            d[k-1][l-1] + (i-k-1) + cost + (j-l-1))  # transposition
        da[a[i-2]] = i
    return d[len(a)+2][len(b)+2]

