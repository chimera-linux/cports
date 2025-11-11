pkgname = "dolphin-emu"
pkgver = "2506a"
pkgrel = 3
# others have no jit support (so too slow)
archs = ["aarch64", "x86_64"]
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DCMAKE_BUILD_TYPE=Release",
    "-DDISTRIBUTOR=chimera-linux.org",
    "-DENABLE_ANALYTICS=ON",
    "-DENABLE_AUTOUPDATE=OFF",
    "-DENABLE_TESTS=OFF",
    "-DUSE_SANITIZERS=OFF",
    "-DWITH_SANITIZER=OFF",
    # use system libs by default
    "-DUSE_SYSTEM_LIBS=ON",
    # wants 2.x, we have 3.x
    "-DUSE_SYSTEM_MBEDTLS=OFF",
    # mismatch in headers
    "-DUSE_SYSTEM_LIBMGBA=OFF",
    # not packaged
    "-DUSE_SYSTEM_CUBEB=OFF",
]
hostmakedepends = [
    "clang-tools-extra",
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "bluez-devel",
    "bzip2-devel",
    "curl-devel",
    "enet-devel",
    "ffmpeg-devel",
    "fmt-devel",
    "hidapi-devel",
    "libevdev-devel",
    "libpulse-devel",
    "libspng-devel",
    "libxi-devel",
    "llvm-devel",
    "lz4-devel",
    "lzo-devel",
    "mesa-devel",
    "miniupnpc-devel",
    "minizip-ng-devel",
    "pugixml-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "sdl2-compat-devel",
    "sfml-devel",
    "speexdsp-devel",
    "udev-devel",
    "xxhash-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zlib-ng-devel",
    "zstd-devel",
]
pkgdesc = "GameCube and Wii emulator"
license = "GPL-3.0-only"
url = "https://dolphin-emu.org"
_commit_cubeb = "54217bca3f3e0cd53c073690a23dd25d83557909"
_commit_tinygltf = "c5641f2c22d117da7971504591a8f6a41ece488b"
_commit_implot = "18c72431f8265e2b0b5378a3a73d8a883b2175ff"
_commit_rcheevos = "0115d9198ff7a73ff6568027dfb948ef6031818c"
_commit_spirv = "ebe2aa0cd80f5eb5cd8a605da604cacf72205f3b"
_commit_vulkan_memory = "3bab6924988e5f19bf36586a496156cf72f70d9f"
_commit_mgba = "8739b22fbc90fdf0b4f6612ef9c0520f0ba44a51"
source = [
    f"https://github.com/dolphin-emu/dolphin/archive/refs/tags/{pkgver}.tar.gz",
    f"https://github.com/mozilla/cubeb/archive/{_commit_cubeb}.tar.gz",
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
    "Externals/tinygltf/tinygltf",
    "Externals/implot/implot",
    "Externals/rcheevos/rcheevos",
    "Externals/spirv_cross/SPIRV-Cross",
    "Externals/VulkanMemoryAllocator",
    "Externals/mGBA/mgba",
]
sha256 = [
    "0531c69ad0261a62ac4c051471e3d597b720eb5c93b4a04d4b028db2d0b4a179",
    "a795511bf56183ff7bad8fb2d2836ca5bb158e12ddd519caced62946ffa69c83",
    "6352803f1ed18d479ea93abf96ac75c0222a21403be22840bde1072ee5935dfa",
    "4787c77e6050f3bdc19f39eecf87d5b321bd3096321142b63f8169e1aa8f9b34",
    "81d5d35e8b03194c103ceaedab1f37c473062d0907b496c50481f862f80c654d",
    "ff848426a2eabfa0dfb5ee961440210f6cdec190883ed438ee7252ba595c9128",
    "618dc35e4f571a508575fc1fc914eb15ab513e4443986509aff08dfb8844ba24",
    "07e73f02198affccf83cc9740d377b78ba27866b0d654a5e55cafae69d1dfa1c",
]
# for some reason only -lz-ng is passed but the normal symbols are used
tool_flags = {"LDFLAGS": ["-lz"]}
hardening = ["!int"]


def post_install(self):
    self.install_file("Data/51-usb-device.rules", "usr/lib/udev/rules.d")
