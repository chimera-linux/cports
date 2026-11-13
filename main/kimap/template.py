pkgname = "kimap"
pkgver = "26.08.3"
pkgrel = 0
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
license = "LGPL-2.0-or-later"
url = "https://community.kde.org/KDE_PIM"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kimap-{pkgver}.tar.xz"
sha256 = "b3c74e3652f0b2ced6bb10c356472ddca48b17728d23c12598d1a0f7bc2f976a"


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
