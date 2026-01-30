pkgname = "prismlauncher"
pkgver = "11.0.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DLauncher_BUILD_PLATFORM=chimeralinux",
]
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
    "libarchive-devel",
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
sha256 = "8956e9351bcb0472fc9c2c61ae68aa2960f27f7cabb1cacd86dd2af1c233a064"


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
