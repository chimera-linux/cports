pkgname = "limine"
pkgver = "12.9.0"
pkgrel = 0
# these targets implemented
archs = ["aarch64", "loongarch64", "riscv64", "x86_64"]
build_style = "gnu_configure"
configure_args = ["--enable-all"]
hostmakedepends = ["automake", "mtools", "nasm"]
pkgdesc = "Multiprotocol EFI bootloader"
license = "BSD-2-Clause AND 0BSD"
url = "https://limine-bootloader.org"
source = f"https://github.com/Limine-Bootloader/Limine/releases/download/v{pkgver}/limine-{pkgver}.tar.gz"
sha256 = "adea922af3b9c8179a4676bcecc8e4df2f3ef72ad36b3f4afab44cbf5f265e36"
# no test suite
options = ["!check"]


def post_install(self):
    self.uninstall(f"usr/share/doc/{pkgname}/COPYING")
    self.install_license("COPYING")
