pkgname = "limine"
pkgver = "9.6.5"
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
sha256 = "8751f0418d2ed6c1a99874a8925491f53b963b008ef4a51ecd0725dd812dfff3"
# no test suite
options = ["!check"]


def post_install(self):
    self.uninstall(f"usr/share/doc/{pkgname}/COPYING")
    self.install_license("COPYING")
