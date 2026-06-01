class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        map = {}
        ETAs = []

        for i in range(len(speed)):
            map[position[i]] = speed[i]

        position.sort()

        for i in range(1, len(position)+1):
            s = map[position[-i]]
            time = (target - position[-i]) / s

            if ETAs:
                ETAs.append(max(time, ETAs[-1]))
            else:
                ETAs.append(time)

        print(ETAs)
        ETAs = set(ETAs)

        return len(ETAs)

