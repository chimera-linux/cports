pkgname = "qbe"
pkgver = "1.2"
pkgrel = 0
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "makefile"
pkgdesc = "Compiler backend"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://c9x.me/compile"
source = f"https://c9x.me/compile/release/qbe-{pkgver}.tar.xz"
sha256 = "a6d50eb952525a234bf76ba151861f73b7a382ac952d985f2b9af1df5368225d"
hardening = ["!int"]


def post_install(self):
    self.install_license("LICENSE")
