pkgname = "k3b"
pkgver = "24.12.1"
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
sha256 = "26ca9a5b17293434d54bf14fa333f90d5b72d8473c540da01006080eb423e3ea"

if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]
