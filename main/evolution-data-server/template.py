pkgname = "evolution-data-server"
pkgver = "3.44.4"
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
sha256 = "c0c6658838d58ba46042a4b9e50a3bb1129691e4cdb84b5eba0bf330b2ccb2eb"
# internally passes some stuff that only goes to linker
tool_flags = {"CFLAGS": ["-Wno-unused-command-line-argument"]}
# fail test-book-client-custom-summary
options = ["!cross", "!check"]

def post_install(self):
    self.rm(self.destdir / "usr/lib/systemd", recursive = True)

@subpackage("evolution-data-server-devel")
def _devel(self):
    return self.default_devel()
