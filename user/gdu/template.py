pkgname = "gdu"
pkgver = "5.33.0"
pkgrel = 0
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
sha256 = "14419fa66046c9fc2d1a6deae0c784c4ac5561ba97e1bd39d622293530ed2788"
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
