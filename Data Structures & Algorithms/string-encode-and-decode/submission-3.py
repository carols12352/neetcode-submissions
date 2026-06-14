class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ''
        for i in strs:
            encoding = encoding + "`" + i
        return encoding
    def decode(self, s: str) -> List[str]:
        return s.split("`")[1:]