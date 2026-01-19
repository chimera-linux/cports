pkgname = "vte"
pkgver = "0.82.0"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-D_systemd=false",
    "-Dgir=true",
    "-Dvapi=true",
    "-Dgtk4=true",
]
hostmakedepends = [
    "bash",
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "gperf",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "fribidi-devel",
    "glib-devel",
    "gnutls-devel",
    "gtk+3-devel",
    "gtk4-devel",
    "icu-devel",
    "linux-headers",
    "lz4-devel",
    "pango-devel",
    "pcre2-devel",
    "vala-devel",
    "zlib-ng-compat-devel",
]
renames = ["vte-common"]
pkgdesc = "Gtk terminal widget"
subdesc = "common files"
license = "LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Terminal/VTE"
source = f"$(GNOME_SITE)/vte/{pkgver[: pkgver.rfind('.')]}/vte-{pkgver}.tar.xz"
sha256 = "b0718db3254730701b43bf5e113cbf8cdb2c14715d32ee1e8a707dc6eb70535f"
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
        "usr/lib/libvte-2.91.so.*",
        "usr/lib/girepository-1.0/Vte-2.91.typelib",
    ]


@subpackage("vte-gtk4")
def _(self):
    self.subdesc = "Gtk4"
    self.depends = [self.parent]
    return [
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


@subpackage("vte-demos")
def _(self):
    self.subdesc = "example applications"
    self.depends = [self.parent]
    return [
        "usr/bin/vte-2.91",
        "usr/bin/vte-2.91-gtk4",
        "usr/share/applications/org.gnome.Vte.App.Gtk3.desktop",
        "usr/share/xdg-terminals/org.gnome.Vte.App.Gtk3.desktop",
        "usr/share/applications/org.gnome.Vte.App.Gtk4.desktop",
        "usr/share/xdg-terminals/org.gnome.Vte.App.Gtk4.desktop",
    ]
