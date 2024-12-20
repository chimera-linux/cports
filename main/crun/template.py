pkgname = "crun"
pkgver = "1.19.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://github.com/containers/crun"
source = f"{url}/releases/download/{pkgver}/crun-{pkgver}.tar.zst"
sha256 = "969d66362ecea59f6d93c463739178ac6c2b75eda7a550a45de413e2d92def11"


def post_install(self):
    # useless lib that nothing uses and doesn't even come with headers
    self.uninstall("usr/lib/libcrun.a")
