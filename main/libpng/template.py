pkgname = "libpng"
pkgver = "1.6.53"
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
sha256 = "1d3fb8ccc2932d04aa3663e22ef5ef490244370f4e568d7850165068778d98d4"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libpng-devel")
def _(self):
    return self.default_devel()


@subpackage("libpng-progs")
def _(self):
    return self.default_progs()
