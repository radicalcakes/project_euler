from proj import triple
from proj import product

def gen(a,b):
    for n in a:
        for m in b:
            try: 
                sum(triple(m,n))
            except TypeError:
                continue
            else:
                if sum(triple(m,n)) == 1000:
                    return triple(m,n)


if __name__ == "__main__":
    print product(gen(range(1000),range(1000)))

    
