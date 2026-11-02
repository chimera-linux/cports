pkgname = "gnome-settings-daemon"
pkgver = "51.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Delogind=true",
    "-Dsystemd=false",
    "-Dsystemd-units=false",
    # Unpackaged
    "-Dusb-protection=false",
]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "perl",
    "pkgconf",
]
makedepends = [
    # actually pulseaudio is used, alsa is only used to query hw info
    "alsa-lib-devel",
    "colord-devel",
    "cups-devel",
    "elogind-devel",
    "gcr-devel",
    "geoclue-devel",
    "geocode-glib-devel",
    "gnome-desktop-devel",
    "gsettings-desktop-schemas-devel",
    "libcanberra-devel",
    "libgudev-devel",
    "libgweather-devel",
    "libnotify-devel",
    "libpulse-devel",
    "modemmanager-devel",
    "networkmanager-devel",
    "pango-devel",
    "polkit-devel",
    "udev-devel",
    "upower-devel",
]
checkdepends = [
    "elogind",
    "gnome-session",
    "gnome-shell",
    "hwdata",
    "libnotify",
    "python-dbusmock",
    "python-gobject",
    "python-pycodestyle",
    "udev",
    "umockdev",
]
depends = ["iio-sensor-proxy-meta"]
pkgdesc = "GNOME settings daemon"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-settings-daemon"
source = f"$(GNOME_SITE)/gnome-settings-daemon/{pkgver[:-2]}/gnome-settings-daemon-{pkgver}.tar.xz"
sha256 = "e7de8d30ae2d63c7a9a21f8f0247219275cbc1d7f5ed09205e4a47642666f6ae"
tool_flags = {"CFLAGS": ["-UG_DISABLE_ASSERT"]}
# wants xvfb
options = ["etcfiles", "!check"]


@subpackage("gnome-settings-daemon-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
