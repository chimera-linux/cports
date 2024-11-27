pkgname = "tree-sitter-lua"
pkgver = "0.1.0"
pkgrel = 1
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "tree-sitter-cli",
    "pkgconf",
]
pkgdesc = "Lua grammar for tree-sitter"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/tree-sitter-grammars/tree-sitter-lua"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "230cfcbfa74ed1f7b8149e9a1f34c2efc4c589a71fe0f5dc8560622f8020d722"


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/lua.so", "../libtree-sitter-lua.so.0"
    )


@subpackage("tree-sitter-lua-devel")
def _(self):
    return self.default_devel()
