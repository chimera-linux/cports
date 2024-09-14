pkgname = "trace-cmd"
pkgver = "3.3"
pkgrel = 1
build_style = "meson"
configure_args = [f"-Dversion-tag={pkgver}"]
make_build_args = ["all", "docs"]
hostmakedepends = [
    "asciidoc",
    "bash",
    "meson",
    "pkgconf",
    "source-highlight",
    "xmlto",
]
makedepends = [
    "audit-devel",
    "libtraceevent-devel",
    "libtracefs-devel",
    "linux-headers",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Linux ftrace CLI tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://www.trace-cmd.org"
source = f"https://git.kernel.org/pub/scm/utils/trace-cmd/trace-cmd.git/snapshot/trace-cmd-v{pkgver}.tar.gz"
sha256 = "0671048dd2b8abdb8b2d0eb9cc91335c997620a7da72f858381ff4206f32065f"
