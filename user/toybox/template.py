pkgname = "toybox"
pkgver = "0.8.15"
pkgrel = 0
build_style = "makefile"
make_build_env = {"CBUILD_BYPASS_STRIP_WRAPPER": "1"}
make_check_target = ""
make_use_env = True
hostmakedepends = ["bash", "gsed"]
makedepends = ["linux-headers"]
pkgdesc = "All in one Linux command-line utilities"
license = "0BSD"
url = "https://github.com/landley/toybox"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "52452b68a6cf50f9a9728b0f844b03c4dd1f70463675b202e6cf0475bda3934f"


def configure(self):
    self.do("make", "defconfig")

    self.do(
        "gsed",
        "-i",
        "s/^CONFIG_TOYBOX_ZHELP=.*/# CONFIG_TOYBOX_ZHELP is not set/",
        ".config",
    )


def install(self):
    self.install_file("toybox", "usr/bin", mode=0o755)


def post_install(self):
    self.install_license("LICENSE")
