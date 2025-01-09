pkgname = "vala"
pkgver = "0.56.16"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "bison",
    "docbook-xml",
    "flex",
    "pkgconf",
    "slibtool",
    "xsltproc",
]
makedepends = ["libfl-devel-static", "glib-devel", "graphviz-devel"]
checkdepends = ["dbus", "libgirepository-devel", "bash"]
provides = ["so:libvalaccodegen.so=0"]
pkgdesc = "Programming language based on the GObject type system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/Vala"
source = (
    f"$(GNOME_SITE)/vala/{pkgver[0 : pkgver.rfind('.')]}/vala-{pkgver}.tar.xz"
)
sha256 = "05487b5600f5d2f09e66a753cccd8f39c1bff9f148aea1b7774d505b9c8bca9b"


@subpackage("libvala")
def _(self):
    self.subdesc = "runtime library"

    return ["usr/lib/libvala-*.so.*"]


@subpackage("valadoc")
def _(self):
    self.pkgdesc = "Vala documentation tool"

    return [
        "usr/bin/valadoc*",
        "usr/share/man/man1/valadoc.1",
    ]


@subpackage("libvaladoc")
def _(self):
    self.pkgdesc = "Vala documentation tool"
    self.subdesc = "runtime library"

    return [
        "usr/lib/libvaladoc-*.so.*",
        "usr/lib/valadoc-*",
        "usr/share/valadoc-*",
    ]


@subpackage("valadoc-devel")
def _(self):
    self.pkgdesc = "Vala documentation tool"

    return [
        "usr/include/valadoc-*",
        "usr/lib/libvaladoc-*.so",
        "usr/lib/pkgconfig/valadoc-*.pc",
        "usr/share/vala/vapi/valadoc*",
    ]


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
