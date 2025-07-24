pkgname = "vala"
pkgver = "0.56.16"
pkgrel = 4
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "bison",
    "docbook-xml",
    "flex",
    "libxslt-progs",
    "pkgconf",
    "slibtool",
]
makedepends = ["flex-devel-static", "glib-devel", "graphviz-devel"]
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
    # transitional
    self.provides = [self.with_pkgver("libvala")]

    return ["usr/lib/libvala-*.so.*"]


@subpackage("vala-valadoc")
def _(self):
    self.pkgdesc = "Vala documentation tool"
    # transitional
    self.provides = [self.with_pkgver("valadoc")]

    return [
        "usr/bin/valadoc*",
        "usr/share/man/man1/valadoc.1",
    ]


@subpackage("vala-valadoc-libs")
def _(self):
    self.pkgdesc = "Vala documentation tool"
    # transitional
    self.provides = [self.with_pkgver("libvaladoc")]

    return [
        "usr/lib/libvaladoc-*.so.*",
        "usr/lib/valadoc-*",
        "usr/share/valadoc-*",
    ]


@subpackage("vala-valadoc-devel")
def _(self):
    self.pkgdesc = "Vala documentation tool"
    # transitional
    self.provides = [self.with_pkgver("valadoc-devel")]

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
