pkgname = "gcr"
pkgver = "4.4.0.1"
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
source = f"$(GNOME_SITE)/gcr/{pkgver[:-4]}/gcr-{pkgver}.tar.xz"
sha256 = "0c3c341e49f9f4f2532a4884509804190a0c2663e6120360bb298c5d174a8098"
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
