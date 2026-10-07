class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
      
        def is_valid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        level = {s}

        while level:
            valid = []

            for string in level:
                if is_valid(string):
                    valid.append(string)

            if valid:
                return valid

            next_level = set()

            for string in level:
                for i in range(len(string)):
                    if string[i] in "()":
                        next_level.add(string[:i] + string[i + 1:])

            level = next_level

        return [""]
        