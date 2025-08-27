pkgname = "quickshell"
pkgver = "0.2.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
    "-DCRASH_REPORTER=OFF",
    "-DDISTRIBUTOR_DEBUGINFO_AVAILABLE=YES",
    '-DDISTRIBUTOR="Chimera Linux cports"',
]
hostmakedepends = [
    "cmake",
    "libdrm",
    "mesa-gbm-libs",
    "pipewire-libs",
    "qt6-qtbase",
    "qt6-qtbase-dbus",
    "qt6-qtdeclarative",
    "wayland",
]
makedepends = [
    "pkgconf",
    "qt6-qtshadertools-libs",
    "qt6-qtwayland",
    "spirv-tools",
    "wayland-protocols",
    "wayland-scanner",
]
pkgdesc = "Flexbile QtQuick based desktop shell toolkit"
license = "LGPL-3.0-only"
url = "https://git.outfoxxed.me/quickshell/quickshell"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "568291b2397e4859ebc8b1d5cdc60fead2ce2da2368342e5f35c19bb1e32834d"


def post_install(self):
    self.install_license("LICENSE")
