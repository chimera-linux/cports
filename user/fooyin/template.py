pkgname = "fooyin"
pkgver = "0.15.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_ALSA=OFF"]
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
    "zlib-ng-compat-devel",
]
pkgdesc = "Customisable music player"
license = "GPL-3.0-or-later"
url = "https://fooyin.org"
source = f"https://github.com/fooyin/fooyin/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3f7b63fa99cd017046446fb94b3567bd900c85a472e3e23440f9fc48891cd3a0"
