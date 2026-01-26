pkgname = "phosh-mobile-settings"
pkgver = "0.51.0"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["wlheadless-run", "--", "dbus-run-session"]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "cellbroadcastd-devel",
    "feedbackd-devel",
    "glib-devel",
    "gmobile-devel",
    "gnome-desktop-devel",
    "gsound-devel",
    "libadwaita-devel",
    "libportal-devel",
    "libpulse-devel",
    "libyaml-devel",
    "lm-sensors-devel",
    "phosh-devel",
    "wayland-protocols",
]
checkdepends = ["dbus", "xwayland-run"]
pkgdesc = "Phosh Mobile Settings"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/World/Phosh/phosh-mobile-settings"
source = f"https://sources.phosh.mobi/releases/phosh-mobile-settings/phosh-mobile-settings-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "9d6701cdeb40e8d4c2c0b64782be757c89bbd3411c1605d58d225a8c9132d9ee"
# known issue by upstream
options = ["!check"]
