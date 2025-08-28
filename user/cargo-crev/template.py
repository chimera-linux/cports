pkgname = "cargo-crev"
pkgver = "0.26.5"
pkgrel = 0
build_wrksrc = "cargo-crev"
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl3-devel", "libgit2-devel", "rust-std", "sqlite-devel"]
pkgdesc = "Cryptographically verifiable code review system for cargo"
license = "MPL-2.0 OR MIT OR Apache-2.0"
url = "https://github.com/crev-dev/cargo-crev"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9bf1ec351c15243c598db86b8edc292fb36b9deb8c4e94dd5506abf3edd5a41a"
# takes forever to run literally 2 unittests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
