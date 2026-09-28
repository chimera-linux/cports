pkgname = "cicada"
pkgver = "1.2.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = [
    "rust-std",
    "sqlite-devel",
]
checkdepends = [
    "bash",
    "less",
]
pkgdesc = "Bash-like Unix shell"
license = "MIT"
url = "https://github.com/mitnk/cicada"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "64e2c42b800dd7ea502ffd4eb9a99d4c5e4d40bf354d7d2e1f9aae5eafda04e6"
# Needs exact matching coreutils command output
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_shell("/usr/bin/cicada")
