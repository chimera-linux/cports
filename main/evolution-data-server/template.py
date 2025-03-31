pkgname = "evolution-data-server"
pkgver = "3.56.0"
pkgrel = 2
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
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/evolution-data-server"
source = f"$(GNOME_SITE)/evolution-data-server/{pkgver[:-2]}/evolution-data-server-{pkgver}.tar.xz"
sha256 = "7ae5482aa4ee2894467716c5be982500e1d511dddf4ab29b68fdb107d7f8a8ff"
options = ["!cross"]


def post_install(self):
    self.uninstall("usr/lib/systemd")


@subpackage("evolution-data-server-devel")
def _(self):
    return self.default_devel()
