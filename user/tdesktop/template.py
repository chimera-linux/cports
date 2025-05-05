pkgname = "tdesktop"
pkgver = "5.13.1"
pkgrel = 3
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=OFF",
    "-DTDESKTOP_API_ID=22760243",
    "-DTDESKTOP_API_HASH=adf3bb6bd970f0381a929f47072c4a91",
    "-DDESKTOP_APP_DISABLE_CRASH_REPORTS=ON",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "glib-devel",
    "gobject-introspection",
    "ninja",
    "pkgconf",
    "protobuf",
    "python",
    "wayland-progs",
]
makedepends = [
    "ada-devel",
    "alsa-lib-devel",
    "boost-devel",
    "ffmpeg-devel",
    "glib-devel",
    "fmt-devel",
    "hunspell-devel",
    "jemalloc-devel",
    "kcoreaddons-devel",
    "libdbusmenu-devel",
    "libjpeg-turbo-devel",
    "libpulse-devel",
    "libva-devel",
    "libxcb-devel",
    "lz4-devel",
    "mesa-devel",
    "minizip-devel",
    "openal-soft-devel",
    "openssl3-devel",
    "opus-devel",
    "protobuf-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwayland-devel",
    "rapidjson",
    "rnnoise-devel",
    "tg_owt-static",
    "xcb-util-keysyms-devel",
    "xxhash-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
]
depends = ["qt6-qtimageformats", "webkitgtk4"]
pkgdesc = "Telegram desktop app"
license = "GPL-3.0-or-later"
url = "https://desktop.telegram.org"
source = f"https://github.com/telegramdesktop/tdesktop/releases/download/v{pkgver}/tdesktop-{pkgver}-full.tar.gz"
sha256 = "caa37bbf7d9fcdfecdb5f596f02a44becbe468ea5c6af7f3c670b61952744a80"
# crashes
hardening = ["!int"]

if self.profile().endian == "big":
    broken = "broken at protocol level"
elif self.profile().arch == "riscv64":
    broken = "compiler segfault"
