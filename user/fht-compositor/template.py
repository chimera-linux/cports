pkgname = "fht-compositor"
pkgver = "25.10.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "libdisplay-info-devel",
    "libinput-devel",
    "libseat-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "pipewire-devel",
    "pixman-devel",
    "rust-std",
    "udev-devel",
]
depends = ["so:libEGL.so.1!mesa-egl-libs", "xwayland-satellite"]
pkgdesc = "Dynamic tiling Wayland compositor"
license = "GPL-3.0-only"
url = "https://github.com/nferhat/fht-compositor"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6ed6816a8e003b2d0b1675475bd73f5da14e5c6bd255573f7e7c154acd9adb46"
hardening = ["vis", "cfi"]


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/fht-compositor")
    self.install_license("LICENSE")
    self.install_file(
        "res/systemd/fht-compositor.desktop", "usr/share/wayland-sessions"
    )
    self.install_file(
        "res/fht-compositor.portal", "usr/share/xdg-desktop-portal/portals"
    )
    self.install_file(
        "res/fht-compositor-portals.conf", "usr/share/xdg-desktop-portal"
    )
