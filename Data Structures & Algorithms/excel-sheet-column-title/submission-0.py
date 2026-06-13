class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 0:
            return ""
        else:
            n = columnNumber - 1
            return self.convertToTitle(n // 26) + chr(n % 26 + ord('A'))