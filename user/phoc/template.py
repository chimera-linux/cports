pkgname = "phoc"
pkgver = "0.51.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dembed-wlroots=disabled"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "xwayland",
]
makedepends = [
    "glib-devel",
    "gmobile-devel",
    "gnome-desktop-devel",
    "libinput-devel",
    "udev-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.19-devel",
]
# TODO: only mutter's schemas are used, split it
depends = [
    "dbus",
    "gsettings-desktop-schemas",
    "mutter",
]
pkgdesc = "Phone compositor for the Phosh shell"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/Phosh/phoc"
source = f"https://sources.phosh.mobi/releases/phoc/phoc-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "cf03d7d8b63def0bef0509d217726963693877d6cc985d94eb27ddc3368693cc"
# needs fullblown EGL
options = ["!check"]
