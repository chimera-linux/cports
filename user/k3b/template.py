pkgname = "k3b"
pkgver = "25.08.2"
pkgrel = 1
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
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
license = "GPL-2.0-only"
url = "https://apps.kde.org/k3b"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/k3b-{pkgver}.tar.xz"
sha256 = "b4eb2ee069a968f7dc3ec4825395af75e6bfb489d96a28948f22ee51a36afa35"

if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]


@subpackage("k3b-devel")
def _(self):
    return self.default_devel()
