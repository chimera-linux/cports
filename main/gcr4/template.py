pkgname = "gcr4"
pkgver = "4.0.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgpg_path=/usr/bin/gpg", "-Dsystemd=disabled", "-Dssh_agent=false",
    "-Dgtk_doc=false",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gtk-doc-tools", "gettext-tiny-devel",
    "gobject-introspection", "vala", "openssh",
]
makedepends = [
    "gtk4-devel", "libgcrypt-devel", "libsecret-devel", "p11-kit-devel",
    "libxslt-devel", "vala"
]
pkgdesc = "GNOME crypto package"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gcr"
source = f"$(GNOME_SITE)/gcr/{pkgver[:-2]}/gcr-{pkgver}.tar.xz"
sha256 = "c45855924f0ee7bab43e2dd38bfafd2ac815c6e9864341c0161e171173dcec7c"
# getpass
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
# needs x11
options = ["!check"]

@subpackage("gcr4-devel")
def _devel(self):
    return self.default_devel()

@subpackage("gcr4-progs")
def _progs(self):
    return self.default_progs()

# FIXME visibility
hardening = ["!vis"]
