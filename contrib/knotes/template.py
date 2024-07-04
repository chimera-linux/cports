pkgname = "knotes"
pkgver = "24.05.2"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "akonadi-devel",
    "akonadi-notes-devel",
    "akonadi-search-devel",
    "grantleetheme-devel",
    "kcalutils-devel",
    "kcmutils-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdnssd-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kitemmodels-devel",
    "kitemviews-devel",
    "kmime-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kontactinterface-devel",
    "kparts-devel",
    "kstatusnotifieritem-devel",
    "ktextaddons-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "pimcommon-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["kdepim-runtime"]
checkdepends = ["xwayland-run"] + depends
pkgdesc = "KDE sticky notes"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "(LGPL-2.1-only OR LGPL-3.0-only) AND GPL-2.0-or-later"
url = "https://apps.kde.org/knotes"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/knotes-{pkgver}.tar.xz"
sha256 = "4e6da68e1ccfd5a2fcaf038a6438bef7b671446b05a3e739787b63689016d592"
