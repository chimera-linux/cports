pkgname = "k3b"
pkgver = "24.12.0"
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
    "dvd+rw-tools",
    "libburn",
    "libcdio-paranoia",  # dlopen
    "libdvdcss",  # dlopen
    "schilytools-cdrtools",
]
pkgdesc = "KDE disc burning and ripping application"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://apps.kde.org/k3b"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/k3b-{pkgver}.tar.xz"
sha256 = "2f25aed2645a758da6a781dfda8a0e7fc29a007d47edf66cdb4ab648873b4a31"

if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]
