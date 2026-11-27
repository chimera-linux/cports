pkgname = "mixxx"
pkgver = "2.5.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DDOWNLOAD_MANUAL=OFF",
    "-DENGINEPRIME=OFF",
    "-DKEYFINDER=OFF",
    "-DINSTALL_USER_UDEV_RULES=ON",
    "-DOPTIMIZE=off",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "protobuf-protoc",
    "qt6-qtshadertools",
    "qt6-qttools",
]
makedepends = [
    "benchmark-devel",
    "chromaprint-devel",
    "ffmpeg-devel",
    "gtest-devel",
    "hidapi-devel",
    "lame-devel",
    "libebur128-devel",
    "libid3tag-devel",
    "libmad-devel",
    "libmodplug-devel",
    "libsndfile-devel",
    "libusb-devel",
    "lilv-devel",
    "mesa-devel",
    "ms-gsl",
    "opusfile-devel",
    "portaudio-devel",
    "portmidi-devel",
    "protobuf-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qtkeychain-devel",
    "rubberband-devel",
    "soundtouch-devel",
    "taglib-devel",
    "upower-devel",
    "wavpack-devel",
]
pkgdesc = "DJ mixing software"
license = "GPL-2.0-or-later"
url = "https://mixxx.org"
source = f"https://github.com/mixxxdj/mixxx/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9cfc9025d50d2511767ee52a07b8854f75c581f0585197d043bc219fcf9f9050"
# SIGILL tests fail
hardening = ["!int"]
