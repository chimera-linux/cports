pkgname = "xfce4-mixer"
pkgver = "4.20.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gstreamer-devel",
    "gtk+3-devel",
    "libkeybinder3-devel",
    "libpulse-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce volume control app"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/xfce4-mixer/start"
source = (
    f"$(XFCE_SITE)/apps/xfce4-mixer/{pkgver[:-2]}/xfce4-mixer-{pkgver}.tar.xz"
)
sha256 = "d603be3aec26a16b9d98b9bd71555f80467d556547de50b86337bbf4708ddcaf"
