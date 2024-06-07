pkgname = "fastfetch"
pkgver = "2.15.0"
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
sha256 = "b42392c66eb7292db8b56715a072908b91d72385e6fdeae56fa7653adfc5428d"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
# TODO: CFI dies immediately (ffPlatformPathAddHome at FFlist.c:31:12)
hardening = ["vis", "!cfi"]
