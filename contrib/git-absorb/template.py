pkgname = "git-absorb"
pkgver = "0.6.12"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "pkgconf", "asciidoc"]
makedepends = ["libgit2-devel"]
pkgdesc = "Automatic git commit --fixup; like hg absorb"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/tummychow/git-absorb"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "88a64712bcb4885a65984359c783e7f16b76fe4ca4ccd339d0c2d83139d0428b"


def do_prepare(self):
    # we patch the lockfile so vendor after patch
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_build(self):
    self.do("make", "-C", "Documentation")


def post_install(self):
    self.install_license("LICENSE.md")
    self.install_man("Documentation/git-absorb.1")
