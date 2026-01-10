pkgname = "agate"
pkgver = "3.3.20"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std"]
checkdepends = ["openssl3-devel"]
pkgdesc = "Server for the Gemini Protocol"
license = "Apache-2.0 OR MIT"
url = "https://github.com/mbrubeck/agate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c5e98b4a93c24776b914983c9dc1c1e653fc443430106cd517cf586433b191a8"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/agate")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_sysusers("^/sysusers.conf")
    self.install_license("LICENSE-MIT")
