pkgname = "limine"
pkgver = "7.1.0"
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
source = f"https://github.com/limine-bootloader/limine/releases/download/v{pkgver}/limine-{pkgver}.tar.xz"
sha256 = "9cc58ca26a74310105760f0db94464b4a4240c118eac93f1e1f5b301f230299c"
# no test suite
options = ["!check"]


def post_install(self):
    self.rm(self.destdir / f"usr/share/doc/{pkgname}/COPYING")
    self.install_license("COPYING")
