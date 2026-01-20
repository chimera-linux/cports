pkgname = "tdesktop"
pkgver = "6.4.2"
pkgrel = 0
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
    "gperf",
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
    "fmt-devel",
    "glib-devel",
    "hunspell-devel",
    "jemalloc-devel",
    "kcoreaddons-devel",
    "libavif-devel",
    "libdbusmenu-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
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
source = [
    f"https://github.com/telegramdesktop/tdesktop/releases/download/v{pkgver}/tdesktop-{pkgver}-full.tar.gz",
    "https://github.com/tdlib/td/archive/dd1b761fda7e47f4e0275c4d319f80a04db1997f.tar.gz",
]
source_paths = [".", "tde2e"]
sha256 = [
    "69cf9c0ca160126a0460312242730e2faa9eb5099ca17abc94e80feb8ad1ac0b",
    "b5e2a20eb38044b124650dbc72b3cc9d134e1c7861df2227f0e649b427c29fa4",
]
tool_flags = {"CXXFLAGS": [], "CFLAGS": []}
# crashes
hardening = ["!int"]

if self.profile().endian == "big":
    broken = "broken at protocol level"
elif self.profile().arch == "riscv64":
    broken = "compiler segfault"


def pre_configure(self):
    from cbuild.util import cmake

    # siiigh
    with self.stamp("tdlib_configure") as s:
        s.check()
        # the "out/Release" path is significant as tdesktop expects it
        cmake.configure(
            self,
            build_dir="tde2e/out/Release",
            cmake_dir="tde2e",
            extra_args=[
                "-DBUILD_SHARED_LIBS=OFF",
                "-DBUILD_TESTING=OFF",
                "-DTD_INSTALL_SHARED_LIBRARIES=OFF",
            ],
        )

    # we cannot use an external build btw, as the way the cmake is
    # set up requires a build directory of tdlib present, so...
    with self.stamp("tdlib_build") as s:
        s.check()
        cmake.build(self, "tde2e/out/Release")
