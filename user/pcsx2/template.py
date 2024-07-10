pkgname = "pcsx2"
pkgver = "1.7.5973"
pkgrel = 0
# pcsx2 doesn't support anything else
archs = ["x86_64"]
build_style = "cmake"
configure_args = [
    # disables debug mode
    "-DCMAKE_BUILD_TYPE=Release",
    "-DDISABLE_ADVANCE_SIMD=ON",
    "-DENABLE_TESTS=ON",
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
depends = ["virtual:cmd:gst-play-1.0!gst-plugins-base"]
checkdepends = ["perl"]
pkgdesc = "Playstation 2 emulator"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later"
url = "https://pcsx2.net"
_patches = "85654677173d10ccabb67c89f0f04e4d527321e9"
source = [
    f"https://github.com/PCSX2/pcsx2/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/PCSX2/pcsx2_patches/archive/{_patches}.tar.gz",
]
source_paths = [
    ".",
    "patches",
]
sha256 = [
    "ae7c920a5823583c9613673d2746baa10c8997592b21070f42efbd8297121961",
    "710e9d258b4fb29127d9fa6d9079ded3dfae6afa0ad81ceddf5417f5e9032f2c",
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


def do_install(self):
    self.install_file(
        self.files_path / "PCSX2.desktop", "usr/share/applications"
    )
    self.install_files("build/bin", "usr/lib", name="PCSX2")
    self.install_dir("usr/bin")
    self.install_link("usr/bin/pcsx2", "../lib/PCSX2/pcsx2-qt")
    self.install_file("./patches.zip", "usr/lib/PCSX2/resources")

    # prune test exes since we copy bin/ wholesale
    self.uninstall("usr/lib/PCSX2/*test", glob=True)
