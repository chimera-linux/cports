pkgname = "g4music"
pkgver = "4.3.1"
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
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/neithern/g4music"
source = f"{url}/-/archive/v{pkgver}/g4music-v{pkgver}.tar.gz"
sha256 = "a4aa9db0923ba04b362f45bbe2b777cd6a163a6f209c1bad0db3ea6727f450a0"
