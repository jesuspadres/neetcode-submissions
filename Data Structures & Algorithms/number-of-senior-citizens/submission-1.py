class Solution:
    def countSeniors(self, details: List[str]) -> int:
        retVal = 0

        #details = set(details)

        for det in details:
            age = det[11:13]

            if age.isnumeric() and int(age) > 60:
                retVal += 1

        return retVal