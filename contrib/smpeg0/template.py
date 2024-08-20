pkgname = "smpeg0"
pkgver = "0.4.5"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["sdl12-compat-devel", "glu-devel"]
pkgdesc = "MPEG decoding library for SDL 1.2"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "LGPL-2.1-or-later"
url = "https://icculus.org/smpeg"
source = f"https://github.com/icculus/smpeg/archive/refs/tags/release_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "e2e53bfd2e6401e2c29e5eb3929be0e8698bc9e4c9d731751f67e77b408f1f74"
tool_flags = {"CFLAGS": ["-Dregister=", "-fPIC"]}


@subpackage("smpeg0-devel")
def _(self):
    return self.default_devel()


# so cmd:plaympeg doesn't conflict with smpeg proper
# below -devel so it doesn't pick up smpeg-config
@subpackage("smpeg0-progs")
def _(self):
    return self.default_progs()
