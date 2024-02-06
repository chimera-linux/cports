pkgname = "waybar"
pkgver = "0.9.24"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemd=disabled",
    "-Dtests=enabled",
    "-Dlibcxx=true",
    "-Ddbusmenu-gtk=enabled",
    "-Dmpd=enabled",
    "-Dcava=disabled",
]
hostmakedepends = ["cmake", "meson", "pkgconf", "scdoc", "wayland-protocols"]
makedepends = [
    "clang-tools-extra",
    "fmt-devel",
    "gobject-introspection",
    "gtkmm3.0-devel",
    "gtk-layer-shell-devel",
    "jsoncpp-devel",
    "libdbusmenu-gtk3",
    "libevdev-devel",
    "libgirepository-devel",
    "libinput-devel",
    "libmpdclient-devel",
    "libnl-devel",
    "libsigc++",
    "libxkbregistry",
    "playerctl-devel",
    "spdlog-devel",
    "udev-devel",
    "upower-devel",
    "wayland-devel",
    "wireplumber-devel",
]
checkdepends = ["catch2", "libdbusmenu-devel"]
pkgdesc = (
    "Wayland bar for Sway and Wlroots based compositors"
)
maintainer = "avgwst <avgwst@tutanota.de>"
license = "MIT"
url = "https://github.com/Alexays/Waybar"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "57aa7860bc066ebf4f3327dafa9841100b098c0dec1dce4baaa1fae63e9b57ae"
# breaks tests
hardening = ["!vis"]


def post_install(self):
    self.install_license("LICENSE")
