pkgname = "seahorse"
pkgver = "47.0.1"
pkgrel = 1
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "-Dmanpage=true",
]
hostmakedepends = [
    "desktop-file-utils",
    "docbook-xsl-nons",
    "gcr3-devel",
    "gettext",
    "gnupg",
    "itstool",
    "libhandy-devel",
    "libsecret-devel",
    "meson",
    "openssh",
    "pkgconf",
    "vala",
    "libxslt-progs",
]
makedepends = [
    "avahi-devel",
    "avahi-glib-devel",
    "gcr3-devel",
    "glib-devel",
    "gpgme-devel",
    "gtk+3-devel",
    "libhandy-devel",
    "libpwquality-devel",
    "libsecret-devel",
    "libsoup-devel",
    "openldap-devel",
]
pkgdesc = "Password and encryption key manager for GNOME"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/seahorse"
source = f"{url}/-/archive/{pkgver}/seahorse-{pkgver}.tar.gz"
sha256 = "46f57d8fbf8da147d9842f6efc6a6666ee76853b10d97622a636f73a44869e5e"
