pkgname = "pcsx2"
pkgver = "1.7.5571"
pkgrel = 0
# pcsx2 doesn't support anything else
archs = ["x86_64"]
build_style = "cmake"
configure_args = [
    # disables debug mode
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_DISABLE_PRECOMPILE_HEADERS=ON",
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
_patches = "958d1c0ba868642e5c7557a7b7eab61dab123182"
_glslang = "11.12.0"
_gtest = "v1.14.0"
_rcheevos = "3cadf84c30bbc050c0fec79d26e1c8ff504bda42"
_fastfloat = "v6.1.0"
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
    "3564b0716846be582ffb51295d5741368340766dfd21c2c3fc8aaa76da085d07",
    "bcae748a2d3a41738cb18d419a3ae5a62095bd3e1660198c6a3986a0be6213e6",
    "7795a97450fecd9779f3d821858fbc2d1a3bf1dd602617d95b685ccbcabc302f",
    "8ad598c73ad796e0d8280b082cebd82a630d73e73cd3c70057938a6501bba5d7",
    "f2e623936167b7300c4b65abf6ea096218d2492310438eb3932a76b3cc804ecb",
    "a9c8ca8ca7d68c2dbb134434044f9c66cfd4c383d5e85c36b704d30f6be82506",
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
