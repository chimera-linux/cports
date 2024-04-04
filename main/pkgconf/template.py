pkgname = "pkgconf"
pkgver = "2.2.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
checkdepends = ["kyua"]
provides = [f"pc:libpkgconf={pkgver}"]
pkgdesc = "Provides compiler and linker configuration"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://pkgconf.org"
source = f"https://distfiles.dereferenced.org/pkgconf/pkgconf-{pkgver}.tar.xz"
sha256 = "b06ff63a83536aa8c2f6422fa80ad45e4833f590266feb14eaddfe1d4c853c69"
hardening = ["!cfi"]  # TODO
# checkdepends not available yet
options = ["bootstrap", "!check"]


def post_install(self):
    self.install_license("COPYING")

    self.install_link("usr/bin/pkg-config", "pkgconf")
    self.install_link("usr/share/man/man1/pkg-config.1", "pkgconf.1")


@subpackage("libpkgconf")
def _lib(self):
    self.pkgdesc += " (runtime library)"
    return self.default_libs()


@subpackage("pkgconf-devel")
def _devel(self):
    self.options = ["!scanpkgconf"]
    # pkg.m4 must remain in main package
    return [
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/lib/*.so",
        "usr/lib/*.a",
    ]
