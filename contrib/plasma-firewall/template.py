pkgname = "plasma-firewall"
pkgver = "6.0.5"
pkgrel = 0
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
sha256 = "0b52e7413cc745d97bb16a38ac40612ffb7dc7e4323e156fa17d923425c4b30e"


# TODO: it also supports firewalld but i did not test that
@subpackage("plasma-firewall-ufw")
def _ufw(self):
    self.pkgdesc = f"{pkgdesc} (ufw support)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends += ["ufw"]
    self.options = ["empty"]
    return []
