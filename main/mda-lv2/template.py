pkgname = "mda-lv2"
pkgver = "1.2.10"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = ["lv2"]
pkgdesc = "Port of MDA VST plugins to LV2"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/drobilla/mda-lv2"
source = f"https://download.drobilla.net/mda-lv2-{pkgver}.tar.xz"
sha256 = "aeea5986a596dd953e2997421a25e45923928c6286c4c8c36e5ef63ca1c2a75a"
hardening = ["vis", "!cfi"]
