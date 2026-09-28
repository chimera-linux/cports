pkgname = "qbe"
pkgver = "1.2"
pkgrel = 3
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "makefile"
pkgdesc = "Compiler backend"
license = "MIT"
url = "https://c9x.me/compile"
source = f"https://c9x.me/compile/release/qbe-{pkgver}.tar.xz"
sha256 = "a6d50eb952525a234bf76ba151861f73b7a382ac952d985f2b9af1df5368225d"
# Breaks hare aarch64 build
# alias.c:192:16: runtime error: signed integer overflow: 1 + 9223372036854775807 cannot be represented in type 'int64_t' (aka 'long')
hardening = ["!int"]


def post_install(self):
    self.install_license("LICENSE")
