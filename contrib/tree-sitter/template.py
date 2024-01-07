pkgname = "tree-sitter"
pkgver = "0.20.8"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Parser generator tool and incremental parsing library"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "MIT"
url = "https://tree-sitter.github.io"
source = f"https://github.com/tree-sitter/tree-sitter/archive/v{pkgver}.tar.gz"
sha256 = "6181ede0b7470bfca37e293e7d5dc1d16469b9485d13f13a605baec4a8b1f791"
# check requires cargo/fixture stuff (from remote repositories)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("tree-sitter-devel")
def _devel(self):
    return self.default_devel()
