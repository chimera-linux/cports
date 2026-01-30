pkgname = "tree-sitter-lua"
pkgver = "0.4.1"
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
sha256 = "cef44b8773bde69d427b5e50ca95e417c86c0be91caa37a6782c90d6f529da70"


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/lua.so", "../libtree-sitter-lua.so.15"
    )


@subpackage("tree-sitter-lua-devel")
def _(self):
    return self.default_devel()
