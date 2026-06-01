class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "secretpassword"
        return " secretpassword ".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "secretpassword":
            return []
        
        return s.split(" secretpassword ")