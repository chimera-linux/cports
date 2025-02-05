pkgname = "spice-gtk"
pkgver = "0.42"
pkgrel = 2
build_style = "meson"
configure_args = [
    "-Dbuiltin-mjpeg=false",
    "-Dcoroutine=gthread",
    "-Degl=enabled",
    "-Dgtk=enabled",
    "-Dintrospection=enabled",
    "-Dlibcap-ng=enabled",
    "-Dlz4=enabled",
    "-Dopus=enabled",
    "-Dpolkit=enabled",
    "-Dsasl=enabled",
    "-Dvapi=enabled",
    "-Dsmartcard=enabled",
    "-Dwayland-protocols=enabled",
    "-Dwebdav=disabled",  # needs libphodav
]
hostmakedepends = [
    "asciidoc",
    "gettext",
    "gobject-introspection",
    "gtk-doc-tools",
    "libcap-progs",
    "meson",
    "perl",
    "pkgconf",
    "python-six",
]
makedepends = [
    "acl-devel",
    "gdk-pixbuf-devel",
    "gobject-introspection-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libcacard-devel",
    "libcap-ng-devel",
    "libepoxy-devel",
    "libjpeg-turbo-devel",
    "libsasl-devel",
    "libusb-devel",
    "libva-devel",
    "lz4-devel",
    "opus-devel",
    "polkit-devel",
    "spice-devel",
    "spice-protocol",
    "usbredir-devel",
    "usbutils",
    "vala-devel",
    "wayland-protocols",
]
pkgdesc = "GTK+3 widget for SPICE remote desktop client"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.freedesktop.org/spice/spice-gtk"
source = f"https://www.spice-space.org/download/gtk/spice-gtk-{pkgver}.tar.xz"
sha256 = "9380117f1811ad1faa1812cb6602479b6290d4a0d8cc442d44427f7f6c0e7a58"
file_modes = {
    "usr/libexec/spice-client-glib-usb-acl-helper": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/libexec/spice-client-glib-usb-acl-helper": {
        "security.capability": "cap_fowner+ep",
    },
}
# FIXME: crashes virt-manager sometimes, to be investigated
hardening = ["!int"]
options = ["linkundefver"]


@subpackage("spice-gtk-devel")
def _(self):
    return self.default_devel()
