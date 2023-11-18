pkgname = "geany"
pkgver = "2.0.0"
pkgrel = 1
build_style = "gnu_configure"
configure_env = {"NOCONFIGURE": "1"}
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "gettext",
    "gmake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
]
checkdepends = ["bash"]
depends = ["desktop-file-utils"]
pkgdesc = "Gtk+3 IDE"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://geany.org"
source = f"https://github.com/geany/geany/releases/download/{pkgver}/geany-{pkgver[:-2]}.tar.gz"
sha256 = "50d28a45ac9b9695e9529c73fe7ed149edb512093c119db109cea6424114847f"

if self.profile().arch == "aarch64":
    # work around builtins not being linked properly
    tool_flags = {
        "CXXFLAGS": ["-mno-outline-atomics"],
        "CFLAGS": ["-mno-outline-atomics"],
    }


@subpackage("geany-devel")
def _devel(self):
    return self.default_devel()
