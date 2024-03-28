pkgname = "limine"
pkgver = "7.2.1"
pkgrel = 0
# these targets implemented
archs = ["aarch64", "x86_64", "riscv64"]
build_style = "gnu_configure"
configure_args = ["--enable-all", "TOOLCHAIN_FOR_TARGET=llvm"]
make_cmd = "gmake"
hostmakedepends = ["automake", "gmake", "mtools", "nasm"]
pkgdesc = "Multiprotocol EFI bootloader"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause AND 0BSD"
url = "https://limine-bootloader.org"
source = f"https://github.com/limine-bootloader/limine/releases/download/v{pkgver}/limine-{pkgver}.tar.xz"
sha256 = "bf72fe4deacd40a1730196021a1ea2d8a11eb2388ab71fb7ff57cebdd5c65915"
# no test suite
options = ["!check"]


def post_install(self):
    self.rm(self.destdir / f"usr/share/doc/{pkgname}/COPYING")
    self.install_license("COPYING")
