pkgname = "libcloudproviders"
pkgver = "0.3.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true", "-Dvapigen=true"]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel",
    "vala-devel",
]
makedepends = ["glib-devel",]
pkgdesc = "DBus API for cloud storage sync clients to expose their services"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/libcloudproviders"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "bd00e7b85d84d201bd36f6e460555d8ba41246d63d5f3607ff7542a257f27236"

@subpackage("libcloudproviders-devel")
def _devel(self):
    return self.default_devel()
