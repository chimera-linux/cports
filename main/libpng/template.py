pkgname = "libpng"
pkgver = "1.6.59"
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
sha256 = "d80dd2a38a37f803cb9b6ac7b14bd6e74ddc3b654780a8380bdf93523fdb4389"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libpng-devel")
def _(self):
    return self.default_devel()


@subpackage("libpng-progs")
def _(self):
    return self.default_progs()
