pkgname = "oxygen"
pkgver = "6.0.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_QT5=OFF"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "frameworkintegration-devel",
    "kcmutils-devel",
    "kcompletion-devel",
    "kcoreaddons-devel",
    "kdecoration-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kservice-devel",
    "kwindowsystem-devel",
    "libplasma-devel",
    "qt6-qtdeclarative-devel",
]
depends = [
    f"oxygen-cursors={pkgver}-r{pkgrel}",
    "oxygen-icons",
    "frameworkintegration",
]
pkgdesc = "Oxygen visual style for the KDE Plasma Desktop"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"  # FIXME
url = "https://invent.kde.org/plasma/oxygen"
source = f"$(KDE_SITE)/plasma/{pkgver}/oxygen-{pkgver}.tar.xz"
sha256 = "7e54372d6fdc6b7373d948d9489f3e94b457a6f22a8f00f6eade33cd83ce8022"
# CFI: test
hardening = ["vis", "!cfi"]


@subpackage("oxygen-cursors")
def _cursors(self):
    self.pkgdesc = f"{pkgdesc} (cursor themes)"
    return [
        "usr/share/icons/Oxygen*",
        "usr/share/icons/KDE_Classic",
    ]
