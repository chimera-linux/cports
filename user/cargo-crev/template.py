pkgname = "cargo-crev"
pkgver = "0.26.2"
pkgrel = 0
build_wrksrc = "cargo-crev"
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl-devel", "libgit2-devel", "rust-std", "sqlite-devel"]
pkgdesc = "Cryptographically verifiable code review system for cargo"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MPL-2.0 OR MIT OR Apache-2.0"
url = "https://github.com/crev-dev/cargo-crev"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b2204510acf65667418980dc6e93580167e738376ee888f810064542fa04ef92"
# takes forever to run literally 2 unittests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
