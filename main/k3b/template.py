pkgname = "k3b"
pkgver = "26.08.3"
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
    "ffmpeg-devel",
    "flac-devel",
    "karchive-devel",
    "kauth-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdoctools-devel",
    "kfilemetadata-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kjobwidgets-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "lame-devel",
    "libdvdread-devel",
    "libkcddb-devel",
    "libmusicbrainz-devel",
    "libsamplerate-devel",
    "libsndfile-devel",
    "libvorbis-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtmultimedia-devel",
    "solid-devel",
    "taglib-devel",
]
depends = [
    "cdrdao",
    "cdrkit",
    "dvd+rw-tools",
    "libburn",
    "libcdio-paranoia",  # dlopen
    "libdvdcss",  # dlopen
]
pkgdesc = "KDE disc burning and ripping application"
license = "GPL-2.0-only"
url = "https://apps.kde.org/k3b"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/k3b-{pkgver}.tar.xz"
sha256 = "a726c99221f1da02ea47bbe63a282fb510ca996eb449461d4b9ecdfbe69ed8f5"

if self.profile.arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]


@subpackage("k3b-devel")
def _(self):
    return self.default_devel()
