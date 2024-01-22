pkgname = "spice-gtk"
pkgver = "0.42"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dcoroutine=gthread",
    "-Dwayland-protocols=enabled",
    "-Dlibcap-ng=enabled",
    "-Dgtk=enabled",
    "-Degl=enabled",
    "-Dlz4=enabled",
    "-Dopus=enabled",
    "-Dsasl=enabled",
    "-Dvapi=enabled",
    "-Dsmartcard=enabled",
    "-Dintrospection=enabled",
    "-Dbuiltin-mjpeg=false",
    "-Dpolkit=disabled",  # uses setuid binaries
    "-Dwebdav=disabled",  # needs libphodav
]
hostmakedepends = [
    "asciidoc",
    "gettext",
    "gobject-introspection",
    "gtk-doc-tools",
    "meson",
    "perl",
    "pkgconf",
    "python-six",
]
makedepends = [
    "acl-devel",
    "gdk-pixbuf-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libcacard-devel",
    "libcap-ng-devel",
    "libepoxy-devel",
    "libgirepository-devel",
    "libjpeg-turbo-devel",
    "libsasl-devel",
    "libusb-devel",
    "libva-devel",
    "lz4-devel",
    "opus-devel",
    "spice-devel",
    "spice-protocol",
    "usbredir-devel",
    "usbutils-devel",
    "vala-devel",
    "wayland-protocols",
]
pkgdesc = "GTK+3 widget for SPICE remote desktop client"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/spice/spice-gtk"
source = f"https://www.spice-space.org/download/gtk/spice-gtk-{pkgver}.tar.xz"
sha256 = "9380117f1811ad1faa1812cb6602479b6290d4a0d8cc442d44427f7f6c0e7a58"
options = ["linkundefver"]


@subpackage("spice-gtk-devel")
def _devel(self):
    return self.default_devel()
