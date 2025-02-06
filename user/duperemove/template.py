pkgname = "duperemove"
pkgver = "0.15"
pkgrel = 0
build_style = "makefile"
make_build_env = {
    "VERSION": f"v{pkgver}",
    "IS_RELEASE": "1",
}
hostmakedepends = ["pkgconf"]
makedepends = [
    "glib-devel",
    "musl-bsd-headers",
    "sqlite-devel",
    "xxhash-devel",
    "linux-headers",
]
pkgdesc = "Tools for deduplicating extents in filesystems like Btrfs"
maintainer = "autumnontape <autumn@cyfox.net>"
license = "GPL-2.0-only"
url = "https://github.com/markfasheh/duperemove"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1dacde51f12ead1da6b067d5520731a83adee3301fbc36eb282cf8362b93d773"
tool_flags = {"CFLAGS": ["-std=c23"]}
hardening = ["vis", "cfi"]
# no test suite exists
options = ["!check"]
