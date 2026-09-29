pkgname = "libsecret"
pkgver = "0.21.8.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    # complains about duplicate target names otherwise
    "-Ddefault_library=shared",
    "-Dgtk_doc=false",
]
hostmakedepends = [
    "bash-completion",
    "docbook-xsl-nons",
    "glib-devel",
    "gobject-introspection",
    "libxslt-progs",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = ["glib-devel", "libgcrypt-devel", "vala"]
pkgdesc = "GObject-based library for accessing the Secret Service API"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libsecret"
source = f"$(GNOME_SITE)/libsecret/{pkgver[:-4]}/libsecret-{pkgver}.tar.xz"
sha256 = "142948339c5b971d8f6a8c7099521f6fd319b6fe73d2694b4e6d3310ed28b6e6"
# does not work in container
options = ["!check", "!cross"]


@subpackage("libsecret-devel")
def _(self):
    return self.default_devel()


@subpackage("libsecret-progs")
def _(self):
    return self.default_progs()
