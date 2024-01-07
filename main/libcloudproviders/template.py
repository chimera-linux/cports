pkgname = "libcloudproviders"
pkgver = "0.3.5"
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
sha256 = "5642fe3d89322e79bff919e828dd3ad4e109ccfaadfc2f9a87fa40694ed08bee"


@subpackage("libcloudproviders-devel")
def _devel(self):
    return self.default_devel()
