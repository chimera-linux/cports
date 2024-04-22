pkgname = "gcr"
pkgver = "4.3.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgpg_path=/usr/bin/gpg",
    "-Dsystemd=disabled",
    "-Dssh_agent=false",
    "-Dgtk_doc=false",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gtk-doc-tools",
    "gettext-devel",
    "gobject-introspection",
    "vala",
    "openssh",
]
makedepends = [
    "gtk4-devel",
    "libgcrypt-devel",
    "libsecret-devel",
    "p11-kit-devel",
    "libxslt-devel",
    "vala",
]
pkgdesc = "GNOME crypto package"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gcr"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c3ee8728e4364b0397f435fa20f92f901ab139d2b264f4e059d67b3c0f43cd36"
# getpass
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
# FIXME int (crashes gnome-keyring suite)
hardening = ["!int"]
# needs x11
options = ["!check"]


@subpackage("gcr-devel")
def _devel(self):
    return self.default_devel()


@subpackage("gcr-progs")
def _progs(self):
    return self.default_progs()
