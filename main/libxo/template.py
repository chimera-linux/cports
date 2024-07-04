pkgname = "libxo"
pkgver = "1.7.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = []
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["musl-bsd-headers"]
pkgdesc = "Library for generating text, XML, JSON, and HTML output"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/Juniper/libxo"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "d12249ffad3ef04b160e6419adf1bbe7e593a60bb23f0a0a077fa780b214934a"
tool_flags = {"CFLAGS": ["-Wno-unused-command-line-argument"]}
options = ["bootstrap"]

if self.stage > 0:
    # otherwise we get .a files for plugins
    configure_args += ["--disable-static", "--enable-gettext"]
else:
    configure_args += [
        "--disable-libxo-options",
        "--disable-gettext",
        "--disable-shared",
        "--enable-text-only",
    ]


# libxo does not respect LDFLAGS, so hack it in
def init_configure(self):
    tcflags = self.get_cflags(shell=True)
    tlflags = self.get_ldflags(shell=True)

    self.configure_env = {"CFLAGS": f"{tcflags} {tlflags}"}


def post_install(self):
    self.install_license("Copyright")

    if self.stage == 0:
        self.uninstall("usr/lib/libxo")


@subpackage("libxo-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libxo-progs")
def _progs(self):
    return self.default_progs()
