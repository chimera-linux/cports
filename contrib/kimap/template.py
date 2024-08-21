pkgname = "kimap"
pkgver = "24.05.2"
pkgrel = 1
build_style = "cmake"
# no valid mechs
# make_check_args = ["-E", "loginjobtest"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kmime-devel",
    "libsasl-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE IMAP access API"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kdepim/kimap/html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kimap-{pkgver}.tar.xz"
sha256 = "167bed276867fb9536e86f8ecac36911b51c90b3f13e167118b44a1d46eb96e0"


@subpackage("kimap-devel-static")
def _(self):
    return ["usr/lib/*.a"]


@subpackage("kimap-devel")
def _(self):
    self.depends += [
        # for cmake detection.. static-only test lib
        self.with_pkgver("kimap-devel-static"),
        "kcoreaddons-devel",
        "kmime-devel",
    ]
    return self.default_devel()
