pkgname = "libpng"
pkgver = "1.6.58"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # TODO: breaks riscv64 build
    "--disable-riscv-rvv",
]
hostmakedepends = ["automake", "pkgconf", "libtool"]
makedepends = ["zlib-ng-compat-devel"]
pkgdesc = "Library for manipulating PNG images"
license = "Libpng"
url = "https://www.libpng.org/pub/png/libpng.html"
source = f"$(SOURCEFORGE_SITE)/libpng/libpng-{pkgver}.tar.xz"
sha256 = "28eb403f51f0f7405249132cecfe82ea5c0ef97f1b32c5a65828814ae0d34775"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libpng-devel")
def _(self):
    return self.default_devel()


@subpackage("libpng-progs")
def _(self):
    return self.default_progs()
