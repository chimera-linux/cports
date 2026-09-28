pkgname = "duperemove"
pkgver = "0.15.2"
pkgrel = 0
build_style = "makefile"
make_build_env = {
    "VERSION": f"v{pkgver}",
    "IS_RELEASE": "1",
}
hostmakedepends = ["pkgconf"]
makedepends = [
    "glib-devel",
    "linux-headers",
    "musl-bsd-headers",
    "sqlite-devel",
    "xxhash-devel",
]
pkgdesc = "Tools for deduplicating extents in filesystems like Btrfs"
license = "GPL-2.0-only"
url = "https://github.com/markfasheh/duperemove"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "27809aa91b7b9b7d0810e5329614bf80af2c48e917781e682a3fbcf61fa274da"
tool_flags = {"CFLAGS": ["-std=c23"]}
hardening = ["vis", "cfi"]
# no test suite exists
options = ["!check"]
