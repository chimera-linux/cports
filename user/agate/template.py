pkgname = "agate"
pkgver = "3.3.19"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std"]
checkdepends = ["openssl3-devel"]
pkgdesc = "Server for the Gemini Protocol"
license = "Apache-2.0 OR MIT"
url = "https://github.com/mbrubeck/agate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b820b56463bcc335e57c565c23db3aa4f8dc06f3131a5d7ce77407fe783fd3be"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/agate")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_sysusers("^/sysusers.conf")
    self.install_license("LICENSE-MIT")
