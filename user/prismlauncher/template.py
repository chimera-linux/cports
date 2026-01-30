pkgname = "prismlauncher"
pkgver = "10.0.2"
pkgrel = 0
build_style = "cmake"
configure_env = {"JAVA_HOME": "/usr/lib/jvm/java-17-openjdk"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "openjdk17-jdk",
    "pkgconf",
    "qt6-qtbase",
    "scdoc",
]
makedepends = [
    "cmark",  # cmake detection
    "cmark-devel",
    "gamemode-devel",
    "qrencode-devel",
    "qt6-qtbase-devel",
    "qt6-qtnetworkauth-devel",
    "qt6-qtsvg-devel",
    "tomlplusplus-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Minecraft launcher with multiple instances support"
license = "GPL-3.0-or-later"
url = "https://github.com/PrismLauncher/PrismLauncher"
source = f"{url}/releases/download/{pkgver}/prismlauncher-{pkgver}.tar.gz"
sha256 = "4b36e8b0345a21a9a8da36633fa5bf4d8f44d992da1529cdfb6bf52a0ff7f33c"


@subpackage("prismlauncher-natives")
def _(self):
    self.subdesc = "native default libs"
    self.install_if = [self.parent]
    self.depends += [
        "so:libglfw.so.3!glfw",
        "so:libjemalloc.so.2!jemalloc",
        "so:libopenal.so.1!openal-soft",
    ]
    self.options = ["empty"]

    return []
