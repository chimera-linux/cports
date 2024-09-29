pkgname = "gnome-control-center"
pkgver = "47.0.1"
pkgrel = 1
build_style = "meson"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "libxml2-progs",
    "meson",
    "pkgconf",
    "polkit",
    "python",
    "tecla",
]
makedepends = [
    "accountsservice-devel",
    "colord-devel",
    "colord-gtk-devel",
    "cups-devel",
    "gcr-devel",
    "glib-devel",
    "gnome-bluetooth-devel",
    "gnome-desktop-devel",
    "gnome-online-accounts-devel",
    "gnome-settings-daemon-devel",
    "gnutls-devel",
    "gsettings-desktop-schemas-devel",
    "gsound-devel",
    "gtk4-devel",
    "heimdal-devel",
    "ibus-devel",
    "libepoxy-devel",
    "libgtop-devel",
    "libgudev-devel",
    "libhandy-devel",
    "libnma-devel",
    "libpulse-devel",
    "libpwquality-devel",
    "libsecret-devel",
    "libsmbclient-devel",
    "libsoup-devel",
    "libwacom-devel",
    "libx11-devel",
    "libxi-devel",
    "libxml2-devel",
    "modemmanager-devel",
    "networkmanager-devel",
    "polkit-devel",
    "udisks-devel",
    "upower-devel",
]
depends = [
    "cups-pk-helper",
    "desktop-file-utils",
    "fprintd-meta",
    "gsettings-desktop-schemas",
    "power-profiles-daemon-meta",
    "sound-theme-freedesktop",
    "system-config-printer",
    "tecla",
    "udisks",
]
checkdepends = ["python-dbusmock", "xwayland-run", *depends]
pkgdesc = "GNOME control center"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-control-center"
source = f"$(GNOME_SITE)/gnome-control-center/{pkgver.split('.')[0]}/gnome-control-center-{pkgver}.tar.xz"
sha256 = "87eedf74337b3c61df19a0dc8c25b5c29629fb5f919bec34cbd0a4b1c7db3567"


@subpackage("gnome-control-center-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
