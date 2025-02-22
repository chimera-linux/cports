pkgname = "strawberry"
pkgver = "1.2.7"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_GPOD=OFF"]
hostmakedepends = [
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
    "protobuf",
    "qt6-qtbase",
    "qt6-qttools",
]
makedepends = [
    "alsa-lib-devel",
    "boost-devel",
    "chromaprint-devel",
    "dbus-devel",
    "fftw-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gstreamer-devel",
    "gst-plugins-base-devel",
    "icu-devel",
    "kdsingleapplication-devel",
    "libcdio-devel",
    "libebur128-devel",
    "libmtp-devel",
    "libpulse-devel",
    "protobuf-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "sqlite-devel",
    "taglib-devel",
]
checkdepends = ["gtest-devel"]
depends = ["qt6-qtbase-sql"]
pkgdesc = "Audio player and organizer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.strawberrymusicplayer.org"
source = f"https://files.strawberrymusicplayer.org/strawberry-{pkgver}.tar.xz"
sha256 = "3411878ce1937fc5161ed9cffe25591c228035b6918d383bd26f73d12eed799a"
