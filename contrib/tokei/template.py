pkgname = "tokei"
pkgver = "12.1.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "CLI for counting lines of code with stats per language"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/XAMPPRocky/tokei"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "81ef14ab8eaa70a68249a299f26f26eba22f342fb8e22fca463b08080f436e50"


def do_prepare(self):
    # we patch the lockfile so vendor after patch
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("LICENCE-MIT")
