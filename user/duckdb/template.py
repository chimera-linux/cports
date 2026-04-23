pkgname = "duckdb"
pkgver = "1.4.2"
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
sha256 = "43193b3661e0f6dce8a1ad9144bbd21c42601fe0e84efee7b3577a4bb160965c"


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
    return self.default_devel()
