pkgname = "g4music"
pkgver = "3.9.1"
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
sha256 = "50574f49505ba239da4f7bdfb57e2199e74e40ec8e10feb4953fcdf529401b22"
