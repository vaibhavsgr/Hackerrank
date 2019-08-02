all_paths = []

def findPaths(matrix, m, n):
    path = [0 for d in range(m+n-1)]
    findPathsUtil(matrix, m, n, 0, 0, path,  0)


def findPathsUtil(matrix, m, n, i, j, path, index):

    if i == m-1:
        for k in range(j, n):
            #path[index+k-j] = matrix[i][k]
            path.append(matrix[i][k])

        print (path)
        all_paths.append(path)
        return

    if j == n-1:
        for k in range(i, m):
            path.append(matrix[k][j])

        print (path)
        all_paths.append(path)
        return



if __name__ == "__main__":
    matrix = [[1,2,3],
            [4,5,6],
            [7,8,9]]

    findPaths(matrix, 3, 3)
