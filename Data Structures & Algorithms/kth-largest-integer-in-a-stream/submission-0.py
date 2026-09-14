class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Store the position of the largest element we want
        self.k = k

        # Store all of the numbers
        self.arr = nums

    def add(self, val: int) -> int:
        # Add the new value to the array
        self.arr.append(val)

        # Sort the array in ascending order
        self.arr.sort()

        # The kth largest element is k positions from the end
        return self.arr[len(self.arr) - self.k]