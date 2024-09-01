pkgname = "pcsx2"
pkgver = "2.1.120"
pkgrel = 0
# pcsx2 doesn't support anything else
archs = ["x86_64"]
build_style = "cmake"
configure_args = [
    # disables debug mode
    "-DCMAKE_BUILD_TYPE=Release",
    "-DDISABLE_ADVANCE_SIMD=ON",
    "-DENABLE_TESTS=ON",
    "-DPACKAGE_MODE=ON",
    "-DUSE_BACKTRACE=OFF",
    "-DUSE_LINKED_FFMPEG=ON",
    "-DUSE_VTUNE=OFF",
    "-DUSE_VULKAN=ON",
    "-DWAYLAND_API=ON",
    "-DX11_API=ON",
    f"-DPCSX2_GIT_TAG=v{pkgver}",
]
make_check_target = "unittests"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "extra-cmake-modules",
    "ffmpeg-devel",
    "libcurl-devel",
    "libpcap-devel",
    "libpng-devel",
    "libpulse-devel",
    "libwebp-devel",
    "libzip-devel",
    "libzip-progs",
    "lz4-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "sdl-devel",
    "shaderc-devel",
    "udev-devel",
    "vulkan-loader-devel",
    "wayland-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
depends = ["cmd:gst-play-1.0!gst-plugins-base"]
checkdepends = ["perl"]
pkgdesc = "Playstation 2 emulator"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://pcsx2.net"
source = [
    f"https://github.com/PCSX2/pcsx2/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/PCSX2/pcsx2_patches/archive/f89319e50e759b4d34cf6cf360b74b39d0a3f18a.tar.gz",
]
source_paths = [
    ".",
    "patches",
]
sha256 = [
    "c4960ae92f119643433f98009a1e5164b6aab9f34b4ecc9ddfd736327ea802ad",
    "a83fe869ee4108b8539454038403cda5c93143ed773668ff8bac6973d154285b",
]
# FIXME: cfi, int
# but it's an emulator so..
hardening = ["vis", "!int"]

# shut up about PAGE_SIZE on internal emulator stuff,
# and meaningless deprecation warnings spamming the logs
tool_flags = {
    "CXXFLAGS": [
        "-Wno-deprecated-declarations",
        "-Wno-macro-redefined",
    ],
}


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
