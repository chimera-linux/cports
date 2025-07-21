pkgname = "libcloudproviders"
pkgver = "0.3.6"
pkgrel = 1
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
sha256 = "fa25bdc2e415a717999f3d0bac8756dc0dcfe40e3ada864fadc26df0746a7116"


@subpackage("libcloudproviders-devel")
def _(self):
    return self.default_devel()
