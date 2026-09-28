url = "https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc"
pattern = r"(\d+)\.[0-9a-f]{7}"


def fetch_versions(self, src):
    return map(lambda v: f"0_git{v}", self.fetch_versions(src))
