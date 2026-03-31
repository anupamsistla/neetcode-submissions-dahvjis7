class Solution:
    def isValid(self, s: str) -> bool:
        track = []
        for c in s:
            if c == '(':
                track.append(')')
            elif c == '{':
                track.append('}')
            elif c == '[':
                track.append(']')
            elif c not in track:
                return False
            elif track[-1] == c:
                track.pop()
        return len(track) ==0