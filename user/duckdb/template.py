pkgname = "duckdb"
pkgver = "1.5.4"
pkgrel = 0
# https://duckdblabs.com/community_support_policy/
archs = ["aarch64", "x86_64"]
build_style = "cmake"
configure_args = [
    f"-DOVERRIDE_GIT_DESCRIBE=v{pkgver}",
    "-DENABLE_JEMALLOC=OFF",
    "-DMUSL_ENABLED=ON",
    "-DCORE_EXTENSIONS='autocomplete;icu;json;parquet'",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
makedepends = ["openssl3-devel"]
pkgdesc = "High-performance analytical database system"
license = "MIT"
url = "https://duckdb.org"
source = f"https://github.com/duckdb/duckdb/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "99c36e4bf415f295e19ed67401adb72e075e63e6a0dc3a14312c986e29781fd0"
# tests take an eternity and are intermittently flaky and also not rerunnable
# recheck upon updates but don't enable for builders
options = ["!check"]


match self.profile().arch:
    case "x86_64":
        configure_args += ["-DDUCKDB_EXPLICIT_PLATFORM=linux_amd64_musl"]
    case "aarch64":
        configure_args += ["-DDUCKDB_EXPLICIT_PLATFORM=linux_arm64_musl"]


def post_install(self):
    self.install_license("LICENSE")


def check(self):
    self.do("./build/test/unittest", "*")


@subpackage("duckdb-devel")
def _(self):
    self.depends += [self.parent]

    return self.default_devel()
