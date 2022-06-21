"""# Devuelve verdadero si existe una sublista de la lista `nums[0…n)` con la suma dada
def subsetSum(nums, total):
    n = len(nums)

    # `T[i][j]` almacena verdadero si se puede obtener un subconjunto con la suma `j`
    # utilizando elementos hasta los primeros elementos `i`
    T = [[False for x in range(total + 1)] for y in range(n + 1)]

    # si la suma es cero
    for i in range(n + 1):
        T[i][0] = True

    # hacer por i-ésimo artículo
    for i in range(1, n + 1):

        # considera todas las sumas desde 1 hasta el total
        for j in range(1, total + 1):

            # no incluye el i-ésimo elemento si `j-nums[i-1]` es negativo
            if nums[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                # encuentre el subconjunto con la suma `j` excluyendo o incluyendo el i-ésimo elemento
                T[i][j] = T[i - 1][j] or T[i - 1][j - nums[i - 1]]

    # valor máximo de retorno
    for i in T:
        print(i)
    return T[n][total]


# Devuelve verdadero si la lista dada `nums[0…n-1]` se puede dividir en dos
# sublistas con igual suma
def partition(nums):
    total = sum(nums)

    # devuelve verdadero si la suma es par y la lista se puede dividir en
    # dos sublistas con igual suma
    return (total & 1) == 0 and subsetSum(nums, total // 2)


if __name__ == '__main__':

    # Entrada #: un conjunto de elementos
    nums = [1, 20, 3, 9, 2, 11, 4]

    if partition(nums):
        print('Set can be partitioned')
    else:
        print('Set cannot be partitioned')
"""


def isSubsetSum(arr, n, sum, dp):
    # Base Cases
    if (sum == 0):
        return True
    if (n == 0 and sum != 0):
        return False

    # return solved subproblem
    if (dp[n][sum] != -1):
        return dp[n][sum]

    # If last element is greater than sum, then
    # ignore it
    if (arr[n - 1] > sum):
        return isSubsetSum(arr, n - 1, sum, dp)

        # else, check if sum can be obtained by any of
        # the following
        # (a) including the last element
        # (b) excluding the last element

    # also store the subproblem in dp matrix
    dp[n][sum] = isSubsetSum(arr, n - 1, sum, dp) or isSubsetSum(arr, n - 1, sum - arr[n - 1], dp)
    """for i in dp:
        print(i)"""
    return dp[n][sum]


# Returns true if arr[] can be partitioned in two
# subsets of equal sum, otherwise false
def findPartiion(arr, n):
    # Calculate sum of the elements in array
    sum = 0
    for i in range(n):
        sum += arr[i]

    # If sum is odd, there cannot be two subsets
    # with equal sum
    if (sum % 2 != 0):
        return False

    # To store overlapping subproblems
    dp = [[-1] * (sum + 1)] * (n + 1)
    print(dp)

    # Find if there is subset with sum equal to
    # half of total sum
    return isSubsetSum(arr, n, sum // 2, dp)


# Driver code

arr = [1, 20, 3, 9, 2, 11, 4]
n = len(arr)

# Function call
if (findPartiion(arr, n) == True):
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")

