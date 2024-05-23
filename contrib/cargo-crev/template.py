pkgname = "cargo-crev"
pkgver = "0.25.9"
pkgrel = 0
build_wrksrc = "cargo-crev"
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl-devel", "libgit2-devel", "sqlite-devel"]
pkgdesc = "Cryptographically verifiable code review system for cargo"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MPL-2.0 OR MIT OR Apache-2.0"
url = "https://github.com/crev-dev/cargo-crev"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7ebc63b272f09730d44c469d39413e3208538e885cf977bf4a61d768948700a2"


def post_install(self):
    self.install_license("LICENSE-MIT")
