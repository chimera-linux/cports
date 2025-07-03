pkgname = "cargo-update"
pkgver = "16.3.2"
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
sha256 = "49e016c8189b779af4663c62c2b304f770e5a4358ed5348ae61e68bf3034a689"


def install(self):
    with self.pushd(f"target/{self.profile().triplet}/release"):
        self.install_bin("cargo-install-update")
        self.install_bin("cargo-install-update-config")
    self.install_license("LICENSE")
