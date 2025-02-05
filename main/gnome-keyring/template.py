pkgname = "gnome-keyring"
# pam_gnome_keyring may be moved to libsecret later?
# as of 46 it does not install it and distros don't use it
pkgver = "46.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-pam-dir=/usr/lib/security",
    "--disable-schemas-compile",
    # TODO replace with gcr + user service
    "--enable-ssh-agent",
]
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
    "libtasn1-progs",
    "libtool",
    "openssh",
    "pkgconf",
    "python",
    "libxslt-progs",
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
source = (
    f"$(GNOME_SITE)/gnome-keyring/{pkgver[:-2]}/gnome-keyring-{pkgver}.tar.xz"
)
sha256 = "bf26c966b8a8b7f3285ecc8bb3e467b9c20f9535b94dc451c9c559ddcff61925"
