pkgname = "fastfetch"
pkgver = "2.22.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TESTS=ON", "-DENABLE_SYSTEM_YYJSON=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "chafa-devel",
    "dbus-devel",
    "dconf-devel",
    "ddcutil-devel",
    "elfutils-devel",
    "libmagick-devel",
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
depends = ["lscpu"]
pkgdesc = "Neofetch-like system information fetching tool"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://github.com/fastfetch-cli/fastfetch"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ada2d56e14ce2eadaa88573dada5881684ceeaaa11df23017631b91dfa745d00"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
# CFI: dies immediately (ffPlatformPathAddHome at FFlist.c:31:12)
hardening = ["vis", "!cfi"]
