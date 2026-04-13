pkgname = "dolphin-emu"
pkgver = "2603a"
pkgrel = 0
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
    "cmake",
    "gettext",
    "glslang-progs",
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
    "glslang-devel",
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
    "sdl3-devel",
    "sfml-devel",
    "speexdsp-devel",
    "spirv-tools-devel",
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
_commit_imgui = "45acd5e0e82f4c954432533ae9985ff0e1aad6d5"
_commit_implot = "3da8bd34299965d3b0ab124df743fe3e076fa222"
_commit_rcheevos = "926e4608f8dca7989267c787bbefb3ab1c835ac5"
_commit_spirv = "ebe2aa0cd80f5eb5cd8a605da604cacf72205f3b"
_commit_vulkan_memory = "3bab6924988e5f19bf36586a496156cf72f70d9f"
_commit_mgba = "0b40863f64d0940f333fa1c638e75f86f8a26a33"
_commit_cpp_ipc = "ce0773b3e6d5abaa8d104100c5704321113853ca"
_commit_cpp_optparse = "2265d647232249a53a03b411099863ceca35f0d3"
_commit_watcher = "b03bdcfc11549df595b77239cefe2643943a3e2f"
source = [
    f"https://github.com/dolphin-emu/dolphin/archive/refs/tags/{pkgver}.tar.gz",
    f"https://github.com/mozilla/cubeb/archive/{_commit_cubeb}.tar.gz",
    f"https://github.com/syoyo/tinygltf/archive/{_commit_tinygltf}.tar.gz",
    f"https://github.com/ocornut/imgui/archive/{_commit_imgui}.tar.gz",
    f"https://github.com/epezent/implot/archive/{_commit_implot}.tar.gz",
    f"https://github.com/RetroAchievements/rcheevos/archive/{_commit_rcheevos}.tar.gz",
    f"https://github.com/KhronosGroup/SPIRV-Cross/archive/{_commit_spirv}.tar.gz",
    f"https://github.com/GPUOpen-LibrariesAndSDKs/VulkanMemoryAllocator/archive/{_commit_vulkan_memory}.tar.gz",
    f"https://github.com/mgba-emu/mgba/archive/{_commit_mgba}.tar.gz",
    f"https://github.com/mutouyun/cpp-ipc/archive/{_commit_cpp_ipc}.tar.gz",
    f"https://github.com/weisslj/cpp-optparse/archive/{_commit_cpp_optparse}.tar.gz",
    f"https://github.com/e-dant/watcher/archive/{_commit_watcher}.tar.gz",
]
source_paths = [
    ".",
    "Externals/cubeb/cubeb",
    "Externals/tinygltf/tinygltf",
    "Externals/imgui/imgui",
    "Externals/implot/implot",
    "Externals/rcheevos/rcheevos",
    "Externals/spirv_cross/SPIRV-Cross",
    "Externals/VulkanMemoryAllocator",
    "Externals/mGBA/mgba",
    "Externals/cpp-ipc/cpp-ipc",
    "Externals/cpp-optparse/cpp-optparse",
    "Externals/watcher/watcher",
]
sha256 = [
    "ae6ca2e812357ae56a31c00498a984e42b5c46946050ae4a946c7e3f63d1ec7b",
    "a795511bf56183ff7bad8fb2d2836ca5bb158e12ddd519caced62946ffa69c83",
    "6352803f1ed18d479ea93abf96ac75c0222a21403be22840bde1072ee5935dfa",
    "97484925aec2f4d3e913d6644d46b234f8d6d8d98c6aa9c50109e0f0df772090",
    "4700b44ef00ca2feba0b35a31922c240045bbeb900da5b3eb3830b56871ada45",
    "11e5fc43c4676289ff4637c04a9f43070235006d826c363628dcb194d5182ebd",
    "ff848426a2eabfa0dfb5ee961440210f6cdec190883ed438ee7252ba595c9128",
    "618dc35e4f571a508575fc1fc914eb15ab513e4443986509aff08dfb8844ba24",
    "9b59ed1422914f605ce912e9cafcd84d1c5b1bf9abcf0fef1b49e1d810f6f5e5",
    "01613a09deb56de754d5f3b284cb7d21c7286dbb61cd148f26515b1a0bd04d79",
    "6f38fff3c4d2788eead7a28626b3220cc4c101510fc984678ad55f77756b107e",
    "61e97c12c3d23f2b6588d99ce61c8ad462b4382f979d14c7a338a11af507edd1",
]
# for some reason only -lz-ng is passed but the normal symbols are used
tool_flags = {"LDFLAGS": ["-lz"]}
hardening = ["!int"]


def post_install(self):
    self.install_file("Data/51-usb-device.rules", "usr/lib/udev/rules.d")
