pkgname = "nushell"
pkgver = "0.97.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["libgit2-devel", "openssl-devel", "sqlite-devel", "zstd-devel"]
pkgdesc = "Shell with a focus on structured data"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://www.nushell.sh"
source = f"https://github.com/nushell/nushell/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e605d5a7f104b7f2bf99197ca2f34a4a68f68cc12ecab41f606113e6a65b67b1"
# Checks fail with libgit2 < 1.8.1
options = ["!check"]


def post_install(self):
    self.install_shell("/usr/bin/nu")
    self.install_license("LICENSE")
