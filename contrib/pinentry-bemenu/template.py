pkgname = "pinentry-bemenu"
pkgver = "0.13.2"
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
sha256 = "a1296ed087335d68df65442b222bcdd34c9b51132623a8141d5a8cca8e735a1c"


@subpackage("pinentry-bemenu-default")
def _def(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provides = ["pinentry-default=0"]
    self.origin = "pinentry"

    return ["@usr/bin/pinentry=>pinentry-bemenu"]
