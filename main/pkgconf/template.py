pkgname = "pkgconf"
pkgver = "2.3.0"
pkgrel = 2
build_style = "gnu_configure"
configure_gen = []
checkdepends = ["kyua"]
pkgdesc = "Provides compiler and linker configuration"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://pkgconf.org"
source = f"https://distfiles.dereferenced.org/pkgconf/pkgconf-{pkgver}.tar.xz"
sha256 = "3a9080ac51d03615e7c1910a0a2a8df08424892b5f13b0628a204d3fcce0ea8b"
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
