pkgname = "kaccounts-integration"
pkgver = "25.08.3"
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
    "signon-kwallet-extension",
    # TODO: maybe these should go elsewhere
    "signon-plugin-oauth2",
]
pkgdesc = "KDE integration for Accounts-SSO and SignOn-SSO"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/network/kaccounts-integration"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kaccounts-integration-{pkgver}.tar.xz"
sha256 = "7fa0343f0c3f59375c4817cbd29b0fed7e45cbb31f4956e6d3f62c0abe2a1c8b"
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
