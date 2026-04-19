pkgname = "cargo-update"
pkgver = "20.0.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "curl-devel",
    "libgit2-devel",
    "libssh2-devel",
    "rust-std",
]
pkgdesc = "Cargo subcommand for updating installed executables"
license = "MIT"
url = "https://github.com/nabijaczleweli/cargo-update"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7e9898ae686fe64c4cf75be5c4e9e6d5f6141371182a12e4bdaa806cfe321806"


def install(self):
    with self.pushd(f"target/{self.profile().triplet}/release"):
        self.install_bin("cargo-install-update")
        self.install_bin("cargo-install-update-config")
    self.install_license("LICENSE")
