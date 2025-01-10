pkgname = "xfce4-verve-plugin"
pkgver = "2.0.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "gtk+3-devel",
    "libxfce4ui-devel",
    "pcre2-devel",
    "xfce4-panel-devel",
]
pkgdesc = "Xfce command line panel plugin"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-verve-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-verve-plugin/{pkgver[:-2]}/xfce4-verve-plugin-{pkgver}.tar.bz2"
sha256 = "214a812dd7cc410bbe85d736e0dc76459ddd7861e5a1c60b67dd89dcd34e90a1"
