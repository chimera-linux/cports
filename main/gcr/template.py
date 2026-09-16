pkgname = "gcr"
pkgver = "4.4.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgpg_path=/usr/bin/gpg",
    "-Dsystemd=disabled",
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
    "gtk4-devel",
    "libgcrypt-devel",
    "libsecret-devel",
    "libxslt-devel",
    "p11-kit-devel",
    "vala",
]
pkgdesc = "GNOME crypto package"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gcr"
source = f"$(GNOME_SITE)/gcr/{pkgver[:-2]}/gcr-{pkgver}.tar.xz"
sha256 = "c4442c15d4330f17a1f5194df08c576877af68412ab2521446a93bd5e24c931b"
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
