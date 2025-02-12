pkgname = "gcr"
pkgver = "4.3.1"
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
source = f"$(GNOME_SITE)/gcr/{pkgver[:-2]}/gcr-{pkgver}.tar.xz"
sha256 = "b2f070fff1840eef70546a28be80235427c116aadc593b5b68ccc869be3aa09d"
# getpass
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
# FIXME int (crashes gnome-keyring suite)
hardening = ["!int"]
# needs x11
options = ["!check"]


@subpackage("gcr-devel")
def _(self):
    return self.default_devel()


@subpackage("gcr-progs")
def _(self):
    return self.default_progs()
