pkgname = "thunar-vcs-plugin"
pkgver = "0.4.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
]
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "apr-devel",
    "apr-util-devel",
    "exo-devel",
    "gtk+3-devel",
    "libxfce4ui-devel",
    "subversion-devel",
    "thunar-devel",
]
pkgdesc = "Thunar VCS plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/thunar/thunar-vcs-plugin"
source = f"$(XFCE_SITE)/thunar-plugins/thunar-vcs-plugin/{pkgver[:-2]}/thunar-vcs-plugin-{pkgver}.tar.xz"
sha256 = "0e4170e099c9ffedfcbb1290f1fc42c00560cf6108e25fe90685315f18c8d6cc"
