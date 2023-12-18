pkgname = "pcsx2"
pkgver = "1.7.5310"
pkgrel = 0
# pcsx2 doesn't support anything else
archs = ["x86_64"]
build_style = "cmake"
configure_args = [
    # disables debug mode
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_DISABLE_PRECOMPILE_HEADERS=ON",
    "-DDISABLE_ADVANCE_SIMD=ON",
    "-DDISABLE_BUILD_DATE=ON",
    "-DENABLE_TESTS=ON",
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
    "libwebp-devel",
    "libzip-devel",
    "libzip-progs",
    "lz4-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "rapidyaml-devel",
    "sdl-devel",
    "udev-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
    "zlib-devel",
    "zstd-devel",
]
checkdepends = ["perl"]
pkgdesc = "Playstation 2 emulator"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later"
url = "https://pcsx2.net"
_patches = "42d7ee72b66955e3bbd2caaeaa855f605b463722"
_glslang = "11.12.0"
_gtest = "v1.14.0"
_rcheevos = "8afec6c55e3a0f72368a5a085203bab1b8828ffb"
_fastfloat = "v5.3.0"
source = [
    f"https://github.com/PCSX2/pcsx2/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/PCSX2/pcsx2_patches/archive/{_patches}.tar.gz",
    f"https://github.com/KhronosGroup/glslang/archive/{_glslang}.tar.gz",
    f"https://github.com/google/googletest/archive/refs/tags/{_gtest}.tar.gz",
    f"https://github.com/RetroAchievements/rcheevos/archive/{_rcheevos}.tar.gz",
    f"https://github.com/fastfloat/fast_float/archive/refs/tags/{_fastfloat}.tar.gz",
]
source_paths = [
    ".",
    "patches",
    "3rdparty/glslang/glslang",
    "3rdparty/gtest",
    "3rdparty/rcheevos/rcheevos",
    "3rdparty/fast_float",
]
sha256 = [
    "d6fe7044b6279f5644fb2af534ad5d0b253eec4bf90a330723a51f89aa81ba94",
    "3c7b2f810db2ecf2256b1b13b28efb5faf43f97d1c681eb77823a0a4494e4ab9",
    "7795a97450fecd9779f3d821858fbc2d1a3bf1dd602617d95b685ccbcabc302f",
    "8ad598c73ad796e0d8280b082cebd82a630d73e73cd3c70057938a6501bba5d7",
    "4767a3b9b1b2422b002dc4aa68fc7141452950946d1da8f950880b92c91fd305",
    "2f3bc50670455534dcaedc9dcd0517b71152f319d0cec8625f21c51d23eaf4b9",
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
