pkgname = "cargo-update"
pkgver = "16.3.0"
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
sha256 = "f6a87615d72db3f1068aef2ad383813a96238c4963f6498c675c555a32e95bd3"


def post_install(self):
    self.install_license("LICENSE")
