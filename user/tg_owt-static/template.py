pkgname = "tg_owt-static"
pkgver = "0_git20260803"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=OFF",
]
_gitrev = "19d51d3c19632a63fdbe17c62f10332d978cb940"
_libyuv_gitrev = "04821d1e7d60845525e8db55c7bcd41ef5be9406"
_crc32c_gitrev = "1c51f87c9ad8157b4461e2216b9272f13fd0be3b"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "protobuf",
    "python",
]
_rdeps = [
    "abseil-cpp-devel",
    "alsa-lib-devel",
    "libdrm-devel",
    "libpulse-devel",
    "libx11-devel",
    "libxdamage-devel",
    "libxext-devel",
    "libxfixes-devel",
    "libxrandr-devel",
    "libxtst-devel",
    "linux-headers",
    "mesa-gbm-devel",
    "musl-bsd-headers",
    "openssl3-devel",
    "opus-devel",
    "pipewire-devel",
]
makedepends = [
    "ffmpeg-devel",
    "glib-devel",
    "libdrm-devel",
    "libepoxy-devel",
    "libevent-devel",
    "libglvnd-devel",
    "libjpeg-turbo-devel",
    "libsrtp-devel",
    "libvpx-devel",
    "libxcomposite-devel",
    "libxrender-devel",
    "mesa-gbm-devel",
    "openh264-devel",
    "protobuf-devel",
    *_rdeps,
]
depends = [
    "pc:gl!libglvnd-devel",
    *_rdeps,
]
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
    "eee57f5f544dd8c0e29719a0c3ec56c221ade343036caf080e260d6c695167df",
    "b0397b85ddf0ee10be288687a017ad057f93bac5e1a28f30fcd67665d4271285",
    "eadc1c7276135320f42a22599f23a2f55419e1d90a3c6a4c58cd1586f7b83bff",
]
tool_flags = {"CXXFLAGS": [], "CFLAGS": []}
# crashes
hardening = ["!int"]

if self.profile.endian == "big":
    broken = "tdesktop deosn't work on this anyway etc."


def post_install(self):
    self.install_license("LICENSE")
