pkgname = "mimetreeparser"
pkgver = "24.05.1"
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
sha256 = "cd4466bb62a7055314cae10b8af63097e2fd35881271137b74ea3690886b3836"


@subpackage("mimetreeparser-devel")
def _devel(self):
    self.depends += [
        "ki18n-devel",
        "ki18n-devel",
        "kmbox-devel",
        "kmime-devel",
        "mailimporter-devel",
    ]
    return self.default_devel()
