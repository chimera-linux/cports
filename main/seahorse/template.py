pkgname = "seahorse"
pkgver = "43.0"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dmanpage=true"]
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
    "xsltproc",
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
sha256 = "0a2512e9e8fd3e271177df7f1e01f8c6e7bce8867b4d258148360105721af108"
