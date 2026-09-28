pkgname = "agate"
pkgver = "3.3.24"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std"]
checkdepends = ["openssl3-devel"]
pkgdesc = "Server for the Gemini Protocol"
license = "Apache-2.0 OR MIT"
url = "https://github.com/mbrubeck/agate"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8776f2d7fe9155149cefd1151b43171ca307eb7b6eb5050221d73a4cefef5db0"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "agate"))
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_license("LICENSE-MIT")
