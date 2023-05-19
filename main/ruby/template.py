pkgname = "ruby"
pkgver = "3.2.2"
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
sha256 = "4b352d0f7ec384e332e3e44cdbfdcd5ff2d594af3c8296b5636c710975149e23"
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
        f"usr/lib/ruby/{pkgver[:-2]}.0/mkmf.rb"
    ])

@subpackage("ruby-ri")
def _ri(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return ["usr/bin/ri"]

configure_gen = []
