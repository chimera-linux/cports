pkgname = "xwaylandvideobridge"
pkgver = "0.4.0"
pkgrel = 3
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kcoreaddons-devel",
    "ki18n-devel",
    "knotifications-devel",
    "kpipewire-devel",
    "kstatusnotifieritem-devel",
    "kwindowsystem-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "xcb-util-devel",
]
pkgdesc = "Utility to stream Wayland screens/windows to X11 applications"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/system/xwaylandvideobridge"
source = f"$(KDE_SITE)/xwaylandvideobridge/xwaylandvideobridge-{pkgver}.tar.xz"
sha256 = "ea72ac7b2a67578e9994dcb0619602ead3097a46fb9336661da200e63927ebe6"
hardening = ["vis"]
