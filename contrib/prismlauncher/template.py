pkgname = "prismlauncher"
pkgver = "7.0"
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
    "zlib-devel",
]
pkgdesc = "Minecraft launcher with multiple instances support"
maintainer = "aurelia <git@elia.garden>"
license = "GPL-3.0-or-later"
url = "https://github.com/PrismLauncher/PrismLauncher"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "aef3d368aea8c5c65d6db0d258ef3d0a2965a009f1311568190d2b557ec01833"
