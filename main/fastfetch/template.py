pkgname = "fastfetch"
pkgver = "2.50.2"
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
sha256 = "e59f2a2bdd5834ef40adb9fb6680820c268ff60ca0534469c5ea4b86775c83db"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
# CFI: dies immediately (ffPlatformPathAddHome at FFlist.c:31:12)
hardening = ["vis", "!cfi"]
