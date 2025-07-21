pkgname = "tree-sitter-bash"
pkgver = "0.25.0"
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
sha256 = "9d6bad618e712b51ff060515b0ce6872e33727148f35becb8aa3ad80044c2348"


def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/bash.so", "../libtree-sitter-bash.so.15"
    )


@subpackage("tree-sitter-bash-devel")
def _(self):
    return self.default_devel()
