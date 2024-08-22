pkgname = "xfce4-cpufreq-plugin"
pkgver = "1.2.8"
pkgrel = 0
build_style = "gnu_configure"
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
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce CPU governor and frequency panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-cpufreq-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-cpufreq-plugin/{pkgver[:-2]}/xfce4-cpufreq-plugin-{pkgver}.tar.bz2"
sha256 = "07e458d9f4725e572001fb7eb66b9e931792311146e0f75ad5d87b9ae19573e9"
