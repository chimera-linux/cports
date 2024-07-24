pkgname = "rocksdb"
pkgver = "9.4.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_env = {
    "PORTABLE": "1",
}
make_build_target = ""
make_build_args = [
    "shared_lib",
    "static_lib",
]
make_build_env = {
    "DEBUG_LEVEL": "0",
}
make_use_env = True
hostmakedepends = [
    "bash",
    "gmake",
    "perl",
    "pkgconf",
]
makedepends = [
    "bzip2-devel",
    "gflags-devel-static",
    "liburing-devel",
    "linux-headers",
    "lz4-devel",
    "snappy-devel",
    "zstd-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Embeddable, persistent key-value store for fast storage"
maintainer = "Gnarwhal <git.aspect893@passmail.net>"
license = "(GPL-2.0-or-later OR Apache-2.0) AND BSD-3-Clause"
url = "https://rocksdb.org"
source = f"https://github.com/facebook/rocksdb/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1f829976aa24b8ba432e156f52c9e0f0bd89c46dc0cc5a9a628ea70571c1551c"
tool_flags = {
    "CXXFLAGS": [
        "-D_GNU_SOURCE",
        "-fPIC",
        "-frtti",
    ],
}
# idk
# options = ["!check"]


def init_build(self):
    self.make_build_args += [
        "EXTRA_CFLAGS=" + self.get_cflags(shell=True),
        "EXTRA_LDFLAGS=" + self.get_ldflags(shell=True),
        "EXTRA_CXXFLAGS=" + self.get_cxxflags(shell=True),
    ]


def post_install(self):
    self.install_license("LICENSE.leveldb")


@subpackage(f"{pkgname}-devel")
def _devel(self):
    return self.default_devel()
