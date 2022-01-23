pkgname = "gnome-settings-daemon"
pkgver = "41.0"
pkgrel = 0
build_style = "meson"
# TODO: modemmanager, libwacom, nss
configure_args = [
    "-Dsystemd=false", "-Dsmartcard=false", "-Dwwan=false", "-Dwacom=false",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "xsltproc", "docbook-xsl-nons", "perl",
]
makedepends = [
    "libglib-devel", "geocode-glib-devel", "gnome-desktop-devel",
    "gtk+3-devel", "gsettings-desktop-schemas-devel", "libgweather-devel",
    "lcms2-devel", "libcanberra-devel", "geoclue-devel", "libnotify-devel",
    "libpulse-devel", "pango-devel", "upower-devel", "libx11-devel",
    "libxfixes-devel", "libgudev-devel", "wayland-devel", "cups-devel",
    "eudev-devel", "networkmanager-devel", "colord-devel", "polkit-devel",
    # actually pulseaudio is used, alsa is only used to query hw info
    "alsa-lib-devel",
]
depends = ["hicolor-icon-theme"]
checkdepends = [
    "elogind", "eudev", "libnotify", "python-dbusmock", "python-gobject",
    "python-pycodestyle", "hwids"
]
pkgdesc = "GNOME settings daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-settings-daemon"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "e6ca6361fbd1deab2de1a1e390d4f14167cf47b1c547dbb8b65a5d89e9663884"
tool_flags = {"CFLAGS": ["-UG_DISABLE_ASSERT"]}
# unpackaged checkdepends
options = ["!check"]

@subpackage("gnome-settings-daemon-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()
