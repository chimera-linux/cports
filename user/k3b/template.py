pkgname = "k3b"
pkgver = "25.12.1"
pkgrel = 0
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
sha256 = "7d3af238285b129a36877121b2e4cfd0572072ab6601ada178b2961f52bb496e"

if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]


@subpackage("k3b-devel")
def _(self):
    return self.default_devel()
