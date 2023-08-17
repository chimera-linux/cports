pkgname = "libcloudproviders"
pkgver = "0.3.2"
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
makedepends = [
    "glib-devel",
]
pkgdesc = "DBus API for cloud storage sync clients to expose their services"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/libcloudproviders"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "378bbb383ba5005799e1df8542d59a4330f741f898a23a3d1f9cb82f08ede66d"


@subpackage("libcloudproviders-devel")
def _devel(self):
    return self.default_devel()
