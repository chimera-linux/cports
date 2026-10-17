pkgname = "mutt"
pkgver = "2.4.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-autocrypt",
    "--enable-compressed",
    "--enable-debug",
    "--enable-gpgme",
    "--enable-hcache",
    "--enable-imap",
    "--enable-pop",
    "--enable-sidebar",
    "--enable-smtp",
    "--with-sqlite3",
    "--with-lmdb",
]
hostmakedepends = [
    "autoconf",
    "automake",
]
makedepends = [
    "gpgme-devel",
    "lmdb-devel",
    "ncurses-devel",
    "perl",
    "sqlite-devel",
]
pkgdesc = "Mail reader"
license = "GPL-2.0-or-later"
url = "http://mutt.org"
source = f"http://ftp.mutt.org/pub/mutt/mutt-{pkgver}.tar.gz"
sha256 = "ce9154e3afede622d98b90a22c87d06f32051c930a9afb2b7ef41656c4dbc948"
# Doesn't have any meaningful tests
options = ["!check"]


def post_install(self):
    # These files aren't needed, since our immutable copy is in
    # /usr/share/mutt, so we don't need a pristine "backup" in /etc
    self.uninstall("etc/Muttrc.dist")
    self.uninstall("etc/mime.types.dist")
    # mutt will read files in /etc first, and if they don't exist, it'll try
    # /usr/share/mutt/ instead
    self.rename("etc/Muttrc", "usr/share/mutt/Muttrc", relative=False)
    self.rename("etc/mime.types", "usr/share/mutt/mime.types", relative=False)
