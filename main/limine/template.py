pkgname = "limine"
pkgver = "11.1.0"
pkgrel = 0
# these targets implemented
archs = ["aarch64", "loongarch64", "riscv64", "x86_64"]
build_style = "gnu_configure"
configure_args = ["--enable-all"]
hostmakedepends = ["automake", "mtools", "nasm"]
pkgdesc = "Multiprotocol EFI bootloader"
license = "BSD-2-Clause AND 0BSD"
url = "https://limine-bootloader.org"
source = f"https://codeberg.org/Limine/Limine/releases/download/v{pkgver}/limine-{pkgver}.tar.gz"
sha256 = "ef4585442b5cde1fc0b32e59668a16dd283f96780f178364e283e6feafe98460"
# no test suite
options = ["!check"]


def post_install(self):
    self.uninstall(f"usr/share/doc/{pkgname}/COPYING")
    self.install_license("COPYING")
