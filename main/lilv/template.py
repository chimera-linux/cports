pkgname = "lilv"
pkgver = "0.28.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libsndfile-devel",
    "lv2",
    "python-devel",
    "serd-devel",
    "sord-devel",
    "sratom-devel",
]
pkgdesc = "C API for using LV2 plugins"
license = "ISC"
url = "https://drobilla.net/software/lilv.html"
source = f"https://download.drobilla.net/lilv-{pkgver}.tar.xz"
sha256 = "8dcb70adb5cf072335115a6b091f4113710bdc73abaadaa3f9e9c1e55957b149"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")
    self.rename(
        "etc/bash_completion.d/lilv",
        "usr/share/bash-completion/completions/lv2info",
        relative=False,
    )


@subpackage("lilv-devel")
def _(self):
    return self.default_devel()


@subpackage("lilv-progs")
def _(self):
    return self.default_progs()
