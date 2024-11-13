pkgname = "niri"
pkgver = "0.1.10.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "dbus,dinit,xdp-gnome-screencast",
]
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "glib-devel",
    "libdisplay-info-devel",
    "libinput-devel",
    "libseat-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "pango-devel",
    "pipewire-devel",
    "pixman-devel",
    "rust-std",
    "udev-devel",
]
depends = [
    "so:libEGL.so.1!libegl",
]
pkgdesc = "Scrollable-tiling wayland compositor"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://github.com/YaLTeR/niri"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d8854830436a87215b0bc6a60b6d43f350d927a03a2798c75f0fbda228bac8d3"

# TODO: dinit graphical user session service, --notify-fd, etc


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/niri")
    self.install_file("resources/niri.desktop", "usr/share/wayland-sessions")
    self.install_file(
        "resources/niri-portals.conf", "usr/share/xdg-desktop-portal"
    )
