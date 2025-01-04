pkgname = "sq"
pkgver = "0.48.4"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/neilotoole/sq/cli/buildinfo.Version=v{pkgver}"
    " -X github.com/neilotoole/sq/cli/buildinfo.Commit=RELEASE"
]
hostmakedepends = ["go"]
makedepends = ["icu-devel", "sqlite-devel", "libpq-devel"]
go_build_tags = [
    "sqlite_vtable",
    "sqlite_stat4",
    "sqlite_fts5",
    "sqlite_icu",
    "sqlite_introspect",
    "sqlite_json",
    "sqlite_math_functions",
]
pkgdesc = "Tool to inspect, query, join, import, and export structured data"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://sq.io"
source = f"https://github.com/neilotoole/sq/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4692a71da5302f0f392721e9d9f28676d5120aefe90e81dcab54bc3214882977"
# some tests require network
options = ["!check"]


def post_build(self):
    with open(self.cwd / "sq.1", "w") as outf:
        self.do("build/sq", "man", stdout=outf)
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"sq.{shell}", "w") as outf:
            self.do(
                "build/sq",
                "completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("sq.1")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"sq.{shell}", shell)
