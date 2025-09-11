pkgname = "agate"
pkgver = "3.3.18"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std"]
checkdepends = ["openssl3-devel"]
pkgdesc = "Server for the Gemini Protocol"
license = "Apache-2.0 OR MIT"
url = "https://github.com/mbrubeck/agate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bfeda7e8bd8bcbbf3e84ac8bb36204841c9d79984767c4930b8c46c60c9d9b5b"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/agate")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_sysusers("^/sysusers.conf")
    self.install_license("LICENSE-MIT")
