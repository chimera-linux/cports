pkgname = "niri"
pkgver = "25.02"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "dbus,dinit,xdp-gnome-screencast",
]
make_check_args = [*make_build_args]
make_check_env = {"XDG_RUNTIME_DIR": "/tmp"}
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
    "so:libEGL.so.1!mesa-egl-libs",
]
checkdepends = ["xkeyboard-config"]
pkgdesc = "Scrollable-tiling wayland compositor"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-or-later"
url = "https://github.com/YaLTeR/niri"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "602b1f38c6ab01b19e95ac2ef86d7c91dfa9b212437d62fb40def9664c1419d6"
# check may be disabled
options = []

if self.profile().wordsize == 32:
    broken = "weird pipewire api stuff"

if self.profile().arch == "ppc64le":
    # fails some xkeyboard stuff mysteriously? FIXME
    options += ["!check"]

# TODO: dinit graphical user session service, --notify-fd, etc


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/niri")
    self.install_file("resources/niri.desktop", "usr/share/wayland-sessions")
    self.install_file(
        "resources/niri-portals.conf", "usr/share/xdg-desktop-portal"
    )
