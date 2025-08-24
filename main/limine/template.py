pkgname = "limine"
pkgver = "9.6.1"
pkgrel = 0
# these targets implemented
archs = ["aarch64", "loongarch64", "riscv64", "x86_64"]
build_style = "gnu_configure"
configure_args = ["--enable-all"]
hostmakedepends = ["automake", "mtools", "nasm"]
pkgdesc = "Multiprotocol EFI bootloader"
license = "BSD-2-Clause AND 0BSD"
url = "https://limine-bootloader.org"
source = f"https://github.com/limine-bootloader/limine/releases/download/v{pkgver}/limine-{pkgver}.tar.zst"
sha256 = "730fc68ef7d068cb370420f8783a14c021a0c45e864dff7e1f4df6e9d2cfea7e"
# no test suite
options = ["!check"]


def post_install(self):
    self.uninstall(f"usr/share/doc/{pkgname}/COPYING")
    self.install_license("COPYING")
