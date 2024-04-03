pkgname = "pinentry-bemenu"
pkgver = "0.13.1"
pkgrel = 3
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
sha256 = "db513f0cb2ee81f064da2dca976cb9376857da4bef316d493b347f692521bb40"


@subpackage("pinentry-bemenu-default")
def _def(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provides = ["pinentry-default=0"]
    self.origin = "pinentry"

    return ["@usr/bin/pinentry=>pinentry-bemenu"]
