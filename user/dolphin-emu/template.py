pkgname = "dolphin-emu"
pkgver = "2412"
pkgrel = 0
# others have no jit support (so too slow)
archs = ["aarch64", "x86_64"]
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DDISTRIBUTOR=chimera-linux.org",
    "-DENABLE_ANALYTICS=ON",
    "-DENABLE_AUTOUPDATE=OFF",
    "-DENABLE_TESTS=OFF",
    "-DUSE_SANITIZERS=OFF",
    "-DWITH_SANITIZER=OFF",
]
hostmakedepends = [
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "bluez-devel",
    "bzip2-devel",
    "ffmpeg-devel",
    "fmt-devel",
    "hidapi-devel",
    "libcurl-devel",
    "libevdev-devel",
    "libpulse-devel",
    "libspng-devel",
    "libxi-devel",
    "lz4-devel",
    "lzo-devel",
    "mesa-devel",
    "minizip-ng-devel",
    "pugixml-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "sdl-devel",
    "speexdsp-devel",
    "udev-devel",
    "xxhash-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zlib-ng-devel",
    "zstd-devel",
]
pkgdesc = "GameCube and Wii emulator"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-only"
url = "https://dolphin-emu.org"
_commit_cubeb = "54217bca3f3e0cd53c073690a23dd25d83557909"
_commit_enet = "2a85cd64459f6ba038d233a634d9440490dbba12"
_commit_tinygltf = "c5641f2c22d117da7971504591a8f6a41ece488b"
_commit_implot = "cc5e1daa5c7f2335a9460ae79c829011dc5cef2d"
_commit_rcheevos = "d54cf8f1059cebc90a6f5ecdf03df69259f22054"
_commit_spirv = "50b4d5389b6a06f86fb63a2848e1a7da6d9755ca"
_commit_vulkan_memory = "009ecd192c1289c7529bff248a16cfe896254816"
_commit_mgba = "8739b22fbc90fdf0b4f6612ef9c0520f0ba44a51"
source = [
    f"https://github.com/dolphin-emu/dolphin/archive/refs/tags/{pkgver}.tar.gz",
    f"https://github.com/mozilla/cubeb/archive/{_commit_cubeb}.tar.gz",
    f"https://github.com/lsalzman/enet/archive/{_commit_enet}.tar.gz",
    f"https://github.com/syoyo/tinygltf/archive/{_commit_tinygltf}.tar.gz",
    f"https://github.com/epezent/implot/archive/{_commit_implot}.tar.gz",
    f"https://github.com/RetroAchievements/rcheevos/archive/{_commit_rcheevos}.tar.gz",
    f"https://github.com/KhronosGroup/SPIRV-Cross/archive/{_commit_spirv}.tar.gz",
    f"https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator/archive/{_commit_vulkan_memory}.tar.gz",
    f"https://github.com/mgba-emu/mgba/archive/{_commit_mgba}.tar.gz",
]
source_paths = [
    ".",
    "Externals/cubeb/cubeb",
    "Externals/enet/enet",
    "Externals/tinygltf/tinygltf",
    "Externals/implot/implot",
    "Externals/rcheevos/rcheevos",
    "Externals/spirv_cross/SPIRV-Cross",
    "Externals/VulkanMemoryAllocator",
    "Externals/mGBA/mgba",
]
sha256 = [
    "6aafc7d3b6f735a727db26c329679d4973b1b15e028c82e4452c33c4eb9fefa4",
    "a795511bf56183ff7bad8fb2d2836ca5bb158e12ddd519caced62946ffa69c83",
    "526c5af3980edfaebb510119c3311a9062d33ca5599e9f137a88e0d8a3be67a6",
    "6352803f1ed18d479ea93abf96ac75c0222a21403be22840bde1072ee5935dfa",
    "af51940ae6482c0e96ffb4309982fa309f9aa383cd8f980081681010c8c3a835",
    "bf8e6e9afa865c51ab796c8329df206297b329f008ef0c1308c642480fb2d289",
    "ed27481a78470fe9905cdfec8fd2ebb6c8f68a17377c2879527c2fcb2a01751c",
    "5ed5125086a92666f1698df907a29f54f11197c382996094b556a1b22186ecaf",
    "07e73f02198affccf83cc9740d377b78ba27866b0d654a5e55cafae69d1dfa1c",
]
# for some reason only -lz-ng is passed but the normal symbols are used
tool_flags = {"LDFLAGS": ["-lz"]}
hardening = ["!int"]


def post_install(self):
    self.install_file("Data/51-usb-device.rules", "usr/lib/udev/rules.d")
