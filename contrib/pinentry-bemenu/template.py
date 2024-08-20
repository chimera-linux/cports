pkgname = "pinentry-bemenu"
pkgver = "0.14.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "bemenu-devel",
    "libassuan-devel",
    "libgpg-error-devel",
    "popt-devel",
]
pkgdesc = "Pinentry based on bemenu"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "GPL-3.0-or-later"
url = "https://github.com/t-8ch/pinentry-bemenu"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "4ae3b3db14cb84e31da3e8995653c50cf0cd5019b32dc321518b42ec894b8071"


@subpackage("pinentry-bemenu-default")
def _(self):
    self.depends = [self.parent]
    self.provides = ["pinentry-default=0"]
    self.origin = "pinentry"

    return ["@usr/bin/pinentry=>pinentry-bemenu"]
