pkgname = "quickshell"
pkgver = "0.3.2"
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
sha256 = "f14115a73c9fff6aa6399f924b632e88c3ce2cead2657f814a7825341f35baad"
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSE")
