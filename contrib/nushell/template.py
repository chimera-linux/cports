pkgname = "nushell"
pkgver = "0.96.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["libgit2-devel", "openssl-devel", "sqlite-devel", "zstd-devel"]
pkgdesc = "Shell with a focus on structured data"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://www.nushell.sh"
source = f"https://github.com/nushell/nushell/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "829e2f91d130d7b0063a08b1fadb737bdff616ac744eba43baa5fc42aa8b682b"
# Checks fail with libgit2 < 1.8.1
options = ["!check"]


def post_install(self):
    self.install_shell("/usr/bin/nu")
    self.install_license("LICENSE")
