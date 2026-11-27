pkgname = "openbox"
pkgver = "3.6.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "slibtool", "pkgconf"]
makedepends = [
    "glib-devel",
    "imlib2-devel",
    "libice-devel",
    "librsvg-devel",
    "libsm-devel",
    "libxcursor-devel",
    "libxml2-devel",
    "pango-devel",
    "startup-notification-devel",
]
pkgdesc = "Highly configurable and lightweight X11 window manager"
license = "GPL-2.0-or-later"
url = "https://openbox.org"
source = f"{url}/dist/openbox/openbox-{pkgver}.tar.gz"
sha256 = "8b4ac0760018c77c0044fab06a4f0c510ba87eae934d9983b10878483bde7ef7"
options = ["etcfiles"]


def post_install(self):
    # ancient and dead
    self.uninstall("cmd:gdm-control")
    self.uninstall("cmd:gnome-panel-control")
    self.uninstall("cmd:openbox-*-session", glob=True)
    self.uninstall("usr/share/gnome*", glob=True)
    self.uninstall("usr/share/xsessions/openbox-*.desktop", glob=True)

    self.rename(
        "usr/share/pixmaps/openbox.png",
        "usr/share/icons/hicolor/48x48/apps/openbox.png",
        relative=False,
    )


@split("devel")
def _(self):
    return self.default_devel()
