# keep in sync with vala-valadoc
pkgname = "vala"
pkgver = "0.56.16"
pkgrel = 5
build_style = "gnu_configure"
configure_args = ["--disable-valadoc"]
hostmakedepends = [
    "automake",
    "bison",
    "docbook-xml",
    "flex",
    "libtool",
    "libxslt-progs",
    "pkgconf",
]
makedepends = ["flex-devel-static", "glib-devel", "gobject-introspection-devel"]
checkdepends = ["dbus", "gobject-introspection-devel", "bash"]
provides = ["so:libvalaccodegen.so=0"]
pkgdesc = "Programming language based on the GObject type system"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Vala"
source = (
    f"$(GNOME_SITE)/vala/{pkgver[0 : pkgver.rfind('.')]}/vala-{pkgver}.tar.xz"
)
sha256 = "05487b5600f5d2f09e66a753cccd8f39c1bff9f148aea1b7774d505b9c8bca9b"


@subpackage("vala-libs")
def _(self):
    self.renames = ["libvala"]

    return ["usr/lib/libvala-*.so.*"]


@subpackage("vala-devel")
def _(self):
    self.depends += [self.parent]

    # do not pick up vapigen.pc etc
    return [
        "usr/lib/libvala-*.so",
        "usr/lib/pkgconfig/libvala*.pc",
        "usr/include/vala-*",
        "usr/share/vala/vapi/libvala-*.*",
        "usr/share/aclocal",
    ]
