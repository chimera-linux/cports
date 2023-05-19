pkgname = "gnome-keyring"
pkgver = "42.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-pam-dir=/usr/lib/security", "--disable-schemas-compile"
]
make_cmd = "gmake"
make_check_args = ["-j1"]
make_check_wrapper = ["xvfb-run"]
hostmakedepends = [
    "gmake", "pkgconf", "docbook-xsl-nons", "glib-devel", "python",
    "libtasn1-progs", "xsltproc", "openssh", "automake", "libtool",
    "gettext-tiny-devel",
]
makedepends = [
    "gcr-devel", "glib-devel", "linux-pam-devel", "libgcrypt-devel"
]
checkdepends = ["xserver-xorg-xvfb", "dbus-x11"]
depends = ["dconf"]
pkgdesc = "GNOME password and secret manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-keyring"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c7f4d040cc76a6b7fe67e08ef9106911c3c80d40fc88cbfc8e2684a4c946e3e6"
