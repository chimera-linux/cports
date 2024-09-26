pkgname = "nushell"
pkgver = "0.98.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "openssl-devel",
    "rust-std",
    "sqlite-devel",
    "zstd-devel",
]
pkgdesc = "Shell with a focus on structured data"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://www.nushell.sh"
source = f"https://github.com/nushell/nushell/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c77fd63c4a5f2d35f7dcbb3e9bd76dfaa23acc6bc21fb1de4e7a4a94dc458839"


def post_install(self):
    self.install_shell("/usr/bin/nu")
    self.install_license("LICENSE")
