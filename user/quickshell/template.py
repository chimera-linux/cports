pkgname = "quickshell"
pkgver = "0.3.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DDISTRIBUTOR=Chimera Linux",
    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
    "-DINSTALL_QML_PREFIX=lib/qt6/qml",
    # PCH breaks polkit build with clang, see
    # https://github.com/quickshell-mirror/quickshell/issues/491
    "-DNO_PCH=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "qt6-qtshadertools",
    "spirv-tools",
    "wayland-progs",
]
makedepends = [
    "cli11",
    "cpptrace-devel",
    "glib-devel",
    "jemalloc-devel",
    "libdrm-devel",
    "libxcb-devel",
    "linux-pam-devel",
    "mesa-gbm-devel",
    "pipewire-devel",
    "polkit-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "vulkan-headers",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["qt6-qtsvg"]
pkgdesc = "QtQuick toolkit for making desktop shells on Wayland and X11"
license = "LGPL-3.0-only"
url = "https://quickshell.org"
source = (
    f"https://git.outfoxxed.me/quickshell/quickshell/archive/v{pkgver}.tar.gz"
)
sha256 = "f4821f9084cab04bd2b5384cc92b9726aecc4ce3eb27200dca24edc67da3b6e5"
# TODO
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSE")
