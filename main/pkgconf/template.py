pkgname = "pkgconf"
pkgver = "2.4.3"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
checkdepends = ["kyua"]
pkgdesc = "Provides compiler and linker configuration"
license = "MIT"
url = "http://pkgconf.org"
source = f"https://distfiles.dereferenced.org/pkgconf/pkgconf-{pkgver}.tar.xz"
sha256 = "51203d99ed573fa7344bf07ca626f10c7cc094e0846ac4aa0023bd0c83c25a41"
hardening = ["!vis", "!cfi"]
# check: cycle
options = ["bootstrap", "!check"]


def post_install(self):
    self.install_license("COPYING")

    self.install_link("usr/bin/pkg-config", "pkgconf")
    self.install_link("usr/share/man/man1/pkg-config.1", "pkgconf.1")


@subpackage("pkgconf-libs")
def _(self):
    self.subdesc = "runtime library"
    # transitional
    self.provides = [self.with_pkgver("libpkgconf")]

    return self.default_libs()


@subpackage("pkgconf-devel")
def _(self):
    self.options = ["!scanpkgconf"]
    self.provides = [f"pc:libpkgconf={pkgver}"]
    # pkg.m4 must remain in main package
    return [
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/lib/*.so",
        "usr/lib/*.a",
    ]
