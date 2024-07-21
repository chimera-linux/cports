pkgname = "limine"
pkgver = "7.12.0"
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
sha256 = "66f7818f878d4841bf8dc4405706dfcd02926e36605b772e51041ada7e123e57"
# no test suite
options = ["!check"]


def post_install(self):
    self.uninstall(f"usr/share/doc/{pkgname}/COPYING")
    self.install_license("COPYING")
