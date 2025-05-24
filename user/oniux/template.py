pkgname = "oniux"
pkgver = "0.4.0"
pkgrel = 0
build_style = "cargo"
make_install_args = ["--locked"]
hostmakedepends = ["cargo-auditable", "cmake", "pkgconf", "rust-bindgen"]
makedepends = ["rust-std", "sqlite-devel", "zstd-devel"]
pkgdesc = "Kernel-level Tor isolation for Linux applications"
license = "MIT OR Apache-2.0"
url = "https://gitlab.torproject.org/tpo/core/oniux"
source = f"https://gitlab.torproject.org/tpo/core/oniux/-/archive/v{pkgver}/oniux-v{pkgver}.tar.gz"
sha256 = "fbb1ca986d61d658a70c959242ce8d8a41437d2ec99e25d416311c1045ea72ff"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
