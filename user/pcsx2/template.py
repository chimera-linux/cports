pkgname = "pcsx2"
pkgver = "2.8.2"
pkgrel = 0
# game patches from https://github.com/PCSX2/pcsx2_patches
_patches_commit = "1fd98102b8e2fffe3e0c29aab55339d48af0ffe5"
# pcsx2 doesn't support anything else
archs = ["aarch64", "x86_64"]
build_style = "cmake"
configure_args = [
    # disables debug mode
    "-DCMAKE_BUILD_TYPE=Release",
    "-DDISABLE_ADVANCE_SIMD=ON",
    "-DPACKAGE_MODE=ON",
    "-DUSE_BACKTRACE=OFF",
    "-DUSE_LINKED_FFMPEG=ON",
    "-DUSE_VTUNE=OFF",
    f"-DPCSX2_GIT_TAG=v{pkgver}",
]
make_check_target = "unittests"
hostmakedepends = [
    "cmake",
    "libzip-progs",
    "ninja",
    "pkgconf",
]
makedepends = [
    "curl-devel",
    "extra-cmake-modules",
    "ffmpeg-devel",
    "kddockwidgets-devel",
    "libpcap-devel",
    "libpng-devel",
    "libpulse-devel",
    "libwebp-devel",
    "libzip-devel",
    "lz4-devel",
    "plutosvg-devel",
    "plutovg-devel",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
    "rapidyaml-devel",
    "sdl3-devel",
    "shaderc-devel",
    "udev-devel",
    "vulkan-loader-devel",
    "wayland-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
depends = ["cmd:gst-play-1.0!gst-plugins-base"]
pkgdesc = "Playstation 2 emulator"
license = "GPL-3.0-or-later"
url = "https://pcsx2.net"
source = [
    f"https://github.com/PCSX2/pcsx2/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/PCSX2/pcsx2_patches/archive/{_patches_commit}.tar.gz",
]
source_paths = [
    ".",
    "patches",
]
sha256 = [
    "8d1762d568c92198e61a284064d0e5c0d2c6ab1c5bac60ef1330dd0fe44d10a7",
    "c3c1ddbf46d4f4e138d0c1a2502d912b0ee6fc468c29b7af5c091d79499ebc70",
]
# int crashes, but it's an emulator so..
hardening = ["vis", "!int"]


def post_build(self):
    # .pnach's are top-level files in a patches.zip archive to be loaded
    self.do(
        "tar",
        "--strip-components=2",
        "-cvaf",
        "patches.zip",
        *self.find("patches", "*.pnach"),
    )


def post_install(self):
    self.install_file(
        self.files_path / "PCSX2.desktop", "usr/share/applications"
    )
    self.install_file("./patches.zip", "usr/share/PCSX2/resources")
    self.install_file(
        "bin/resources/icons/AppIconLarge.png",
        "usr/share/icons/hicolor/512x512/apps",
        name="PCSX2.png",
    )
    self.install_file(
        "pcsx2-qt/resources/icons/AppIcon64.png",
        "usr/share/icons/hicolor/64x64/apps",
        name="PCSX2.png",
    )
