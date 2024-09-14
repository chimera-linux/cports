pkgname = "tree-sitter-markdown"
pkgver = "0.2.3"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
hostmakedepends = [
    "nodejs",
    "pkgconf",
    "tree-sitter-cli",
]
pkgdesc = "Markdown grammar for tree-sitter"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "MIT"
url = "https://github.com/tree-sitter-grammars/tree-sitter-markdown"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4909d6023643f1afc3ab219585d4035b7403f3a17849782ab803c5f73c8a31d5"


def configure(self):
    for x in ("tree-sitter-markdown", "tree-sitter-markdown-inline"):
        with self.pushd(x):
            self.do(
                "tree-sitter",
                "generate",
                "--no-bindings",
                env={"ALL_EXTENSIONS": "1"},
            )


def post_install(self):
    self.install_license("LICENSE")
    self.install_dir("usr/lib/tree-sitter")
    self.install_link(
        "usr/lib/tree-sitter/markdown.so",
        "../libtree-sitter-markdown.so.0",
    )
    self.install_link(
        "usr/lib/tree-sitter/inline_markdown.so",
        "../libtree-sitter-markdown-inline.so.0",
    )


@subpackage("tree-sitter-markdown-devel")
def _(self):
    return self.default_devel()
