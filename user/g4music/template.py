pkgname = "g4music"
pkgver = "4.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk4-devel",
    "libadwaita-devel",
]
pkgdesc = "GTK4 music player with a fluent adaptive user interface"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/neithern/g4music"
source = f"{url}/-/archive/v{pkgver}/g4music-v{pkgver}.tar.gz"
sha256 = "763d71466f58e43866b82cae28c5fda09c378af10763c3c8078b34f141ea7032"
