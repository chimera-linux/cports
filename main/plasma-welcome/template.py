pkgname = "plasma-welcome"
pkgver = "6.4.3"
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
    "kirigami-devel",
    "kirigami-addons-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kconfigwidgets-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "knewstuff-devel",
    "kservice-devel",
    "kwindowsystem-devel",
    "kdbusaddons-devel",
    "kcmutils-devel",
    "ksvg-devel",
    "kjobwidgets-devel",
    "kuserfeedback-devel",
    "libplasma-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
depends = ["kuserfeedback"]
pkgdesc = "KDE onboarding wizard"
license = "GPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-welcome"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-welcome-{pkgver}.tar.xz"
sha256 = "d71cd6399f759fa4fcfa30f508a460ab37d2ab4fbdcddf9a2e7f2b5ab870b463"


@subpackage("plasma-welcome-devel-static")
def _(self):
    return ["usr/lib/*.a"]


@subpackage("plasma-welcome-devel")
def _(self):
    # pull in static-only public plugin lib .a
    self.depends += [self.with_pkgver("plasma-welcome-devel-static")]
    self.options = ["empty"]
    return self.default_devel()
