pkgname = "audiocd-kio"
pkgver = "25.12.2"
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
sha256 = "19b05dad94de5be4ea5f9dff736d74c58eccbde92d4f7c6249c09d92339e5490"


@subpackage("audiocd-kio-devel")
def _(self):
    self.depends += [
        "kio-devel",
        "libkcddb-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
