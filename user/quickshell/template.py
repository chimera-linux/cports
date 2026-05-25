pkgname = "quickshell"
pkgver = "0.3.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DDISTRIBUTOR=Chimera Linux",
    "-DHYPRLAND=OFF",
    "-DSCREENCOPY_HYPRLAND_TOPLEVEL=OFF",
    "-DINSTALL_QML_PREFIX=lib/qt6/qml",
    "-DUSE_JEMALLOC=OFF",
    "-DBUILD_TESTING=ON",
    # https://github.com/quickshell-mirror/quickshell/issues/491
    "-DNO_PCH=ON",
]
make_check_args = ["-E", "popupwindow"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
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
pkgdesc = "QtQuick toolkit for desktop shells"
license = "LGPL-3.0-only"
url = "https://quickshell.org"
source = (
    f"https://git.outfoxxed.me/quickshell/quickshell/archive/v{pkgver}.tar.gz"
)
sha256 = "f4821f9084cab04bd2b5384cc92b9726aecc4ce3eb27200dca24edc67da3b6e5"
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSE")
