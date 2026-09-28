pkgname = "cargo-crev"
pkgver = "0.27.1"
pkgrel = 0
build_wrksrc = "cargo-crev"
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl3-devel", "libgit2-devel", "rust-std", "sqlite-devel"]
pkgdesc = "Cryptographically verifiable code review system for cargo"
license = "MPL-2.0 OR MIT OR Apache-2.0"
url = "https://github.com/crev-dev/cargo-crev"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "785ed01f3352331ac4f6ecd63da5ab896a4d251678ad75b6bcf1545858a4cc82"
# takes forever to run literally 2 unittests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
