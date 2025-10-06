pkgname = "duckdb"
pkgver = "1.4.1"
_pkghash = "b8a06e4a22"
pkgrel = 0
# https://duckdblabs.com/community_support_policy/
archs = ["aarch64", "x86_64"]
build_style = "cmake"
configure_args = [
    f"-DOVERRIDE_GIT_DESCRIBE=v{pkgver}-0-g{_pkghash}",
    "-DMUSL_ENABLED=ON",
    "-DCORE_EXTENSIONS='autocomplete;icu;json;parquet'",
    "-DSKIP_EXTENSIONS='jemalloc'",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
makedepends = ["openssl3-devel"]
pkgdesc = "High-performance analytical database system"
license = "MIT"
url = "https://duckdb.org"
source = f"https://github.com/duckdb/duckdb/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "91e55efe2c1627c4432d620ee9d2ffcd72f954699e76d7dab523348a7dfbb00a"


match self.profile().arch:
    case "x86_64":
        configure_args += ["-DDUCKDB_EXPLICIT_PLATFORM=linux_amd64"]
    case "aarch64":
        configure_args += ["-DDUCKDB_EXPLICIT_PLATFORM=linux_arm64"]


def post_install(self):
    self.install_license("LICENSE")


def check(self):
    self.do("./build/test/unittest", "*")


@subpackage("duckdb-devel")
def _(self):
    return self.default_devel()
