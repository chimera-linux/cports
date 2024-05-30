pkgname = "gnome-keyring"
# pam_gnome_keyring may be moved to libsecret later?
# as of 46 it does not install it and distros don't use it
pkgver = "46.1"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-pam-dir=/usr/lib/security",
    "--disable-schemas-compile",
    # TODO replace with gcr + user service
    "--enable-ssh-agent",
]
make_cmd = "gmake"
make_check_args = ["-j1"]
make_check_wrapper = [
    "wlheadless-run",
    "--",
    "dbus-run-session",
    "--",
]
hostmakedepends = [
    "automake",
    "docbook-xsl-nons",
    "gettext-devel",
    "glib-devel",
    "gmake",
    "libtasn1-progs",
    "libtool",
    "openssh",
    "pkgconf",
    "python",
    "xsltproc",
]
makedepends = [
    "gcr3-devel",
    "glib-devel",
    "libgcrypt-devel",
    "linux-pam-devel",
]
checkdepends = ["dbus", "xwayland-run"]
depends = ["dconf"]
pkgdesc = "GNOME password and secret manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-keyring"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b1d3ae9132ff2f8b3f25a190790892968e3d0acf952a487e40f644a8550ce3f6"
