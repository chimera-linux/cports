pkgname = "kaccounts-integration"
pkgver = "25.04.2"
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
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/network/kaccounts-integration"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kaccounts-integration-{pkgver}.tar.xz"
sha256 = "0fecd64d0b0bc698bd4c9a13a80daf96d3a77072ddb8616b8bc670b67249d15c"
hardening = ["vis"]


if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    depends += ["signon-ui"]


@subpackage("kaccounts-integration-devel")
def _(self):
    self.depends += [
        "intltool",  # yes, really
        "libaccounts-qt-devel",
        "signond-devel",
    ]
    return self.default_devel()
