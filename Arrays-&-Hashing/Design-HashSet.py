# input: positive numbers
# output: either null or True/False
# if we add number 5 three times, set will be [5]
# if remove 3, does nothing. If remove 5, set will be []

class MyHashSet:

    def __init__(self):
        self.array = []

    def add(self, key: int) -> None:
        # Use contains method. If inside, return Nothing. If not, append to array
        if not self.contains(key):
            self.array.append(key)

    def remove(self, key: int) -> None:
        # Use contains method to check if element in array. If so, remove element
        if self.contains(key):
            self.array.remove(key)

    def contains(self, key: int) -> bool:
        # if number inside of array, return True. False otherwise
        if key in self.array:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)