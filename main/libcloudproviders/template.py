pkgname = "libcloudproviders"
pkgver = "0.3.6"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true", "-Dvapigen=true"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "glib-devel",
    "vala-devel",
]
makedepends = ["glib-devel"]
pkgdesc = "DBus API for cloud storage sync clients to expose their services"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/libcloudproviders"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "fa25bdc2e415a717999f3d0bac8756dc0dcfe40e3ada864fadc26df0746a7116"


@subpackage("libcloudproviders-devel")
def _devel(self):
    return self.default_devel()
