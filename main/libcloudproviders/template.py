pkgname = "libcloudproviders"
pkgver = "0.3.4"
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
sha256 = "e98897c747cb07b5ef49c9be6b7da1d47c69cc8020d08d16e5e8165eb606496a"


@subpackage("libcloudproviders-devel")
def _devel(self):
    return self.default_devel()
