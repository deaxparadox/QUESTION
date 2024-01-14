
class Solution:
    def check_path(self, path: list[str]) -> bool:
        for c in path:
            if (c == '.') or (c == '..'):
                return False
        return True
    def simplifyPath(self, path: str) -> str:
        path_split_slash = path.split('/')
        pre: str = ''
        for i in range(len(path_split_slash)):
            if i == 0:
                pre == path_split_slash[0]
            if path_split_slash[i] == '/' and pre == path_split_slash[i]:
                path_split_slash[0] = ''

        path_split_slash = [x for x in path_split_slash if (x != "")]
        path_split_slash = [x for x in path_split_slash if (x != '.')]
        print(path_split_slash)
        if len(path_split_slash) == 0: return '/'
        if len(path_split_slash) == 1 and (path_split_slash[0] == '..' or path_split_slash[0] == '/'):
            return "/"
        while True:
            if self.check_path(path_split_slash): break
            for i in range(len(path_split_slash)):
                # if the current path is "..", replace previous path with ""
                if (path_split_slash[i] == '..' and i > 0):
                    path_split_slash[i-1] = ''
                    path_split_slash[i] = ''
                    break
                if (path_split_slash[i] == '..' and i == 0):
                    path_split_slash[i] = ''
                    break
                print(path_split_slash)
            path_split_slash = [x for x in path_split_slash if x != ""]
        return "/" + "/".join(path_split_slash)

        
def main():
    s = Solution()
    paths = [
        # "/home/", 
        # "/../", 
        # "/home//foo/", 
        # "//",
        # "/a/./b/../../c/",
        "/a/../../b/../c//.//"
    ]
    for p in paths: 
        print("orginal path: {:<20}\tcorrect: {}".format(p, s.simplifyPath(p)))


if __name__ == "__main__":
    main()