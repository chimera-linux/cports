pkgname = "trace-cmd"
pkgver = "3.3.1"
pkgrel = 0
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
sha256 = "2efe103389367e93c764c4a788880ba51018a65dec21b0411965a5f06a6338c1"


def post_install(self):
    self.rename(
        "usr/share/bash-completion/completions/trace-cmd.bash", "trace-cmd"
    )
