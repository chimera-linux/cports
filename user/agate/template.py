pkgname = "agate"
pkgver = "3.3.23"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std"]
checkdepends = ["openssl3-devel"]
pkgdesc = "Server for the Gemini Protocol"
license = "Apache-2.0 OR MIT"
url = "https://github.com/mbrubeck/agate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b88dd2f7adeecef209675fbf83962a553dbf44441cb6cf8b8b094e0f0d55286d"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/agate")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_license("LICENSE-MIT")
