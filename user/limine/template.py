pkgname = "limine"
pkgver = "7.3.0"
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
source = f"https://github.com/limine-bootloader/limine/releases/download/v{pkgver}/limine-{pkgver}.tar.zst"
sha256 = "68048bce429b45c5f61edaecb23ac7af10b3eeaff3b0ea2663e3101fcba32e7e"
# no test suite
options = ["!check"]


def post_install(self):
    self.rm(self.destdir / f"usr/share/doc/{pkgname}/COPYING")
    self.install_license("COPYING")
