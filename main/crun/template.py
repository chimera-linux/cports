pkgname = "crun"
pkgver = "1.23.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-systemd"]
# broken presently
configure_gen = []
# full testsuite fails in netns
make_check_target = "tests/tests_libcrun_errors.log"
hostmakedepends = [
    "go-md2man",
    "pkgconf",
    "python",
]
makedepends = [
    "argp-standalone",
    "libcap-devel",
    "libseccomp-devel",
    # -static for test build from all target
    "libunwind-devel-static",
    "yajl-devel",
]
pkgdesc = "Fast and lightweight OCI runtime"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://github.com/containers/crun"
source = f"{url}/releases/download/{pkgver}/crun-{pkgver}.tar.zst"
sha256 = "6cea8d41e4be425ba2fa55587e16e44ddbe2fa333b367024e68235b922e26056"


def post_install(self):
    # useless lib that nothing uses and doesn't even come with headers
    self.uninstall("usr/lib/libcrun.a")
