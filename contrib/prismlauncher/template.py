pkgname = "prismlauncher"
pkgver = "8.0"
pkgrel = 0
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
sha256 = "462f35eeda6e107b5f23a97500accf43e4227a0fb40145b29d0895bcfe3372b0"
