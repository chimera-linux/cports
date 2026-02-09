pkgname = "quickshell"
pkgver = "0.2.1"
pkgrel = 0
build_style = "cmake"
configure_args = [  # https://git.outfoxxed.me/quickshell/quickshell/src/branch/master/BUILD.md
    '-DDISTRIBUTOR="Chimera Linux"',
    "-DDISTRIBUTOR_DEBUGINFO_AVAILABLE=YES",
    "-DCMAKE_BUILD_TYPE=RelWithDebInfo",
    "-DCRASH_REPORTER=OFF",  # depends on google-breakpad
    "-DUSE_JEMALLOC=ON",  # depends on jemalloc
    "-DSOCKETS=ON",
    "-DWAYLAND=ON",  # depends on qt6wayland, wayland, wayland-scanner, wayland-protocols
    "-DWAYLAND_WLR_LAYERSHELL=ON",  # zwlr-layer-shell-v1 protocol
    "-DWAYLAND_SESSION_LOCK=ON",  # ext-session-lock-v1 protocol
    "-DWAYLAND_TOPLEVEL_MANAGEMENT=ON",  # zwlr-foreign-toplevel-management-v1 protocol
    "-DSCREENCOPY=ON",  # depends on libdrm-devel and qt6-qtbase
    "-DSCREENCOPY_ICC=ON",  # ext-image-copy-capture-v1 protocol
    "-DSCREENCOPY_WLR=ON",  # zwlr-screencopy-v1 protocol
    "-DSCREENCOPY_HYPRLAND_TOPLEVEL=ON",  # hyprland-toplevel-export-v1 protocol
    "-DX11=ON",  # depends on libxcb
    "-DSERVICE_PIPEWIRE=ON",  # depends on libpipewire
    "-DSERVICE_STATUS_NOTIFIER=ON",  # depends on qt6dbus
    "-DSERVICE_MPRIS=ON",  # depends on qt6dbus
    "-DSERVICE_PAM=ON",  # depends on pam
    "-DHYPRLAND=ON",  # requires WAYLAND=ON
    "-DHYPRLAND_GLOBAL_SHORTCUTS=ON",  # hyprland-global-shortcuts-v1 protocol
    "-DHYPRLAND_FOCUS_GRAB=ON",  # hyprland-focus-grab-v1 protocol.
    "-DI3=ON",
    "-DI3_IPC=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "spirv-tools",
    "wayland-progs",
]
makedepends = [
    "cli11",
    "jemalloc-devel",  # memory masking support
    "libdrm-devel",  # screencopy support
    "libxcb-devel",  # X11 support
    "linux-pam-devel",  # PAM support
    "pipewire-devel",  # pipewire support
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtscxml-devel",  # for QML
    "qt6-qtshadertools-devel",
    "qt6-qtwayland-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = [
    "qt6-qtsvg",  # icon and image support
]
pkgdesc = "Flexible QtQuick-based desktop shell toolkit"
license = "LGPL-3.0-only"
url = "https://quickshell.org"
source = (
    f"https://git.outfoxxed.me/quickshell/quickshell/archive/v{pkgver}.tar.gz"
)
sha256 = "d815c5f99f4a0a28545ffaa90464420c773b7c0ab62f713d9d8735a8e7282ca7"


def post_install(self):
    self.install_license("LICENSE")
