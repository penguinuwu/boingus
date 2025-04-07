class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []

        for p in path.split("/"):
            if p == "" or p == ".":
                continue
            elif p == "..":
                if result:
                    result.pop()
            else:
                result.append(p)

        return "/" + str.join("/", result)
