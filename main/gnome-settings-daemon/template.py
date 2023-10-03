pkgname = "gnome-settings-daemon"
pkgver = "45.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemd=false"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "xsltproc",
    "docbook-xsl-nons",
    "perl",
    "gettext",
]
makedepends = [
    "glib-devel",
    "geocode-glib-devel",
    "gnome-desktop-devel",
    "gtk+3-devel",
    "gsettings-desktop-schemas-devel",
    "libgweather-devel",
    "lcms2-devel",
    "libcanberra-devel",
    "geoclue-devel",
    "libnotify-devel",
    "libpulse-devel",
    "pango-devel",
    "upower-devel",
    "libx11-devel",
    "libxfixes-devel",
    "libgudev-devel",
    "wayland-devel",
    "cups-devel",
    "udev-devel",
    "networkmanager-devel",
    "colord-devel",
    "polkit-devel",
    # actually pulseaudio is used, alsa is only used to query hw info
    "modemmanager-devel",
    "gcr-devel",
    "alsa-lib-devel",
    "libwacom-devel",
    "nss-devel",
]
checkdepends = [
    "elogind",
    "udev",
    "libnotify",
    "python-dbusmock",
    "python-gobject",
    "python-pycodestyle",
    "hwdata",
]
pkgdesc = "GNOME settings daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-settings-daemon"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "bb4dc46950e2a90f38f23225848856d2a7b1b718c89d0285ce197b7016bb1dc8"
tool_flags = {"CFLAGS": ["-UG_DISABLE_ASSERT"]}
# unpackaged checkdepends
options = ["!check"]


@subpackage("gnome-settings-daemon-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()
