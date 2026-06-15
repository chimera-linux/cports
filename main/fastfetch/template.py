pkgname = "fastfetch"
pkgver = "2.64.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_FLASHFETCH=OFF",
    "-DBUILD_TESTS=ON",
    "-DENABLE_SYSTEM_YYJSON=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "chafa-devel",
    "dbus-devel",
    "dconf-devel",
    "ddcutil-devel",
    "elfutils-devel",
    "imagemagick-devel",
    "libpulse-devel",
    "libxrandr-devel",
    "ocl-icd-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
    "yyjson-devel",
    "zlib-ng-compat-devel",
]
depends = ["cmd:lscpu!util-linux-lscpu"]
pkgdesc = "Neofetch-like system information fetching tool"
license = "MIT"
url = "https://github.com/fastfetch-cli/fastfetch"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "28db81d6568f28281d9aab9e88d5a4c7892d519c54b8739eef17953cce6802d0"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
# CFI: dies immediately (ffPlatformPathAddHome at FFlist.c:31:12)
hardening = ["vis", "!cfi"]
