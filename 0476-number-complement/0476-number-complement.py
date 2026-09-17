class Solution:
    def findComplement(self, num):
        bits = num.bit_length()
        mask = (1 << bits) - 1
        return num ^ mask