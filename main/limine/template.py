pkgname = "limine"
pkgver = "10.5.0"
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
sha256 = "da14c18eff4bda562cc44c69c7e2aebd9419ac1f1c8be32d76232eaa367503d2"
# no test suite
options = ["!check"]


def post_install(self):
    self.uninstall(f"usr/share/doc/{pkgname}/COPYING")
    self.install_license("COPYING")
