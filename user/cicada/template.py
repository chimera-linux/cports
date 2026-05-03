pkgname = "cicada"
pkgver = "1.1.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = [
    "rust-std",
    "sqlite-devel",
]
checkdepends = [
    "less",
]
pkgdesc = "Bash-like Unix shell"
license = "MIT"
url = "https://github.com/mitnk/cicada"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fa98e4b15d62ce0343d69a9f51d737fe02b8200f5903c14f5131dec6c7a54656"
# Needs exact matching coreutils command output
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_shell("/usr/bin/cicada")
