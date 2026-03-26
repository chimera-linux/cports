pkgname = "feedbackd"
pkgver = "0.8.7"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "gmobile-devel",
    "gobject-introspection-devel",
    "gsound-devel",
    "json-glib-devel",
    "libgudev-devel",
    "umockdev-devel",
]
depends = ["dbus", "feedbackd-device-themes"]
checkdepends = ["dbus"]
pkgdesc = "Daemon to provide haptic, LED, and audio feedback"
license = "GPL-3.0-or-later"
url = "https://gitlab.freedesktop.org/agx/feedbackd"
source = (
    f"https://sources.phosh.mobi/releases/feedbackd/feedbackd-{pkgver}.tar.xz"
)
sha256 = "bd3a76c0dade8cb032fca7a739fd4b4e8d27eca5a806fd33859ecf48a349a5d0"
# cannot register existing type 'LfbGdbusFeedback'
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("feedbackd-devel")
def _(self):
    return self.default_devel()
