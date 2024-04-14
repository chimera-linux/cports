pkgname = "tree-sitter"
pkgver = "0.22.4"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Parser generator tool and incremental parsing library"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "MIT"
url = "https://tree-sitter.github.io"
source = f"https://github.com/tree-sitter/tree-sitter/archive/v{pkgver}.tar.gz"
sha256 = "919b750da9af1260cd989498bc84c63391b72ee2aa2ec20fc84882544eb7a229"
# check requires cargo/fixture stuff (from remote repositories)
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("tree-sitter-devel")
def _devel(self):
    return self.default_devel()
