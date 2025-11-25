pkgname = "tg_owt-static"
pkgver = "0_git20251117"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=OFF",
]
_gitrev = "d067233a845e387e63d480d0d846da5fcb6a40cb"
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
    "2fa028a7ce63e13abd01ab959c9c22aaaac22953b5ab1c76de224536575f0d74",
    "b0397b85ddf0ee10be288687a017ad057f93bac5e1a28f30fcd67665d4271285",
    "eadc1c7276135320f42a22599f23a2f55419e1d90a3c6a4c58cd1586f7b83bff",
]
tool_flags = {"CXXFLAGS": [], "CFLAGS": []}
# crashes
hardening = ["!int"]

if self.profile().endian == "big":
    broken = "tdesktop deosn't work on this anyway etc."


def post_install(self):
    self.install_license("LICENSE")
