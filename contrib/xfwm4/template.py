pkgname = "xfwm4"
pkgver = "4.18.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-poswin", "--enable-xi2"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "libtool",
    "gettext-devel",
    "gmake",
    "intltool",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libepoxy-devel",
    "libwnck-devel",
    "libxext-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxpresent-devel",
    "libxres-devel",
    "startup-notification-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce window manager"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/xfwm4/start"
source = f"$(XFCE_SITE)/xfce/xfwm4/{pkgver[:-2]}/xfwm4-{pkgver}.tar.bz2"
sha256 = "92cd1b889bb25cb4bc06c1c6736c238d96e79c1e706b9f77fad0a89d6e5fc13f"


@subpackage("xfwm4-default-themes")
def _default_themes(self):
    self.pkgdesc = f"{pkgdesc} (default themes)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    # See patches/default-theme.patch
    self.depends = ["adw-xfwm4"]
    self.options = ["empty"]

    return []
