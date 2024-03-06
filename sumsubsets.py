def subsets_sum(arr, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(arr)):
            if arr[i] > target:
                continue
            backtrack(i + 1, target - arr[i], path + [arr[i]])

    result = []
    arr.sort()
    backtrack(0, target, [])
    return result


arr = [2, 4, 6, 8]
target = 8
print("Subsets with sum", target, "are:")
print(subsets_sum(arr, target))
