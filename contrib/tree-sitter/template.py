pkgname = "tree-sitter"
pkgver = "0.22.5"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Parser generator tool and incremental parsing library"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "MIT"
url = "https://tree-sitter.github.io"
source = f"https://github.com/tree-sitter/tree-sitter/archive/v{pkgver}.tar.gz"
sha256 = "6bc22ca7e0f81d77773462d922cf40b44bfd090d92abac75cb37dbae516c2417"
# check requires cargo/fixture stuff (from remote repositories)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("tree-sitter-devel")
def _devel(self):
    return self.default_devel()
