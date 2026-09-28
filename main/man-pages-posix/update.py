pattern = r"man-pages-posix-([\d\-a-z]+).tar.xz"
url = "https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/man-pages-posix"


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", ""), self.fetch_versions(src))
