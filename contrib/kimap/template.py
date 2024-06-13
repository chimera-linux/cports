pkgname = "kimap"
pkgver = "24.05.1"
pkgrel = 0
build_style = "cmake"
# no valid mechs
make_check_args = ["-E", "loginjobtest"]
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
sha256 = "b227112a6e8b585a5ea40ffa5b393a62dbf122ee46f6541e787f33c8f8c6cedd"


@subpackage("kimap-devel-static")
def _devel_static(self):
    self.pkgdesc = f"{pkgdesc} (development files) (static libraries)"
    return ["usr/lib/*.a"]


@subpackage("kimap-devel")
def _devel(self):
    self.depends += [
        # for cmake detection.. static-only test lib
        f"kimap-devel-static={pkgver}-r{pkgrel}",
        "kcoreaddons-devel",
        "kmime-devel",
    ]
    return self.default_devel()
