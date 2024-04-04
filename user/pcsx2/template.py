pkgname = "pcsx2"
pkgver = "1.7.5671"
pkgrel = 1
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
_patches = "f5300ed085d38bce33c94faad2cd3b155b5c344b"
_glslang = "11.12.0"
_gtest = "v1.14.0"
_fastfloat = "v6.1.1"
source = [
    f"https://github.com/PCSX2/pcsx2/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://github.com/PCSX2/pcsx2_patches/archive/{_patches}.tar.gz",
    f"https://github.com/KhronosGroup/glslang/archive/{_glslang}.tar.gz",
    f"https://github.com/google/googletest/archive/refs/tags/{_gtest}.tar.gz",
    f"https://github.com/fastfloat/fast_float/archive/refs/tags/{_fastfloat}.tar.gz",
]
source_paths = [
    ".",
    "patches",
    "3rdparty/glslang/glslang",
    "3rdparty/gtest",
    "3rdparty/fast_float",
]
sha256 = [
    "50642e4a41c3a6f0c37d82353b3bf7a7090c19b96a658b33e7c553161daf009e",
    "02fa94b54d76d7a5c0bb94c790d4212f4b6b98e196d01ba39baf0d9b9490236b",
    "7795a97450fecd9779f3d821858fbc2d1a3bf1dd602617d95b685ccbcabc302f",
    "8ad598c73ad796e0d8280b082cebd82a630d73e73cd3c70057938a6501bba5d7",
    "10159a4a58ba95fe9389c3c97fe7de9a543622aa0dcc12dd9356d755e9a94cb4",
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
    self.install_link("usr/bin/pcsx2", "../lib/PCSX2/pcsx2-qt")
