pkgname = "gcr3"
pkgver = "3.41.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgpg_path=/usr/bin/gpg",
    "-Dsystemd=disabled",
    "-Dssh_agent=false",
    "-Dgtk_doc=false",
]
hostmakedepends = [
    "gettext-devel",
    "glib-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "meson",
    "openssh",
    "pkgconf",
    "vala",
]
makedepends = [
    "gtk+3-devel",
    "libgcrypt-devel",
    "libsecret-devel",
    "libxslt-devel",
    "p11-kit-devel",
    "vala",
]
pkgdesc = "GNOME crypto package 3.x"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gcr"
source = f"$(GNOME_SITE)/gcr/{pkgver[:-2]}/gcr-{pkgver}.tar.xz"
sha256 = "bad10f3c553a0e1854649ab59c5b2434da22ca1a54ae6138f1f53961567e1ab7"
# getpass
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
# FIXME int (crashes gnome-keyring suite)
hardening = ["!int"]
# needs x11
options = ["!check"]


@subpackage("gcr3-devel")
def _(self):
    return self.default_devel()


@subpackage("gcr3-progs")
def _(self):
    return self.default_progs()
