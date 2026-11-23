pkgname = "pkgconf"
pkgver = "3.0.11"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
pkgdesc = "Provides compiler and linker configuration"
license = "MIT"
url = "http://pkgconf.org"
source = f"https://distfiles.dereferenced.org/pkgconf/pkgconf-{pkgver}.tar.xz"
sha256 = "d0cd841bc8e55b9da888106c00dc256d05b7d1d8e5a46f4be4eb4c5125bd2dc4"
hardening = ["!vis", "!cfi"]
options = ["bootstrap"]


def post_install(self):
    self.install_license("COPYING")

    self.install_link("usr/bin/pkg-config", "pkgconf")
    self.install_link("usr/share/man/man1/pkg-config.1", "pkgconf.1")


@split("libs")
def _(self):
    self.subdesc = "runtime library"
    # transitional
    self.provides = [self.with_pkgver("libpkgconf")]

    return self.default_libs()


@split("devel")
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
