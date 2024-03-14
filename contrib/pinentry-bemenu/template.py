pkgname = "pinentry-bemenu"
pkgver = "0.13.1"
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
sha256 = "db513f0cb2ee81f064da2dca976cb9376857da4bef316d493b347f692521bb40"
