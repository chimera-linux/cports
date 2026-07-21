pkgname = "gnupg"
pkgver = "2.4.9"
pkgrel = 1
_freepg_rel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-all-tests",
    "--enable-large-secmem",
]
configure_gen = []
make_check_env = {"TESTFLAGS": f"--parallel={self.conf_jobs}"}
hostmakedepends = ["pkgconf", "libgpg-error-progs", "texinfo"]
# TODO: switch to libedit once it gains missing features
makedepends = [
    "bzip2-devel",
    "gnutls-devel",
    "libassuan-devel",
    "libgcrypt-devel",
    "libgpg-error-devel",
    "libksba-devel",
    "libusb-devel",
    "npth-devel",
    "openldap-devel",
    "readline-devel",
    "sqlite-devel",
]
depends = ["pinentry"]
pkgdesc = "GNU Privacy Guard 2.x"
license = "GPL-3.0-or-later"
url = "https://www.gnupg.org"
source = [
    f"https://gnupg.org/ftp/gcrypt/gnupg/gnupg-{pkgver}.tar.bz2",
    f"https://gitlab.com/freepg/gnupg/-/archive/source-{pkgver}-freepg-{_freepg_rel}/gnupg-source-{pkgver}-freepg-{_freepg_rel}.tar.gz",
]
source_paths = [".", "freepg"]
sha256 = [
    "dd17ab2e9a04fd79d39d853f599cbc852062ddb9ab52a4ddeb4176fd8b302964",
    "9d971136172c1370731586563b96596770d3ad5b9f40b22aaeeb61da8ba900ff",
]


def post_extract(self):
    from cbuild.util import patch

    plist = sorted(
        (
            self.cwd
            / f"freepg/STABLE-BRANCH-{pkgver[:-2].replace('.', '-')}-freepg"
        ).glob("*.patch")
    )
    if len(plist) == 0:
        self.error("no freepg patches found")

    patch.patch(self, plist, stamp=True)
