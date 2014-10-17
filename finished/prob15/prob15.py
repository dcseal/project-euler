def lattice_path(n,m):
    """Compute the shortest path on an nxm lattice."""
   
    # base case:
    if( n==0 or m==0 ):
        return 1

    # WLOG, may assume n < m:
    if( n == m ):
        return 2*lattice_path(n-1,m)
    else:
        return lattice_path(n-1,m) + lattice_path(n,m-1)

#   return lattice_path(n-1,m) + lattice_path(n,m-1)

#print( lattice_path(20,20) )
