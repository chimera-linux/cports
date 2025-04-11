pkgname = "tree-sitter-lua"
pkgver = "0.3.0"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "tree-sitter-cli",
    "pkgconf",
]
pkgdesc = "Lua grammar for tree-sitter"
license = "MIT"
url = "https://github.com/tree-sitter-grammars/tree-sitter-lua"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a34cc70abfd8d2d4b0fabf01403ea05f848e1a4bc37d8a4bfea7164657b35d31"


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/lua.so", "../libtree-sitter-lua.so.14"
    )


@subpackage("tree-sitter-lua-devel")
def _(self):
    return self.default_devel()
