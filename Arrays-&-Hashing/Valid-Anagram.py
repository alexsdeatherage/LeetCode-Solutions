class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if len(s) == len(t). If not, return False
        if len(s) != len(t):
            return False

        # Init sMap and tMap as dicts
        sMap = dict()
        tMap = dict()

        # Use for loop for s, t, to add char freq to dicts
        for c in s:
            if c not in sMap:
                sMap[c] = 1
            else:
                sMap[c] += 1

        for c in t:
            if c not in tMap:
                tMap[c] = 1
            else:
                tMap[c] += 1

        # Compare dicts. If equal, return True
        return sMap == tMap