pkgname = "cargo-crev"
pkgver = "0.25.6"
pkgrel = 0
build_wrksrc = "cargo-crev"
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl-devel", "libgit2-devel"]
pkgdesc = "Cryptographically verifiable code review system for cargo"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MPL-2.0 OR MIT OR Apache-2.0"
url = "https://github.com/crev-dev/cargo-crev"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8a8b737aff1361677e3733133944728871ccf7ac00ea15b32f9d0ef6d5814f62"


def post_install(self):
    self.install_license("LICENSE-MIT")
