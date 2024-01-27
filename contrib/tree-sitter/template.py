pkgname = "tree-sitter"
pkgver = "0.20.9"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Parser generator tool and incremental parsing library"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "MIT"
url = "https://tree-sitter.github.io"
source = f"https://github.com/tree-sitter/tree-sitter/archive/v{pkgver}.tar.gz"
sha256 = "9b2fd489a7281e3a7e5e7cbbf3a974e5a6a115889ae65676d61b79bdae96464e"
# check requires cargo/fixture stuff (from remote repositories)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("tree-sitter-devel")
def _devel(self):
    return self.default_devel()
