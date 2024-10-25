pkgname = "prismlauncher"
pkgver = "9.1"
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
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtnetworkauth-devel",
    "qt6-qtsvg-devel",
    "quazip-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Minecraft launcher with multiple instances support"
maintainer = "aurelia <git@elia.garden>"
license = "GPL-3.0-or-later"
url = "https://github.com/PrismLauncher/PrismLauncher"
source = f"{url}/releases/download/{pkgver}/prismlauncher-{pkgver}.tar.gz"
sha256 = "0aac56ec6b039e28f0605e7d86ebf602ee28dd9e4c7a16915ca974104954e832"


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
