pkgname = "psmisc"
pkgver = "23.5"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "automake"]
makedepends = ["ncurses-devel", "gnu-getopt"]
checkdepends = ["dejagnu"]
pkgdesc = "Small utilities that use the proc file-system"
maintainer = "roastveg <louis@hamptonsoftworks.com>"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/psmisc/psmisc"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "dc37ecc2f7e4a90a94956accc6e1c77adb71316b7c9cbd39b26738db0c3ae58b"
tool_flags = {"LDFLAGS": ["-lgnu_getopt"], "CFLAGS": ["-Dgetopt_long_only=gnu_getopt_long_only"]}

def pre_check(self):
    # ERROR: global config file /builddir/psmisc-23.5/testsuite/global-conf.exp not found.
    (self.cwd / "testsuite/global-conf.exp").touch()

# FIXME visibility
hardening = ["!vis"]
