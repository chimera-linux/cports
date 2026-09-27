pkgname = "fastfetch"
pkgver = "2.69.0"
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
sha256 = "d0e42faf307e39e7b531d632745a56e4eb558a6545f557280099c622562355ee"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
# CFI: dies immediately (ffPlatformPathAddHome at FFlist.c:31:12)
hardening = ["vis", "!cfi"]
