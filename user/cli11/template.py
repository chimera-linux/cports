pkgname = "cli11"
pkgver = "2.6.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
checkdepends = ["catch2-devel"]
pkgdesc = "CLI11 is a command line parser for C++11 and beyond"
license = "custom:cli11"
url = "https://github.com/CLIUtils/CLI11"
source = f"https://github.com/CLIUtils/CLI11/archive/refs/tags/v{pkgver}.zip"
sha256 = "44fd2b73ea6df72876cb0c53796062b2870c73495840b732c3451d5250316258"


def post_install(self):
    self.install_license("LICENSE")
