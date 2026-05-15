pkgname = "sq"
pkgver = "0.50.0"
pkgrel = 1
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/neilotoole/sq/cli/buildinfo.Version=v{pkgver}"
    " -X github.com/neilotoole/sq/cli/buildinfo.Commit=RELEASE"
]
hostmakedepends = ["go"]
makedepends = ["icu-devel", "sqlite-devel", "postgresql16-client-devel"]
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
license = "MIT"
url = "https://sq.io"
source = f"https://github.com/neilotoole/sq/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "36e20553b05aa10069ea3a422bbd98df936f5ca505eae9d61b98ff7ee0b7a279"
# check: some tests require network
# cross: generates manpages/completions with host bins
options = ["!check", "!cross"]


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
