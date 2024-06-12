pkgname = "dolphin-emu"
pkgver = "5.0_git20240612"
pkgrel = 0
# others have no jit support (so too slow)
archs = ["aarch64", "x86_64"]
_commit = "71171a9e4ddc51a854efe34c3986364104c42ebf"
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DDISTRIBUTOR=chimera-linux.org",
    "-DENABLE_ANALYTICS=ON",
    "-DENABLE_AUTOUPDATE=OFF",
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
    "gtest-devel",
    "hidapi-devel",
    "libcurl-devel",
    "libevdev-devel",
    "libpulse-devel",
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
    "spng-devel",
    "udev-devel",
    "xxhash-devel",
    "xz-devel",
    "zlib-devel",
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
_commit_rcheevos = "a6cdbb4a529d85b74777597fcff037dde7bef66b"
_commit_spirv = "50b4d5389b6a06f86fb63a2848e1a7da6d9755ca"
_commit_vulkan_memory = "498e20dfd1343d99b9115201034bb0219801cdec"
_commit_zlib_ng = "ce01b1e41da298334f8214389cc9369540a7560f"
_commit_mgba = "8739b22fbc90fdf0b4f6612ef9c0520f0ba44a51"
source = [
    f"https://github.com/dolphin-emu/dolphin/archive/{_commit}.tar.gz",
    f"https://github.com/mozilla/cubeb/archive/{_commit_cubeb}.tar.gz",
    f"https://github.com/lsalzman/enet/archive/{_commit_enet}.tar.gz",
    f"https://github.com/syoyo/tinygltf/archive/{_commit_tinygltf}.tar.gz",
    f"https://github.com/epezent/implot/archive/{_commit_implot}.tar.gz",
    f"https://github.com/RetroAchievements/rcheevos/archive/{_commit_rcheevos}.tar.gz",
    f"https://github.com/KhronosGroup/SPIRV-Cross/archive/{_commit_spirv}.tar.gz",
    f"https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator/archive/{_commit_vulkan_memory}.tar.gz",
    f"https://github.com/zlib-ng/zlib-ng/archive/{_commit_zlib_ng}.tar.gz",
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
    "Externals/zlib-ng/zlib-ng",
    "Externals/mGBA/mgba",
]
sha256 = [
    "41af06851d9245323cf78648d1217dfe3531c09dd0724e84037b50467a79cf4d",
    "a795511bf56183ff7bad8fb2d2836ca5bb158e12ddd519caced62946ffa69c83",
    "526c5af3980edfaebb510119c3311a9062d33ca5599e9f137a88e0d8a3be67a6",
    "6352803f1ed18d479ea93abf96ac75c0222a21403be22840bde1072ee5935dfa",
    "af51940ae6482c0e96ffb4309982fa309f9aa383cd8f980081681010c8c3a835",
    "bfc91b8712d6e14f5dd90e471bb92b59e8904960015c1b366b1e62f15ff7a181",
    "ed27481a78470fe9905cdfec8fd2ebb6c8f68a17377c2879527c2fcb2a01751c",
    "4cb34c92b57d132d3200aa8c9b7f758e963eaeb31b6127d6edd0cd0902dc177e",
    "64a6d355d2d5c9449fc047e5bb0ca32875fc385061dfaf1df3aa791577b7ff5e",
    "07e73f02198affccf83cc9740d377b78ba27866b0d654a5e55cafae69d1dfa1c",
]
hardening = ["!int"]


def post_install(self):
    self.install_file("Data/51-usb-device.rules", "usr/lib/udev/rules.d")
