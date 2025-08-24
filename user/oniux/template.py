pkgname = "oniux"
pkgver = "0.6.0"
pkgrel = 0
build_style = "cargo"
make_install_args = ["--locked"]
hostmakedepends = ["cargo-auditable", "cmake", "pkgconf", "rust-bindgen"]
makedepends = ["openssl3-devel", "rust-std", "sqlite-devel", "zstd-devel"]
pkgdesc = "Kernel-level Tor isolation for Linux applications"
license = "MIT OR Apache-2.0"
url = "https://gitlab.torproject.org/tpo/core/oniux"
source = f"{url}/-/archive/v{pkgver}/oniux-v{pkgver}.tar.gz"
sha256 = "05146dfcda5bc152c2c9417392fc810cff64cb3842a1af9317a258f2e335d7e2"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
