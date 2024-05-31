pkgname = "kaccounts-integration"
pkgver = "24.05.0"
pkgrel = 1
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcmutils-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kwallet-devel",
    "libaccounts-qt-devel",
    "qcoro-devel",
    "qt6-qtdeclarative-devel",
    "signond-devel",
]
depends = [
    # TODO: maybe these should go elsewhere
    "signon-plugin-oauth2",
    "signon-kwallet-extension",
]
pkgdesc = "KDE integration for Accounts-SSO and SignOn-SSO"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/network/kaccounts-integration"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kaccounts-integration-{pkgver}.tar.xz"
sha256 = "8f2022c1e97d5a0d054aab73a738d56ad25800aff145cc837ff65ca95026c3e8"
# CFI: check
hardening = ["vis", "!cfi"]


if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    depends += ["signon-ui"]


@subpackage("kaccounts-integration-devel")
def _devel(self):
    self.depends += [
        "intltool",  # yes, really
        "libaccounts-qt-devel",
        "signond-devel",
    ]
    return self.default_devel()
