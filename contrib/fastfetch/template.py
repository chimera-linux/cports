pkgname = "fastfetch"
pkgver = "2.20.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TESTS=ON", "-DENABLE_SYSTEM_YYJSON=ON"]
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
    "yyjson-devel",
    "zlib-ng-compat-devel",
]
depends = ["lscpu"]
pkgdesc = "Neofetch-like system information fetching tool"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://github.com/fastfetch-cli/fastfetch"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "461f64bda6ab4a33085b1b75afd01e72a7d0556b678852b95fbea4916ceec2a8"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
# CFI: dies immediately (ffPlatformPathAddHome at FFlist.c:31:12)
hardening = ["vis", "!cfi"]
