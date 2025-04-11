pkgname = "tree-sitter-bash"
pkgver = "0.23.3"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "pkgconf",
    "tree-sitter-cli",
]
pkgdesc = "Bash grammar for tree-sitter"
license = "MIT"
url = "https://github.com/tree-sitter/tree-sitter-bash"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c682b81d0fe953d19f6632db3ba6e4f2db1efe1784f7a28bc5fcf6355d67335b"


def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/bash.so", "../libtree-sitter-bash.so.14"
    )


@subpackage("tree-sitter-bash-devel")
def _(self):
    return self.default_devel()
