pkgname = "gcr4"
pkgver = "3.92.0"
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
sha256 = "896abf8e1db0f40eb28073f364f36a72385ac8abf8cd1362b1016e97721ff518"
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
