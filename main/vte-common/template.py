pkgname = "vte-common"
pkgver = "0.76.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-D_systemd=false",
    "-Dgir=true",
    "-Dvapi=true",
    "-Dgtk4=true",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext-devel",
    "gperf",
    "gobject-introspection",
    "vala",
    "bash",
]
makedepends = [
    "glib-devel",
    "gnutls-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "pcre2-devel",
    "vala-devel",
    "pango-devel",
    "fribidi-devel",
    "icu-devel",
    "lz4-devel",
    "zlib-devel",
    "linux-headers",
]
pkgdesc = "Gtk terminal widget (common files)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Terminal/VTE"
source = (
    f"https://gitlab.gnome.org/GNOME/vte/-/archive/{pkgver}/vte-{pkgver}.tar.gz"
)
sha256 = "2275d5958d89ca1a93488e066ee33987557db36f560a5dfd4101b1a2d4f150a4"
# assert in meson
options = ["!lto", "!cross"]

tool_flags = {
    "CFLAGS": ["-Wno-cast-function-type-strict"],
    "CXXFLAGS": ["-Wno-cast-function-type-strict"],
}


@subpackage("vte-gtk3")
def _gtk3(self):
    self.pkgdesc = "Gtk+3 terminal widget"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return [
        "usr/bin/vte-2.91",
        "usr/lib/libvte-2.91.so.*",
        "usr/lib/girepository-1.0/Vte-2.91.typelib",
    ]


@subpackage("vte-gtk4")
def _gtk4(self):
    self.pkgdesc = "Gtk4 terminal widget"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    return [
        "usr/bin/vte-2.91-gtk4",
        "usr/lib/libvte-2.91-gtk4.so.*",
        "usr/lib/girepository-1.0/Vte-3.91.typelib",
    ]


@subpackage("vte-gtk3-devel")
def _gtk3_devel(self):
    self.pkgdesc = "Gtk+3 terminal widget (development files)"
    return [
        "usr/include/vte-2.91/vte",
        "usr/lib/libvte-2.91.so",
        "usr/lib/pkgconfig/vte-2.91.pc",
        "usr/share/gir-1.0/Vte-2.91.gir",
        "usr/share/vala/vapi/vte-2.91.*",
    ]


@subpackage("vte-gtk4-devel")
def _devel(self):
    self.pkgdesc = "Gtk4 terminal widget (development files)"
    return [
        "usr/include/vte-2.91-gtk4/vte",
        "usr/lib/libvte-2.91-gtk4.so",
        "usr/lib/pkgconfig/vte-2.91-gtk4.pc",
        "usr/share/gir-1.0/Vte-3.91.gir",
        "usr/share/vala/vapi/vte-2.91-gtk4.*",
    ]
