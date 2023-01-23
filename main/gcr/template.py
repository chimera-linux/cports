pkgname = "gcr"
pkgver = "3.41.1"
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
    "gtk+3-devel", "libgcrypt-devel", "libsecret-devel", "p11-kit-devel",
    "libxslt-devel", "vala"
]
pkgdesc = "GNOME crypto package"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gcr"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "bb7128a3c2febbfee9c03b90d77d498d0ceb237b0789802d60185c71c4bea24f"
# getpass
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
# FIXME int (crashes gnome-keyring suite)
hardening = ["!int"]
# needs x11
options = ["!check"]

def post_install(self):
    self.install_file(
        self.files_path / "10-gcr-memlock.conf", "etc/security/limits.d"
    )

@subpackage("gcr-devel")
def _devel(self):
    return self.default_devel()

@subpackage("gcr-progs")
def _progs(self):
    return self.default_progs()
