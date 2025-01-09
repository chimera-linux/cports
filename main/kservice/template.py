pkgname = "kservice"
pkgver = "6.9.0"
pkgrel = 0
build_style = "cmake"
# flaky tests when parallel
make_check_args = ["-j1", "-E", "(kservicetest|kapplicationtradertest)"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Plugin framework for desktop services"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kservice/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kservice-{pkgver}.tar.xz"
sha256 = "f4ff574f422b27575f04c7491694162c61c7db4ad923565408fa23b9a7e9675f"
hardening = ["vis"]


@subpackage("kservice-devel")
def _(self):
    self.depends += ["kconfig-devel", "kcoreaddons-devel"]

    return self.default_devel()
