pkgname = "limine"
pkgver = "12.5.2"
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
sha256 = "1780781336d690c551fc5305604b4c3e3d7499f6cebc504bfa0cda3b712213c1"
# no test suite
options = ["!check"]


def post_install(self):
    self.uninstall(f"usr/share/doc/{pkgname}/COPYING")
    self.install_license("COPYING")
