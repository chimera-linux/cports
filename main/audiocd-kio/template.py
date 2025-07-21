pkgname = "audiocd-kio"
pkgver = "25.04.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cdparanoia-devel",
    "flac-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kio-devel",
    "libkcddb-devel",
    "libkcompactdisc-devel",
    "libvorbis-devel",
    "qt6-qtbase-devel",
]
# mp3 encoding
depends = ["lame"]
pkgdesc = "KDE bookmarks editor"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kio_audiocd"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/audiocd-kio-{pkgver}.tar.xz"
sha256 = "446bf072506f847409fbe2712eed898f14d95be4caad4501cd04be83c4da7213"


@subpackage("audiocd-kio-devel")
def _(self):
    self.depends += [
        "kio-devel",
        "libkcddb-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
