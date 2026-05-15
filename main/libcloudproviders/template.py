pkgname = "libcloudproviders"
pkgver = "0.4.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true", "-Dvapigen=true"]
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala-devel",
]
makedepends = ["glib-devel"]
pkgdesc = "DBus API for cloud storage sync clients to expose their services"
license = "LGPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/libcloudproviders"
source = f"{url}/-/archive/{pkgver}/libcloudproviders-{pkgver}.tar.gz"
sha256 = "ff65b1d4ed685f5f1659370e7dc503e891fdc0c9174661b1447e04798b98ed83"


@subpackage("libcloudproviders-devel")
def _(self):
    return self.default_devel()
