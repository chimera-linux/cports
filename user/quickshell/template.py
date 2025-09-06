pkgname = "quickshell"
pkgver = "0.2.0"
_cli11ver = "2.5.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_TESTING=ON",
    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
    "-DCRASH_REPORTER=OFF",  # breakpad
    "-DDISTRIBUTOR=Chimera Linux",
    "-DDISTRIBUTOR_DEBUGINFO_AVAILABLE=YES",
    "-DINSTALL_QML_PREFIX=lib/qt6/qml",
    "-DX11=OFF",
]
make_check_env = {"QT_QPA_PLATFORM": "minimal"}
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "qt6-qtshadertools",
    "spirv-tools",
    "wayland-progs",
]
makedepends = [
    "jemalloc-devel",
    "libdrm-devel",
    "linux-pam-devel",
    "mesa-gbm-devel",
    "pipewire-devel",
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = ["qt6-qtsvg"]
pkgdesc = "QtQuick based desktop shell toolkit"
license = "LGPL-3.0-only"
url = "https://quickshell.org"
source = [
    f"https://git.outfoxxed.me/quickshell/quickshell/archive/v{pkgver}.tar.gz",
    f"https://github.com/CLIUtils/CLI11/archive/refs/tags/v{_cli11ver}.tar.gz",
]
source_paths = [".", "src/launch/CLI11"]
sha256 = [
    "568291b2397e4859ebc8b1d5cdc60fead2ce2da2368342e5f35c19bb1e32834d",
    "17e02b4cddc2fa348e5dbdbb582c59a3486fa2b2433e70a0c3bacb871334fd55",
]


def post_install(self):
    self.uninstall("usr/bin/qs")  # symlink to quickshell
