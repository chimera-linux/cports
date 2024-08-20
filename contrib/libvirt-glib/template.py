pkgname = "libvirt-glib"
pkgver = "5.0.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "gtk-doc-tools",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "gobject-introspection",
    "libvirt-devel",
    "libxml2-devel",
]
pkgdesc = "Glib integration with libvirt"
maintainer = "cesorious <cesorious@gmail.com>"
license = "LGPL-2.1-only"
url = "https://libvirt.org"
source = f"http://libvirt.org/sources/glib/libvirt-glib-{pkgver}.tar.xz"
sha256 = "9bfec346382416a3575d87299bc641b2a464aa519fd9b1287e318aa43a2f3b8b"


@subpackage("libvirt-glib-devel")
def _(self):
    return self.default_devel()
