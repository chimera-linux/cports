pkgname = "evolution-data-server"
pkgver = "3.42.3"
pkgrel = 0
build_style = "cmake"
# TODO: libgdata
configure_args = [
    "-DENABLE_GOOGLE=OFF", "-DWITH_LIBDB=OFF",
    "-DSYSCONF_INSTALL_DIR=/etc", "-DENABLE_INTROSPECTION=ON",
    "-DENABLE_VALA_BINDINGS=ON",
]
hostmakedepends = [
    "cmake", "ninja", "pkgconf", "flex", "glib-devel", "gperf",
    "gobject-introspection", "gettext-tiny", "vala", "perl",
]
makedepends = [
    "libglib-devel", "libcanberra-devel", "libical-devel", "heimdal-devel",
    "webkitgtk-devel", "libsecret-devel", "gnome-online-accounts-devel",
    "gcr-devel", "sqlite-devel", "libgweather-devel", "libsoup-devel",
    "json-glib-devel", "nss-devel", "nspr-devel", "vala-devel",
    "openldap-devel",
]
checkdepends = ["dbus"]
pkgdesc = "Centralized access to appointments and contacts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/evolution-data-server"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "6f5847a1234799073e9585db861c21381a09ed550dc0a2125f00ba5f90bd361d"
options = ["!cross"]

def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive = True)

@subpackage("evolution-data-server-devel")
def _devel(self):
    return self.default_devel()
