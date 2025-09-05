pkgname = "i3wsr"
pkgver = "3.1.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Sway/i3 workspace renamer"
license = "MIT"
url = "https://github.com/roosta/i3wsr"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0853f1c712d4d4622f7dc7c4eaf10243d06ca1cb1566cf896c957b135f0cb71a"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/i3swr")
    self.install_license("LICENSE")
