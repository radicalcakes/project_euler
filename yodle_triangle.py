# use dynamic programming to find shortest path
def find_sum(triangle):
    index = len(triangle) - 2
    for x in xrange(index, -1, -1):
        for y in xrange(0, x+1):
            triangle[x][y] += max(triangle[x + 1][y], triangle[x + 1][y + 1])
            # a + max(b,c)
    return triangle[x][y]



if __name__ == "__main__":
    text = open("triangle_yodle.txt", "r")
    triangle = []
    for line in text:
        triangle.append([int(num) for num in line.split()])
    print find_sum(triangle)
