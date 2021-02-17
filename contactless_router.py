import numpy as np
from itertools import permutations
def total_dist(route,coords):
    d=0
    for i in range(len(route)-1): d+=np.linalg.norm(coords[route[i]]-coords[route[i+1]])
    return d
def nearest_neighbor(depot,customers,coords):
    route=[depot]; remaining=list(customers)
    while remaining:
        last=route[-1]; nearest=min(remaining,key=lambda c:np.linalg.norm(coords[last]-coords[c]))
        route.append(nearest); remaining.remove(nearest)
    route.append(depot)
    return route
def two_opt(route,coords):
    improved=True
    while improved:
        improved=False
        for i in range(1,len(route)-2):
            for j in range(i+1,len(route)-1):
                new=route[:i]+route[i:j+1][::-1]+route[j+1:]
                if total_dist(new,coords)<total_dist(route,coords):
                    route=new; improved=True
    return route
if __name__=="__main__":
    np.random.seed(42); n=10
    coords=np.vstack([np.array([0,0]),np.random.rand(n,2)*100])
    r=nearest_neighbor(0,list(range(1,n+1)),coords)
    r=two_opt(r,coords)
    print(f"Route: {r}, Dist: {total_dist(r,coords):.1f}")
