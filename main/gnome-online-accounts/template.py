pkgname = "gnome-online-accounts"
pkgver = "3.40.1"
pkgrel = 0
build_style = "gnu_configure"
# TODO: figure out if we can make it work with heimdal
configure_args = [
    "--enable-documentation", "--enable-backend", "--enable-google",
    "--enable-flickr", "--enable-facebook", "--enable-exchange",
    "--enable-imap-smtp", "--enable-owncloud", "--enable-windows-live",
    "--enable-pocket", "--enable-lastfm", "--enable-media-server",
    "--enable-introspection",
    "--disable-fedora", "--disable-kerberos", "--disable-static",
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "gettext-tiny-devel", "docbook-xsl-nons", "glib-devel",
    "xsltproc", "gobject-introspection", "vala", "automake", "libtool",
    "gtk-doc-tools",
]
makedepends = [
    "libglib-devel", "dbus-devel", "gtk+3-devel", "webkitgtk-devel",
    "json-glib-devel", "libsecret-devel", "libsoup-devel", "libxml2-devel",
    "gcr-devel", "rest-devel",
]
pkgdesc = "GNOME service to access online accounts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-online-accounts"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "955a03128d0e87855d34d7c534e088f6286ed7ac01baa4ef824ef42a2cb39aad"

def pre_configure(self):
    self.do("autoreconf", "-if")

@subpackage("gnome-online-accounts-devel")
def _devel(self):
    return self.default_devel()
