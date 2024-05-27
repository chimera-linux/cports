pkgname = "spectacle"
# FIXME: update to 24.05.0 after opencv packaging!
pkgver = "24.02.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kpipewire-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "layer-shell-qt-devel",
    "plasma-wayland-protocols",
    "qt6-qtmultimedia-devel",
    "qt6-qtwayland-devel",
    "xcb-util-devel",
    # "purpose-devel",  # TODO: package for export to websites functionality?
]
# depends = [""]
pkgdesc = "KDE Screenshot capture utility"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/spectacle"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/spectacle-{pkgver}.tar.xz"
sha256 = "4118f7355eb0584deb2a88ce46ece7b616880397f0ab2b810cbe4cbc21742152"
# FIXME: cfi kills app on launch
hardening = ["vis", "!cfi"]
