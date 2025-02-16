pkgname = "liblsdj"
pkgver = "2.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "LSDj save format tools"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://github.com/stijnfrishert/liblsdj"
_catch2_commit = "42e368dd0aedc122798008d8c4f583fea3296a97"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/catchorg/Catch2/archive/{_catch2_commit}.tar.gz",
]
source_paths = [".", "dependency/Catch2"]
sha256 = [
    "74688fca65aa044fb4c8d1211ef013ef7d4fd2ead22b4b075defb0a644e26617",
    "51f4dcc029c08753a6360b61e8b3d8eee7e34f7c227a949688f5a3b10eebc04e",
]


def check(self):
    self.do("build/liblsdj/test/test")


def post_install(self):
    self.install_license("LICENSE")


@subpackage("liblsdj-devel")
def _(self):
    return self.default_devel()
