pkgname = "limine"
pkgver = "12.0.2"
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
sha256 = "6c71c1a90ad02d8d09fbc4647d2f6ab324469387f0db5c6c6f49c1d875642b08"
# no test suite
options = ["!check"]


def post_install(self):
    self.uninstall(f"usr/share/doc/{pkgname}/COPYING")
    self.install_license("COPYING")
