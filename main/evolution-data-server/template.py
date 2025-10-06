pkgname = "evolution-data-server"
pkgver = "3.58.0"
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
    "flex",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gperf",
    "ninja",
    "perl",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "gnome-online-accounts-devel",
    "heimdal-devel",
    "json-glib-devel",
    "libcanberra-devel",
    "libgweather-devel",
    "libical-devel",
    "libsecret-devel",
    "libsoup-devel",
    "nspr-devel",
    "nss-devel",
    "sqlite-devel",
    "vala-devel",
    "webkitgtk-devel",
    "webkitgtk4-devel",
]
checkdepends = ["dbus"]
pkgdesc = "Centralized access to appointments and contacts"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/evolution-data-server"
source = f"$(GNOME_SITE)/evolution-data-server/{pkgver[:-2]}/evolution-data-server-{pkgver}.tar.xz"
sha256 = "a2b5a0b8db11b728edc1d6f1c229dc2711962b7a87c0384221dac8d96000cef7"
options = ["!cross", "!lintpixmaps"]


def post_install(self):
    self.uninstall("usr/lib/systemd")


@subpackage("evolution-data-server-devel")
def _(self):
    return self.default_devel()
