pkgname = "lilv"
pkgver = "0.24.24"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libsndfile-devel",
    "python-devel",
    "serd-devel",
    "sord-devel",
    "sratom-devel",
    "lv2",
]
pkgdesc = "C API for using LV2 plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/lilv.html"
source = f"https://download.drobilla.net/{pkgname}-{pkgver}.tar.xz"
sha256 = "6bb6be9f88504176d0642f12de809b2b9e2dc55621a68adb8c7edb99aefabb4f"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")
    self.rename(
        "etc/bash_completion.d/lilv",
        "usr/share/bash-completion/completions/lilv",
        relative=False,
    )


@subpackage("lilv-devel")
def _devel(self):
    return self.default_devel()


@subpackage("lilv-progs")
def _progs(self):
    return self.default_progs()
