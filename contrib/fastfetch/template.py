pkgname = "fastfetch"
pkgver = "2.10.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TESTS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "chafa-devel",
    "dbus-devel",
    "dconf-devel",
    "ddcutil-devel",
    "libmagick-devel",
    "libpulse-devel",
    "libxrandr-devel",
    "networkmanager-devel",
    "ocl-icd-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
    "xfconf-devel",
    "zlib-devel",
]
depends = ["lscpu"]
pkgdesc = "Neofetch-like system information fetching tool"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://github.com/fastfetch-cli/fastfetch"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d8f8031775c5e39a02522c1d175752640f68b4c7b7fe51b87afaacb9c0ee5f69"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
# TODO: CFI dies immediately (ffPlatformPathAddHome at FFlist.c:31:12)
hardening = ["vis", "!cfi"]
