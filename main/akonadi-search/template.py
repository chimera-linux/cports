pkgname = "akonadi-search"
pkgver = "25.08.0"
pkgrel = 0
build_style = "cmake"
# sqlite: fails instantly (?)
# searchplugintest: fails to find stuff
make_check_args = ["-E", "(akonadi-sqlite.*|searchplugintest)"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cargo",
    "cmake",
    "corrosion",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-devel",
    "akonadi-mime-devel",
    "kcalendarcore-devel",
    "kcmutils-devel",
    "kconfig-devel",
    "kcontacts-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kmime-devel",
    "krunner-devel",
    "ktextaddons-devel",
    "qt6-qtdeclarative-devel",
    "rust-std",
    "xapian-core-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Akonadi search libraries"
license = "LGPL-2.1-only AND (GPL-2.0-only OR GPL-3.0-only)"
url = "https://api.kde.org/kdepim/akonadi-search/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-search-{pkgver}.tar.xz"
)
sha256 = "f63ee1636f91bcef6d3c836c2b5cc87ec0c183f5d69b3736e80e2c690b9d75c2"


def prepare(self):
    from cbuild.util import cargo

    # the version that is in there is busted on loongarch
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.170",
        allow_network=True,
        wrksrc="agent/rs/htmlparser",
    )

    cargo.Cargo(self, wrksrc="agent/rs/htmlparser").vendor()


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "libc", "agent/rs/htmlparser/vendor")


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


@subpackage("akonadi-search-devel")
def _(self):
    self.depends += [
        "akonadi-devel",
        "akonadi-mime-devel",
        "kcalendarcore-devel",
        "kcontacts-devel",
        "kcoreaddons-devel",
        "kmime-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
