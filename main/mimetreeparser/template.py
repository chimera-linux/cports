pkgname = "mimetreeparser"
pkgver = "24.12.2"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-j1"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gpgme-devel",
    "kcalendarcore-devel",
    "kcodecs-devel",
    "ki18n-devel",
    "kmbox-devel",
    "kmime-devel",
    "kwidgetsaddons-devel",
    "libkleo-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE parser for MIME trees"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-only AND GPL-3.0-only"
url = "https://invent.kde.org/pim/mimetreeparser"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/mimetreeparser-{pkgver}.tar.xz"
)
sha256 = "edb23e2a4c39052a5ad40bb2e0759c45c41fe3644d8f3739dd06a42af20b0a4a"


@subpackage("mimetreeparser-devel")
def _(self):
    self.depends += [
        "ki18n-devel",
        "ki18n-devel",
        "kmbox-devel",
        "kmime-devel",
        "mailimporter-devel",
    ]
    return self.default_devel()
