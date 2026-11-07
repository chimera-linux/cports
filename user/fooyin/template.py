pkgname = "fooyin"
pkgver = "0.14.1"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "qt6-qttools",
]
makedepends = [
    "ffmpeg-devel",
    "flac-devel",
    "icu-devel",
    "kdsingleapplication-devel",
    "libarchive-devel",
    "libcdio-devel",
    "libcdio-paranoia-devel",
    "libebur128-devel",
    "libgme-devel",
    "libopenmpt-devel",
    "libsndfile-devel",
    "libvorbis-devel",
    "mpg123-devel",
    "opus-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "qcoro-devel",
    "qt6-qtbase-devel",
    "qt6-qtimageformats-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "soundtouch-devel",
    "soxr-devel",
    "taglib-devel",
    "zlib-ng-devel",
]
pkgdesc = "Customisable music player"
license = "GPL-3.0-or-later"
url = "https://fooyin.org"
source = f"https://github.com/fooyin/fooyin/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "017478a4b9b663e7c88dafc3de6f80d35d11ed83e96eebbb88b54d918f56f734"
# VIS + CFI + SST fails to run with sigsegv, as well as VIS + CFI, or SST
