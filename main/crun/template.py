pkgname = "crun"
pkgver = "1.18"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://github.com/containers/crun"
source = f"{url}/releases/download/{pkgver}/crun-{pkgver}.tar.zst"
sha256 = "f3aaded71c7592324d79422e6d5489dc71b49a11e706ed95e1cd31720bede48f"


def post_install(self):
    # useless lib that nothing uses and doesn't even come with headers
    self.uninstall("usr/lib/libcrun.a")
