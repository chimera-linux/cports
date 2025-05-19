pkgname = "oniux"
pkgver = "0.5.0"
pkgrel = 0
build_style = "cargo"
make_install_args = ["--locked"]
hostmakedepends = ["cargo-auditable", "cmake", "pkgconf", "rust-bindgen"]
makedepends = ["rust-std", "sqlite-devel", "zstd-devel"]
pkgdesc = "Kernel-level Tor isolation for Linux applications"
license = "MIT OR Apache-2.0"
url = "https://gitlab.torproject.org/tpo/core/oniux"
source = f"https://gitlab.torproject.org/tpo/core/oniux/-/archive/v{pkgver}/oniux-v{pkgver}.tar.gz"
sha256 = "27e225e9a8aebc1cdd5731875731c57a3627df5411db2d8cac1cb9db841fc56a"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE-MIT")
