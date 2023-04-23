pkgname = "limine"
pkgver = "4.20230422.0"
pkgrel = 0
archs = ["x86_64", "aarch64"]
build_style = "gnu_configure"
configure_args = [
    "--enable-all",
    "TOOLCHAIN_FOR_TARGET=llvm"
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "mtools", "nasm"]
pkgdesc = "Advanced, portable, multiprotocol bootloader"
maintainer = "vazub <chimera@zubko.cc>"
license = "BSD-2-Clause"
url = "https://limine-bootloader.org"
source = f"https://github.com/limine-bootloader/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d42fe5488c221e2f69e1f7c920e5231841dd5ff65993b70104d7a6be00c93fcc"
hardening = ["vis", "cfi", "sst"]
# no test suite
options = ["!check"]

def post_install(self):
    self.rm(self.destdir / f"usr/share/doc/{pkgname}/LICENSE")
    self.install_license("LICENSE")
