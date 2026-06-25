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
sha256 = "4061d2c27cae284259e542c607b0e588da5818acfff1ed6993aed69c5f5c1553"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/lappverk")
    self.install_license("LICENSE")
