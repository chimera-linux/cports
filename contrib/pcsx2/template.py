pkgname = "pcsx2"
pkgver = "1.7.5082"
pkgrel = 0
# pcsx2 doesn't support anything else
archs = ["x86_64"]
build_style = "cmake"
configure_args = [
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
make_build_args = ["unittests"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "extra-cmake-modules",
    "ffmpeg-devel",
    "libaio-devel",
    "libcurl-devel",
    "libpcap-devel",
    "libpng-devel",
    "libpulse-devel",
    "libwebp-devel",
    "libzip-devel",
    "libzip-progs",
    "zstd-devel",
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
_patches = "4c2e128a675e567e69a7c69afcb1770097105191"
_fmt = "9.1.0"
_glslang = "11.12.0"
_gtest = "v1.14.0"
_rcheevos = "43f8c2a2a0750561786f17dd35af8755716705aa"
_fastfloat = "v5.2.0"
source = [
    f"https://github.com/PCSX2/pcsx2/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/PCSX2/pcsx2_patches/archive/{_patches}.tar.gz",
    f"https://github.com/fmtlib/fmt/archive/{_fmt}.tar.gz",
    f"https://github.com/KhronosGroup/glslang/archive/{_glslang}.tar.gz",
    f"https://github.com/google/googletest/archive/refs/tags/{_gtest}.tar.gz",
    f"https://github.com/RetroAchievements/rcheevos/archive/{_rcheevos}.tar.gz",
    f"https://github.com/fastfloat/fast_float/archive/refs/tags/{_fastfloat}.tar.gz",
]
source_paths = [
    ".",
    "patches",
    "3rdparty/fmt/fmt",
    "3rdparty/glslang/glslang",
    "3rdparty/gtest",
    "3rdparty/rcheevos/rcheevos",
    "3rdparty/fast_float",
]
sha256 = [
    "5b9f6748288f5f638f57a93c0cc333a9f1b2589de42ccc7560966188c29ea043",
    "7cafa594bbfac84d1170e166539ccf1f03562eadea26b9849aa184bcc5c9ea16",
    "5dea48d1fcddc3ec571ce2058e13910a0d4a6bab4cc09a809d8b1dd1c88ae6f2",
    "7795a97450fecd9779f3d821858fbc2d1a3bf1dd602617d95b685ccbcabc302f",
    "8ad598c73ad796e0d8280b082cebd82a630d73e73cd3c70057938a6501bba5d7",
    "b526312b9bb8c47c5a581d60b16c3c33d5ce577fb7c674c42fcefd9e119b5adc",
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
