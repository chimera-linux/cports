pkgname = "evolution-data-server"
pkgver = "3.52.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_LIBDB=OFF",
    "-DSYSCONF_INSTALL_DIR=/etc",
    "-DENABLE_INTROSPECTION=ON",
    "-DENABLE_VALA_BINDINGS=ON",
    "-DWITH_OPENLDAP=OFF",  # don't depend on shit software
]
make_check_args = ["-j1"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "flex",
    "glib-devel",
    "gperf",
    "gobject-introspection",
    "gettext",
    "vala",
    "perl",
]
makedepends = [
    "glib-devel",
    "libcanberra-devel",
    "libical-devel",
    "heimdal-devel",
    "webkitgtk-devel",
    "webkitgtk4-devel",
    "libsecret-devel",
    "nss-devel",
    "nspr-devel",
    "gnome-online-accounts-devel",
    "sqlite-devel",
    "libgweather-devel",
    "libsoup-devel",
    "json-glib-devel",
    "vala-devel",
]
checkdepends = ["dbus"]
pkgdesc = "Centralized access to appointments and contacts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/evolution-data-server"
source = f"$(GNOME_SITE)/evolution-data-server/{pkgver[:-2]}/evolution-data-server-{pkgver}.tar.xz"
sha256 = "e9f6c80c142033b1801bccaa6221c453de34ead4ea089b2086b19086f9a9c2e4"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/systemd")


@subpackage("evolution-data-server-devel")
def _devel(self):
    return self.default_devel()
