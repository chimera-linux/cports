pkgname = "xfwm4"
pkgver = "4.20.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-poswin",
    "--enable-xi2",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
    "slibtool",
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
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/xfwm4/start"
source = f"$(XFCE_SITE)/xfce/xfwm4/{pkgver[:-2]}/xfwm4-{pkgver}.tar.bz2"
sha256 = "a58b63e49397aa0d8d1dcf0636be93c8bb5926779aef5165e0852890190dcf06"


@subpackage("xfwm4-default-themes")
def _(self):
    self.subdesc = "default themes"
    self.install_if = [self.parent]
    # See patches/default-theme.patch
    self.depends = ["adw-xfwm4"]
    self.options = ["empty"]

    return []
