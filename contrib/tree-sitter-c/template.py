pkgname = "tree-sitter-c"
pkgver = "0.21.4"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "tree-sitter-cli",
]
pkgdesc = "C grammar for tree-sitter"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/tree-sitter/tree-sitter-c"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "19194c47a6faf81509aea338b96dd9b59ffd8a7f26bce6487cf4275065433870"


def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link("usr/lib/tree-sitter/c.so", "../libtree-sitter-c.so.0")


@subpackage("tree-sitter-c-devel")
def _devel(self):
    return self.default_devel()
