pkgname = "labwc-tweaks"
pkgver = "0.1.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "perl", "pkgconf"]
makedepends = [
    "libxml2-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "GUI configuration tool for labwc"
license = "GPL-2.0-only"
url = "https://github.com/labwc/labwc-tweaks"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a742250c7e8ea363758a024688226a4296a6798adc57abe0903d580ab195b749"
