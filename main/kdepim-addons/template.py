pkgname = "kdepim-addons"
pkgver = "24.08.3"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = [
    "dbus-run-session",
    "--",
    "wlheadless-run",
    "--",
]
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "corrosion",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-calendar-devel",
    "akonadi-contacts-devel",
    "akonadi-devel",
    "akonadi-import-wizard-devel",
    "akonadi-notes-devel",
    "discount-devel",
    "eventviews-devel",
    "gpgme-devel",
    "grantleetheme-devel",
    "incidenceeditor-devel",
    "kaddressbook-devel",
    "kcalendarcore-devel",
    "kcalutils-devel",
    "kconfig-devel",
    "kcontacts-devel",
    "kdbusaddons-devel",
    "kdeclarative-devel",
    "kguiaddons-devel",
    "kholidays-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kidentitymanagement-devel",
    "kimap-devel",
    "kio-devel",
    "kitinerary-devel",
    "kmailtransport-devel",
    "kmime-devel",
    "kparts-devel",
    "kpimtextedit-devel",
    "kpkpass-devel",
    "ktextaddons-devel",
    "ktexttemplate-devel",
    "ktnef-devel",
    "kxmlgui-devel",
    "libgravatar-devel",
    "libkdepim-devel",
    "libkleo-devel",
    "libksieve-devel",
    "mailcommon-devel",
    "mailimporter-devel",
    "messagelib-devel",
    "pimcommon-devel",
    "prison-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtwebengine-devel",
    "rust-std",
    "syntax-highlighting-devel",
]
depends = ["kirigami-addons"]
checkdepends = ["dbus", "xwayland-run", *depends]
pkgdesc = "KDE PIM application addons"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND GPL-2.0-or-later"
url = "https://invent.kde.org/pim/kdepim-addons"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kdepim-addons-{pkgver}.tar.xz"
)
sha256 = "0db2033c3c673766c3267391b528920c7ecf66bf2033a8a69c6eb4fca5b1a549"
# date diffs, formatting diffs, cant find plugins, ...
options = ["!check"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc="plugins/webengineurlinterceptor/adblock").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)
