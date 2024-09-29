pkgname = "vte-common"
pkgver = "0.78.0"
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
    "zlib-ng-compat-devel",
    "linux-headers",
]
pkgdesc = "Gtk terminal widget"
subdesc = "common files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Terminal/VTE"
source = (
    f"https://gitlab.gnome.org/GNOME/vte/-/archive/{pkgver}/vte-{pkgver}.tar.gz"
)
sha256 = "82e19d11780fed4b66400f000829ce5ca113efbbfb7975815f26ed93e4c05f2d"
# assert in meson
options = ["!lto", "!cross"]

tool_flags = {
    "CFLAGS": ["-Wno-cast-function-type-strict"],
    "CXXFLAGS": [
        "-Wno-cast-function-type-strict",
        # these are bad but also very noisy...
        "-Wno-cast-align",
        "-Wno-float-equal",
    ],
}


@subpackage("vte-gtk3")
def _(self):
    self.subdesc = "Gtk+3"
    self.depends = [self.parent]
    return [
        "usr/bin/vte-2.91",
        "usr/lib/libvte-2.91.so.*",
        "usr/lib/girepository-1.0/Vte-2.91.typelib",
    ]


@subpackage("vte-gtk4")
def _(self):
    self.subdesc = "Gtk4"
    self.depends = [self.parent]
    return [
        "usr/bin/vte-2.91-gtk4",
        "usr/lib/libvte-2.91-gtk4.so.*",
        "usr/lib/girepository-1.0/Vte-3.91.typelib",
    ]


@subpackage("vte-gtk3-devel")
def _(self):
    self.subdesc = "Gtk+3 development files"
    return [
        "usr/include/vte-2.91/vte",
        "usr/lib/libvte-2.91.so",
        "usr/lib/pkgconfig/vte-2.91.pc",
        "usr/share/gir-1.0/Vte-2.91.gir",
        "usr/share/vala/vapi/vte-2.91.*",
    ]


@subpackage("vte-gtk4-devel")
def _(self):
    self.subdesc = "Gtk4 development files"
    return [
        "usr/include/vte-2.91-gtk4/vte",
        "usr/lib/libvte-2.91-gtk4.so",
        "usr/lib/pkgconfig/vte-2.91-gtk4.pc",
        "usr/share/gir-1.0/Vte-3.91.gir",
        "usr/share/vala/vapi/vte-2.91-gtk4.*",
    ]
