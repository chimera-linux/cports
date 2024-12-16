pkgname = "xfce4-settings"
pkgver = "4.20.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-sound-settings",
    "--enable-upower-glib",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libxml2-progs",
    "pkgconf",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "colord-devel",
    "exo-devel",
    "fontconfig-devel",
    "garcon-devel",
    "glib-devel",
    "gtk+3-devel",
    "gtk-layer-shell-devel",
    "libnotify-devel",
    "libx11-devel",
    "libxcursor-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxi-devel",
    "libxklavier-devel",
    "libxrandr-devel",
    "upower-devel",
    "xfconf-devel",
    "xorgproto",
    "xserver-xorg-input-libinput-devel",
]
pkgdesc = "Xfce settings app"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-only"
url = "https://docs.xfce.org/xfce/xfce4-settings/start"
source = f"$(XFCE_SITE)/xfce/xfce4-settings/{pkgver[:-2]}/xfce4-settings-{pkgver}.tar.bz2"
sha256 = "23548da3429a296501fbfdbc98a861ee241b9fdd47e8d5de1781f57c6bbce5a9"


@subpackage("xfce4-settings-default-themes")
def _(self):
    self.subdesc = "default themes"
    self.install_if = [self.parent]
    # See patches/defaults.patch
    self.depends = ["adw-gtk3", "adwaita-icon-theme", "papirus-icon-theme"]
    self.options = ["empty"]

    return []
