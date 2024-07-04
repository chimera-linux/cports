pkgname = "signon-plugin-oauth2"
# fewer deprecations
pkgver = "0.25_git20210102"
pkgrel = 1
_gitrev = "d759439066f0a34e5ad352ebab0b3bb2790d429e"
build_style = "makefile"
make_cmd = "gmake"
make_use_env = True
hostmakedepends = [
    "gmake",
    "pkgconf",
    "qt6-qtbase",
]
makedepends = [
    "qt6-qtbase-devel",
    "signond-devel",
]
pkgdesc = "Oauth 1.0 and 2.0 plugin for signond"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-only"
url = "https://gitlab.com/accounts-sso/signon-plugin-oauth2"
source = f"{url}/-/archive/{_gitrev}.tar.gz"
sha256 = "e27678964563cbb64d9bd4088c4c7876bb2202c8e7af8ea77d8f27c578a8d6e4"


def do_configure(self):
    # TODO: build style these
    self.do(
        "qmake6",
        "LIBDIR=/usr/lib",
        "PREFIX=/usr",
        f"QMAKE_CFLAGS={self.get_cflags(shell=True)}",
        f"QMAKE_CXXFLAGS={self.get_cxxflags(shell=True)}",
        f"QMAKE_LFLAGS={self.get_ldflags(shell=True)}",
    )


def init_install(self):
    self.make_install_args += [f"INSTALL_ROOT={self.chroot_destdir}"]


def post_install(self):
    # mistakenly installed
    self.uninstall("usr/bin/signon-oauth2plugin-tests")
    self.uninstall("usr/share/signon-oauth2plugin-tests")


@subpackage("signon-plugin-oauth2-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel()
