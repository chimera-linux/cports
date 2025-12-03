pkgname = "profanity"
pkgver = "0.15.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-c-plugins",
    "--enable-notifications",
    "--enable-omemo",
    "--enable-pgp",
    # "--enable-python-plugins",
    "--enable-year2038",
]
hostmakedepends = [
    "autoconf",
    "autoconf-archive",
    "automake",
    "libtool-devel",
    "pkgconf",
]
makedepends = [
    "curl-devel",
    "glib-devel",
    "gpgme",
    "libgcrypt-devel",
    "libnotify-devel",
    "readline-devel",
    "shared-mime-info",
    "sqlite-devel",
]
pkgdesc = "Ncurses based XMPP client"
license = "GPL-3.0-or-later"
url = "https://github.com/profanity-im/profanity"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a18aed3ce35e2581e120551991be11b853c42b0f748b9bff7f8e0304abb0fdcc"
