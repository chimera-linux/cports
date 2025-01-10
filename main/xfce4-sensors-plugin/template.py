pkgname = "xfce4-sensors-plugin"
pkgver = "1.4.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-procapi", "--enable-sysfsacpi"]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "gtk+3-devel",
    "libnotify-devel",
    "libsensors-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce hardware sensors panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-sensors-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-sensors-plugin/{pkgver[:-2]}/xfce4-sensors-plugin-{pkgver}.tar.bz2"
sha256 = "f69fdf79b7f76d2a81724828124a6fce76803a9122a4c82de8f3dfa3efbb179a"


@subpackage("xfce4-sensors-plugin-devel")
def _(self):
    return self.default_devel()
