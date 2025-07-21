pkgname = "gnome-keyring"
# pam_gnome_keyring may be moved to libsecret later?
# as of 48 it does not install it and distros don't use it
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    # TODO replace with gcr + user service
    "-Dssh-agent=true",
    "-Dsystemd=disabled",
]
make_check_wrapper = [
    "wlheadless-run",
    "--",
    "dbus-run-session",
    "--",
]
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext-devel",
    "glib-devel",
    "libtasn1-progs",
    "libxslt-progs",
    "meson",
    "openssh",
    "pkgconf",
    "python",
]
makedepends = [
    "gcr3-devel",
    "glib-devel",
    "libcap-ng-devel",
    "libgcrypt-devel",
    "linux-pam-devel",
]
checkdepends = ["dbus", "xwayland-run"]
depends = ["dconf"]
pkgdesc = "GNOME password and secret manager"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-keyring"
source = (
    f"$(GNOME_SITE)/gnome-keyring/{pkgver[:-2]}/gnome-keyring-{pkgver}.tar.xz"
)
sha256 = "f20518c920e9ea3f9c9b8b44be8c50d8d7feecd0dd5624960f77bd2ca4fbeb9d"
# check may be disabled
options = []

if self.profile().wordsize == 32:
    # 32-bit targets fail 2 tests: https://gitlab.gnome.org/GNOME/gnome-keyring/-/issues/124
    options += ["!check"]
