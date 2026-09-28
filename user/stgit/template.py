pkgname = "stgit"
pkgver = "2.6.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "asciidoc",
    "cargo-auditable",
    "perl",
    "pkgconf",
    "xmlto",
]
makedepends = [
    "openssl3-devel",
    "rust-std",
]
pkgdesc = "Manage git commits as a stack of patches"
license = "GPL-2.0-only"
url = "https://stacked-git.github.io"
source = (
    f"https://github.com/stacked-git/stgit/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "12d1af0f521a52bf66f173b9dd74658e5c126aab320180596c88f79f1f2ec0cd"
# generates completions with host bin
options = ["!cross"]


def post_build(self):
    from cbuild.util import cargo

    self.do("make", "-C", "Documentation", "man")
    for shell in ["bash", "fish"]:
        with open(self.cwd / f"stgit.{shell}", "w") as outf:
            self.do(
                cargo.target_path(self, "stg"),
                "completion",
                shell,
                stdout=outf,
            )


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "stg"))
    self.do(
        "make",
        "-C",
        "Documentation",
        "install-man",
        f"DESTDIR={self.chroot_destdir}",
        "man1dir=/usr/share/man/man1",
    )
    for shell in ["bash", "fish"]:
        self.install_completion(f"stgit.{shell}", shell, "stg")
    self.install_completion("completion/stgit.zsh", "zsh", "stg")
    self.install_file("contrib/stgit.el", "usr/share/emacs/site-lisp")
    self.install_file(
        "contrib/vim/ftdetect/stg.vim",
        "usr/share/vim/vimfiles/syntax/ftdetect",
    )
    self.install_file(
        "contrib/vim/syntax/*.vim",
        "usr/share/vim/vimfiles/syntax",
        glob=True,
    )


@subpackage("stgit-emacs")
def _(self):
    self.depends = [self.parent]
    self.subdesc = "emacs stgit"
    self.install_if = [self.parent, "emacs"]
    return ["usr/share/emacs"]


@subpackage("stgit-vim")
def _(self):
    self.depends = [self.parent]
    self.subdesc = "vim stgit"
    self.install_if = [self.parent, "vim"]
    return ["usr/share/vim"]
