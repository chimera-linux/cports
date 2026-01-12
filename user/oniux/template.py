pkgname = "oniux"
pkgver = "0.6.1"
pkgrel = 0
build_style = "cargo"
make_install_args = ["--locked"]
hostmakedepends = ["cargo-auditable", "cmake", "pkgconf", "rust-bindgen"]
makedepends = ["openssl3-devel", "rust-std", "sqlite-devel", "zstd-devel"]
pkgdesc = "Kernel-level Tor isolation for Linux applications"
license = "MIT OR Apache-2.0"
url = "https://gitlab.torproject.org/tpo/core/oniux"
source = f"{url}/-/archive/v{pkgver}/oniux-v{pkgver}.tar.gz"
sha256 = "de8387e2a53ea944d0f368a455661357e5c441ac2cc16b81fb5ce5fbb9d3f532"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
