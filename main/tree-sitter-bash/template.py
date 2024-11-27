pkgname = "tree-sitter-bash"
pkgver = "0.21.0"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "pkgconf",
    "tree-sitter-cli",
]
pkgdesc = "Bash grammar for tree-sitter"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/tree-sitter/tree-sitter-bash"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f0515efda839cfede851adb24ac154227fbc0dfb60c6c11595ecfa9087d43ceb"


def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/bash.so", "../libtree-sitter-bash.so.0"
    )


@subpackage("tree-sitter-bash-devel")
def _(self):
    return self.default_devel()
