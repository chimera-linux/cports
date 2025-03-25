pkgname = "agate"
pkgver = "3.3.14"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl3-devel", "rust-std"]
pkgdesc = "Simple server for the Gemini Protocol"
license = "Apache-2.0 OR MIT"
url = "https://github.com/mbrubeck/agate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1e283fa544468fd67046e593c63c8ad01ae832462653b2c9b97eaed791954f7e"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/agate")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-APACHE")
