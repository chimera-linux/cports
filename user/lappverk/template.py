pkgname = "lappverk"
pkgver = "0.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "libgit2-devel",
    "openssl3-devel",
    "rust-std",
]
pkgdesc = "Tool for modifying other people's software"
license = "Apache-2.0"
url = "https://codeberg.org/natkr/lappverk"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "2204079b632d4832dcda42f796a49515b1b7cb68005551f65d8f2522852ac8d7"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/lappverk")
    self.install_license("LICENSE")
