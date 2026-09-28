pkgname = "prismlauncher"
pkgver = "11.0.3"
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
sha256 = "78c368140a4d49bf2a12ef0e03d045c6723fe8e5a5c9590668fb63ee0a264ef2"


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
