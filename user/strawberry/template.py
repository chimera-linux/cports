pkgname = "strawberry"
pkgver = "1.2.13"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_GPOD=OFF", "-DENABLE_STREAMTAGREADER=OFF"]
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
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "icu-devel",
    "kdsingleapplication-devel",
    "libcdio-devel",
    "libebur128-devel",
    "libmtp-devel",
    "libpulse-devel",
    "protobuf-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "rapidjson",
    "sqlite-devel",
    "taglib-devel",
]
checkdepends = ["gtest-devel"]
depends = ["qt6-qtbase-sql"]
pkgdesc = "Audio player and organizer"
license = "GPL-3.0-or-later"
url = "https://www.strawberrymusicplayer.org"
source = f"https://files.strawberrymusicplayer.org/strawberry-{pkgver}.tar.xz"
sha256 = "8b7eea3f22b354b529f62e27072030a85ef13a4b3fcac77c0f04e452be6f41ae"
