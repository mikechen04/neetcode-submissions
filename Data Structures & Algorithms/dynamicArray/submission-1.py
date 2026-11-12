class DynamicArray:
    
    def __init__(self, capacity: int):
        array = [capacity]

    def get(self, i: int) -> int:
        return array[i]

    def set(self, i: int, n: int) -> None:
        return array[i] == array[n]

    def pushback(self, n: int) -> None:
        return array[n].push()

    def popback(self) -> int:
        array[:-1].pop()
        return array[:-1]

    def resize(self) -> None:
        capacity *= 2

    def getSize(self) -> int:
        return len(array)
    
    def getCapacity(self) -> int:
        return capacity