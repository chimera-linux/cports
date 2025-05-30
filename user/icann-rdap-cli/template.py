pkgname = "icann-rdap-cli"
pkgver = "0.0.22"
pkgrel = 0
build_wrksrc = "icann-rdap-cli"
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl3-devel", "rust-std"]
pkgdesc = "CLI of the ICANN implementation of RDAP"
license = "Apache-2.0 OR MIT"
url = "https://github.com/icann/icann-rdap"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "42360a82605bf92891b4de0a133d43baabb041446b16063094c4abc94c531c30"


def install(self):
    self.install_bin(f"../target/{self.profile().triplet}/release/rdap")
    self.install_bin(f"../target/{self.profile().triplet}/release/rdap-test")
    self.install_license("../LICENSE-APACHE")
