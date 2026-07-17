class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        n = len(s)
        decoded = []
        i = 0
        while i < n:
            # print(decoded)
            size = ''
            j = i
            while s[j] != '#':
                size += s[j]
                j += 1
            i = j+1
            decoded.append(s[i:i+int(size)])
            i += int(size)
        return decoded
            
