pkgname = "fastfetch"
pkgver = "2.56.1"
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
sha256 = "6ffd75c32b2a885fd8497867645ac837ed37d588c94e0df05408cdaa0c8fd2c7"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
# CFI: dies immediately (ffPlatformPathAddHome at FFlist.c:31:12)
hardening = ["vis", "!cfi"]
