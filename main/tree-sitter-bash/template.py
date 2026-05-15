pkgname = "tree-sitter-bash"
pkgver = "0.25.1"
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
sha256 = "2e785a761225b6c433410ef9c7b63cfb0a4e83a35a19e0f2aec140b42c06b52d"


def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/bash.so", "../libtree-sitter-bash.so.15"
    )


@subpackage("tree-sitter-bash-devel")
def _(self):
    return self.default_devel()
