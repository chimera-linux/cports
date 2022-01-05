pkgname = "ruby"
pkgver = "3.1.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-shared", "--disable-rpath", "--disable-install-doc",
    "ac_cv_func_isnan=yes", "ac_cv_func_isinf=yes"
]
make_cmd = "gmake"
make_build_args = ["all", "capi"]
make_install_env = {"MAKE": "gmake"}
hostmakedepends = ["gmake", "pkgconf", "bison", "flex", "mandoc"]
makedepends = [
    "zlib-devel", "libedit-devel", "libffi-devel", "openssl-devel",
    "libyaml-devel"
]
pkgdesc = "Ruby scripting language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Ruby OR BSD-2-Clause"
url = "https://www.ruby-lang.org/en"
source = f"https://cache.ruby-lang.org/pub/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1a0e0b69b9b062b6299ff1f6c6d77b66aff3995f63d1d8b8771e7a113ec472e2"
# until verified; gonna need removing arch prefix from compiler name
# tests mostly pass but there are some portability issues in the test
# suite (stat usage) + chown not working in the sandbox + locale issues
options = ["!cross", "!check"]

match self.profile().arch:
    case "ppc64":
        # just ELFv2
        configure_args += ["--with-coroutine=ppc64le"]

if self.profile().cross:
    hostmakedepends += ["ruby"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("ruby-devel")
def _devel(self):
    return self.default_devel(extra = [
        f"usr/lib/ruby/{pkgver}/mkmf.rb"
    ])

@subpackage("ruby-ri")
def _ri(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return ["usr/bin/ri"]
