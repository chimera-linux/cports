pkgname = "gnome-keyring"
pkgver = "40.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-pam-dir=/usr/lib/security", "--disable-schemas-compile"
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "docbook-xsl-nons", "glib-devel", "libtasn1-progs",
    "xsltproc", "openssh"
]
makedepends = [
    "gcr-devel", "libglib-devel", "linux-pam-devel", "libgcrypt-devel"
]
depends = ["dconf"]
pkgdesc = "GNOME password and secret manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-keyring"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a3d24db08ee2fdf240fbbf0971a98c8ee295aa0e1a774537f4ea938038a3b931"
# FIXME: xvfb-run
options = ["!check"]
