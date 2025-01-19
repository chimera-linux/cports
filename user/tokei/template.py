pkgname = "tokei"
pkgver = "12.1.2"
pkgrel = 1
build_style = "cargo"
# we patch lockfile
prepare_after_patch = True
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "CLI for counting lines of code with stats per language"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/XAMPPRocky/tokei"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "81ef14ab8eaa70a68249a299f26f26eba22f342fb8e22fca463b08080f436e50"


def post_install(self):
    self.install_license("LICENCE-MIT")
