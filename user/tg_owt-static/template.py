pkgname = "tg_owt-static"
pkgver = "0_git20250515"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=OFF",
]
_gitrev = "232ec410502e773024e8d83cfae83a52203306c0"
_libyuv_gitrev = "04821d1e7d60845525e8db55c7bcd41ef5be9406"
_crc32c_gitrev = "1c51f87c9ad8157b4461e2216b9272f13fd0be3b"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "protobuf",
    "python",
]
makedepends = [
    "abseil-cpp-devel",
    "alsa-lib-devel",
    "ffmpeg-devel",
    "glib-devel",
    "libdrm-devel",
    "libepoxy-devel",
    "libevent-devel",
    "libjpeg-turbo-devel",
    "libpulse-devel",
    "libsrtp-devel",
    "libvpx-devel",
    "libxcomposite-devel",
    "libxdamage-devel",
    "libxext-devel",
    "libxfixes-devel",
    "libxrandr-devel",
    "libxrender-devel",
    "libxtst-devel",
    "mesa-devel",
    "mesa-gbm-devel",
    "musl-bsd-headers",
    "openh264-devel",
    "openssl3-devel",
    "opus-devel",
    "pipewire-devel",
    "protobuf-devel",
]
depends = [*makedepends]
pkgdesc = "Telegram's fork of WebRTC"
license = "BSD-3-Clause"
url = "https://github.com/desktop-app/tg_owt"
source = [
    f"{url}/archive/{_gitrev}.tar.gz",
    f"https://github.com/google/crc32c/archive/{_crc32c_gitrev}.tar.gz",
    f"https://github.com/klemensn/libyuv/archive/{_libyuv_gitrev}.tar.gz",
]
source_paths = [
    ".",
    "src/third_party/crc32c/src",
    "src/third_party/libyuv",
]
sha256 = [
    "a5357e0bbf54488cb9c930ca57664e2047dbb0075b122f8186c3817ab70c9f85",
    "b0397b85ddf0ee10be288687a017ad057f93bac5e1a28f30fcd67665d4271285",
    "eadc1c7276135320f42a22599f23a2f55419e1d90a3c6a4c58cd1586f7b83bff",
]
# crashes
hardening = ["!int"]

if self.profile().endian == "big":
    broken = "tdesktop deosn't work on this anyway etc."


def post_install(self):
    self.install_license("LICENSE")
