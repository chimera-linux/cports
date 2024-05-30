pkgname = "gnome-control-center"
pkgver = "46.2"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
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
checkdepends = ["python-dbusmock", "xwayland-run"] + depends
pkgdesc = "GNOME control center"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-control-center"
source = (
    f"$(GNOME_SITE)/{pkgname}/{pkgver.split('.')[0]}/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "6335c6cb8164e574db521fff61cfa3dfaa55f1db66ae3bca02750a193e1c4f3d"


@subpackage("gnome-control-center-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()
