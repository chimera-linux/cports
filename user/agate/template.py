pkgname = "agate"
pkgver = "3.3.17"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std"]
checkdepends = ["openssl3-devel"]
pkgdesc = "Server for the Gemini Protocol"
license = "Apache-2.0 OR MIT"
url = "https://github.com/mbrubeck/agate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "51d9eb747adfa125d1b19db4e94e235455524547961cdbfbac19f32943e454ff"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/agate")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_sysusers("^/sysusers.conf")
    self.install_license("LICENSE-MIT")
