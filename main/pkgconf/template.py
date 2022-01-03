pkgname = "pkgconf"
pkgver = "1.8.0"
pkgrel = 0
build_style = "gnu_configure"
checkdepends = ["kyua"]
provides = [f"pc:libpkgconf={pkgver}"]
pkgdesc = "Provides compiler and linker configuration"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://pkgconf.org"
source = f"https://distfiles.dereferenced.org/pkgconf/pkgconf-{pkgver}.tar.xz"
sha256 = "ef9c7e61822b7cb8356e6e9e1dca58d9556f3200d78acab35e4347e9d4c2bbaf"
# checkdepends not available yet
options = ["bootstrap", "!check"]

def post_install(self):
    self.install_license("COPYING")

    self.install_link("pkgconf", "usr/bin/pkg-config")
    self.install_link("pkgconf.1", "usr/share/man/man1/pkg-config.1")

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
