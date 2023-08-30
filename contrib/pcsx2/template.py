pkgname = "pcsx2"
pkgver = "1.7.4967"
pkgrel = 0
# pcsx2 doesn't support anything else
archs = ["x86_64"]
build_style = "cmake"
configure_args = [
    "-DCMAKE_DISABLE_PRECOMPILE_HEADERS=ON",
    "-DDISABLE_ADVANCE_SIMD=ON",
    "-DDISABLE_BUILD_DATE=ON",
    "-DENABLE_TESTS=ON",
    "-DUSE_ACHIEVEMENTS=ON",
    "-DUSE_DISCORD_PRESENCE=OFF",
    "-DUSE_LINKED_FFMPEG=ON",
    "-DUSE_VTUNE=OFF",
    "-DUSE_VULKAN=ON",
    "-DWAYLAND_API=ON",
    "-DX11_API=ON",
]
make_check_target = "unittests"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "extra-cmake-modules",
    "ffmpeg-devel",
    "fmt-devel",
    "libaio-devel",
    "libcurl-devel",
    "libpcap-devel",
    "libpng-devel",
    "libpulse-devel",
    "libzip-devel",
    "libzip-progs",
    "libzstd-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "rapidyaml-devel",
    "sdl-devel",
    "udev-devel",
    "vulkan-headers",
    "vulkan-loader",
    "wayland-devel",
    "zlib-devel",
]
checkdepends = ["perl"]
pkgdesc = "Playstation 2 emulator"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later"
url = "https://pcsx2.net"
_patches = "ec2132bbb5bd9f588a983fd8949be3eaa52316a8"
_glslang = "11.12.0"
_gtest = "v1.14.0"
_libchdr = "54bfb871ccae31903b95a8feb7f2bf7121f304be"
_rcheevos = "v10.7.1"
_fastfloat = "v5.2.0"
source = [
    f"https://github.com/PCSX2/pcsx2/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/PCSX2/pcsx2_patches/archive/{_patches}.tar.gz",
    f"https://github.com/KhronosGroup/glslang/archive/{_glslang}.tar.gz",
    f"https://github.com/google/googletest/archive/refs/tags/{_gtest}.tar.gz",
    f"https://github.com/rtissera/libchdr/archive/{_libchdr}.tar.gz",
    f"https://github.com/RetroAchievements/rcheevos/archive/refs/tags/{_rcheevos}.tar.gz",
    f"https://github.com/fastfloat/fast_float/archive/refs/tags/{_fastfloat}.tar.gz",
]
source_paths = [
    ".",
    "patches",
    "3rdparty/glslang/glslang",
    "3rdparty/gtest",
    "3rdparty/libchdr/libchdr",
    "3rdparty/rcheevos/rcheevos",
    "3rdparty/fast_float",
]
sha256 = [
    "5973db25ab029eb63b98e150ab7894d711aeb6444d9ffca3d2c103cad9a8245f",
    "811b8391f0a2e658102aca30cb4e5418df1ef9f1f1b90f818c18036b941ae87b",
    "7795a97450fecd9779f3d821858fbc2d1a3bf1dd602617d95b685ccbcabc302f",
    "8ad598c73ad796e0d8280b082cebd82a630d73e73cd3c70057938a6501bba5d7",
    "1ae342dfadd51f7c42b34da44f9eb534fc64ee61c88f96b6bbcbbf9ebe3df636",
    "ef0c6a93340d02114fbf38cd41f0413591b679f728314f4908851a74f8565d0f",
    "72bbfd1914e414c920e39abdc81378adf910a622b62c45b4c61d344039425d18",
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
    self.install_files("build/bin", "usr/lib")
    self.mv(self.destdir / "usr/lib/bin", self.destdir / "usr/lib/PCSX2")

    self.install_dir("usr/lib/PCSX2/resources")
    self.install_file("./patches.zip", "usr/lib/PCSX2/resources")

    # prune test exes since we copy bin/ wholesale
    for f in (self.destdir / "usr/lib/PCSX2").glob("*test"):
        f.unlink()

    self.install_dir("usr/bin")
    self.install_link("../lib/PCSX2/pcsx2-qt", "usr/bin/pcsx2")
