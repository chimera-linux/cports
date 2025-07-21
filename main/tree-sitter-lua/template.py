pkgname = "tree-sitter-lua"
pkgver = "0.4.0"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "pkgconf",
    "tree-sitter-cli",
]
pkgdesc = "Lua grammar for tree-sitter"
license = "MIT"
url = "https://github.com/tree-sitter-grammars/tree-sitter-lua"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b0977aced4a63bb75f26725787e047b8f5f4a092712c840ea7070765d4049559"


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/lua.so", "../libtree-sitter-lua.so.15"
    )


@subpackage("tree-sitter-lua-devel")
def _(self):
    return self.default_devel()
