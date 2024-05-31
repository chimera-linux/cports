pkgname = "libkexiv2"
pkgver = "24.05.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # manual test bins
    "-DBUILD_TESTING=OFF",
    "-DQT_MAJOR_VERSION=6",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "exiv2-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE wrapper around exiv2"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://api.kde.org/libkexiv2/html/index.html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkexiv2-{pkgver}.tar.xz"
sha256 = "0ceed68ae17cc225c915d74e7b67e77d7912d56613c0a842cfe00dd17d054d74"
# CFI: check
hardening = ["vis", "!cfi"]


@subpackage("libkexiv2-devel")
def _devel(self):
    return self.default_devel()
