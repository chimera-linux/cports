pkgname = "cargo-update"
pkgver = "18.0.0"
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
sha256 = "cfa56d6c5fb2d7d1536efb4765031731fe70bf1a8246757a7a9d6a4a046e640f"


def install(self):
    with self.pushd(f"target/{self.profile().triplet}/release"):
        self.install_bin("cargo-install-update")
        self.install_bin("cargo-install-update-config")
    self.install_license("LICENSE")
