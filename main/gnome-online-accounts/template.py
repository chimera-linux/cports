pkgname = "gnome-online-accounts"
pkgver = "3.44.0"
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
sha256 = "381d5d4106f435b6f87786aa049be784774e15996adcc02789807afc87ea7342"
options = ["!cross"]

def pre_configure(self):
    self.do("autoreconf", "-if")

@subpackage("gnome-online-accounts-devel")
def _devel(self):
    return self.default_devel()
