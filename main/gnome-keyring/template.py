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
make_check_wrapper = ["weston-headless-run", "dbus-run-session"]
hostmakedepends = [
    "gmake",
    "pkgconf",
    "docbook-xsl-nons",
    "glib-devel",
    "python",
    "libtasn1-progs",
    "xsltproc",
    "openssh",
    "automake",
    "libtool",
    "gettext-devel",
]
makedepends = ["gcr3-devel", "glib-devel", "linux-pam-devel", "libgcrypt-devel"]
checkdepends = ["weston", "dbus"]
depends = ["dconf"]
pkgdesc = "GNOME password and secret manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-keyring"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b1d3ae9132ff2f8b3f25a190790892968e3d0acf952a487e40f644a8550ce3f6"
