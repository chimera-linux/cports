pkgname = "limine"
pkgver = "7.9.0"
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
sha256 = "d78c77202e4b29ab933678cddf59887c1a4a8363f627d451390d3bcca5742d80"
# no test suite
options = ["!check"]


def post_install(self):
    self.rm(self.destdir / f"usr/share/doc/{pkgname}/COPYING")
    self.install_license("COPYING")
