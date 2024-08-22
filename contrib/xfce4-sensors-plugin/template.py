pkgname = "xfce4-sensors-plugin"
pkgver = "1.4.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-procapi", "--enable-sysfsacpi"]
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "intltool",
    "libtool",
    "pkgconf",
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
sha256 = "6c1605a738e5df40e084d08ac93f962cd445093396de1e9bfadc7ab4588c36b6"


@subpackage("xfce4-sensors-plugin-devel")
def _(self):
    return self.default_devel()
