pkgname = "prismlauncher"
pkgver = "8.4"
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
]
makedepends = [
    "cmark-devel",
    "cmark",  # cmake detection
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "quazip-devel",
    "zlib-devel",
]
pkgdesc = "Minecraft launcher with multiple instances support"
maintainer = "aurelia <git@elia.garden>"
license = "GPL-3.0-or-later"
url = "https://github.com/PrismLauncher/PrismLauncher"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "a4df9059559df2e410ddf933e05fe4bffaa01631c6eeb55e63af4a2d0d719726"
