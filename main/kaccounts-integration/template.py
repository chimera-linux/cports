pkgname = "kaccounts-integration"
pkgver = "24.12.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/network/kaccounts-integration"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kaccounts-integration-{pkgver}.tar.xz"
sha256 = "04e8a00bdd4539027497edcabc4d7c21932ab00f43a51b1184365735f8d3b433"
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
