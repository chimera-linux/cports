pkgname = "fastfetch"
pkgver = "2.45.0"
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
    "xfconf-devel",
    "yyjson-devel",
    "zlib-ng-compat-devel",
]
depends = ["cmd:lscpu!util-linux-lscpu"]
pkgdesc = "Neofetch-like system information fetching tool"
license = "MIT"
url = "https://github.com/fastfetch-cli/fastfetch"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f336ab5fb651fc34759117d9ef081e8c9175cb1538900a8c7b4efdf94a1de85c"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
# CFI: dies immediately (ffPlatformPathAddHome at FFlist.c:31:12)
hardening = ["vis", "!cfi"]
