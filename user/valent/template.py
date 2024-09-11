pkgname = "valent"
pkgver = "1.0.0_alpha"
_alphaver = "46"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dplugin_bluez=true",
    "-Dplugin_pulseaudio=false",
    "-Dvapi=true",
]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "libxml2-progs",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "evolution-data-server-devel",
    "gdk-pixbuf-devel",
    "glib-devel",
    "gnutls-devel",
    "gobject-introspection",
    "gstreamer-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libpeas2-devel",
    "libphonenumber-devel",
    "libportal-devel",
    "pipewire-devel",
    "tracker-devel",
]
pkgdesc = "GTK-based implementation of the KDE Connect protocol"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/andyholmes/valent"
source = (
    f"{url}/archive/refs/tags/v{pkgver.replace("_", ".")}.{_alphaver}.tar.gz"
)
sha256 = "650ae21717644ec5036345645c6b00a8f59368e605dd202924be95c34e896e3c"
