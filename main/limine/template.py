pkgname = "limine"
pkgver = "10.2.0"
pkgrel = 0
# these targets implemented
archs = ["aarch64", "loongarch64", "riscv64", "x86_64"]
build_style = "gnu_configure"
configure_args = ["--enable-all"]
hostmakedepends = ["automake", "mtools", "nasm"]
pkgdesc = "Multiprotocol EFI bootloader"
license = "BSD-2-Clause AND 0BSD"
url = "https://limine-bootloader.org"
source = f"https://codeberg.org/Limine/Limine/releases/download/v{pkgver}/limine-{pkgver}.tar.zst"
sha256 = "0de794cfb061bb42b9a9f5e8a5beac9c8f1f05783d8cb811741a7659c1aeaae0"
# no test suite
options = ["!check"]


def post_install(self):
    self.uninstall(f"usr/share/doc/{pkgname}/COPYING")
    self.install_license("COPYING")
