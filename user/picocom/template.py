pkgname = "picocom"
pkgver = "2024.07"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "CFLAGS += -DNO_CUSTOM_BAUD",
    "picocom",
    "doc",
]
make_use_env = True
hostmakedepends = ["go-md2man"]
pkgdesc = "Minimal dumb-terminal emulation program like minicom"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/wsakernel/picocom"
source = f"{url}/-/archive/{pkgver.replace('.', '-')}/{pkgname}-{pkgver.replace('.', '-')}.tar.gz"
sha256 = "4379de2ec591a5848123f37ccdbc7fbeee6dd3520ef1ce4119d84202fc268a17"
hardening = ["cfi", "vis"]
# no tests available
options = ["!check"]


def install(self):
    self.install_bin("picocom")
    self.install_man("picocom.1")
