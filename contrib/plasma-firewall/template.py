pkgname = "plasma-firewall"
pkgver = "6.1.3"
pkgrel = 1
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ki18n-devel",
    "kconfig-devel",
    "kcmutils-devel",
    "kauth-devel",
    "libplasma-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE control panel for the system firewall"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-firewall"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-firewall-{pkgver}.tar.xz"
sha256 = "f2a0a74e01969630cd21a0f03697a924ea33d6da2f92b08d900d28b97843cf93"


# TODO: it also supports firewalld but i did not test that
@subpackage("plasma-firewall-ufw")
def _ufw(self):
    self.subdesc = "ufw support"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "ufw"]
    self.depends += ["ufw"]
    self.options = ["empty"]
    return []
