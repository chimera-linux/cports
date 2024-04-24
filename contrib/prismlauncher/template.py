pkgname = "prismlauncher"
pkgver = "8.3"
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
sha256 = "4d587122f673ee4daea5aa098bd3da0f51989dbb600560146dd8a0375491cea0"
