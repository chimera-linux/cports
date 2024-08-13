pkgname = "pcsx2"
pkgver = "2.1.46"
pkgrel = 0
# pcsx2 doesn't support anything else
archs = ["x86_64"]
build_style = "cmake"
configure_args = [
    # disables debug mode
    "-DCMAKE_BUILD_TYPE=Release",
    "-DDISABLE_ADVANCE_SIMD=ON",
    "-DENABLE_TESTS=ON",
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
_patches = "efd872286d9b2ae77530b82fbc56a3110caad960"
source = [
    f"https://github.com/PCSX2/pcsx2/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/PCSX2/pcsx2_patches/archive/{_patches}.tar.gz",
]
source_paths = [
    ".",
    "patches",
]
sha256 = [
    "f123604f84576329ae298bdb1726154ee45ef3fbde20b19f3727b204f589c621",
    "1671aac2a840c3e9b0d298c7ab46667c18be9191256802cfc7c5cb1696c82d35",
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
