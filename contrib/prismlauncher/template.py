pkgname = "prismlauncher"
pkgver = "7.2"
pkgrel = 1
build_style = "cmake"
configure_env = {"JAVA_HOME": "/usr/lib/jvm/java-17-openjdk"}
hostmakedepends = [
    "cmake",
    "ninja",
    "extra-cmake-modules",
    "qt6-qtbase",
    "openjdk17-jdk",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qt5compat-devel",
    "qt6-qtsvg-devel",
    "quazip-devel",
    "zlib-devel",
]
pkgdesc = "Minecraft launcher with multiple instances support"
maintainer = "aurelia <git@elia.garden>"
license = "GPL-3.0-or-later"
url = "https://github.com/PrismLauncher/PrismLauncher"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "5733b55c4532286813a6fb7de2f3a38e6f6db743a251919c8b646d32a84514b4"
