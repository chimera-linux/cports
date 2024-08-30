pkgname = "g4music"
pkgver = "3.9"
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
sha256 = "cdc1a79ca579cc211d5da596db4b5791d0899ceafc19dd9028f63b3d25232a36"
