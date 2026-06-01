class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "vErYsPeCiFiCcOmBiNaTiOn1"

        return "vErYsPeCiFiCcOmBiNaTiOn2".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "vErYsPeCiFiCcOmBiNaTiOn1":
            return []
        strs = s.split("vErYsPeCiFiCcOmBiNaTiOn2")
        
        return strs