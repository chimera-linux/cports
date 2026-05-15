pkgname = "gdu"
pkgver = "5.35.0"
pkgrel = 1
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/dundee/gdu/v5/build.Version={pkgver}",
    "./cmd/gdu",
]
# TestOutputFileError: expects writing to /xyzxyz to give eperm instead of erofs (which happens in --ro bwrap)
# TestAnalyzePathWithIgnoring&&TestViewFile: fails to run
make_check_args = [
    "-skip",
    "TestOutputFileError|TestAnalyzePathWithIgnoring|TestViewFile",
    "./...",
]
hostmakedepends = ["go"]
pkgdesc = "Disk usage analyzer"
license = "MIT"
url = "https://github.com/dundee/gdu"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2c0e4fe412a828e1c0f414f7c230b994e44356c4753c3546c67e8178db500535"
# check may be disabled
options = []

# err: while opening file: /tmp/badger/000003.vlog err: cannot allocate memory
if self.profile().wordsize == 32:
    options += ["!check"]


# avoid installing build.go file inside make_dir
def install(self):
    self.install_bin("build/gdu")


def post_install(self):
    self.install_man("gdu.1")
    self.install_license("LICENSE.md")
