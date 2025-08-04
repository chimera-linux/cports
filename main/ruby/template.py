pkgname = "ruby"
pkgver = "3.4.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-shared",
    "--disable-rpath",
    "--disable-install-doc",
    "ac_cv_func_isnan=yes",
    "ac_cv_func_isinf=yes",
]
make_build_args = ["all", "capi"]
hostmakedepends = [
    "automake",
    "bison",
    "flex",
    "mandoc",
    "pkgconf",
]
makedepends = [
    "libedit-devel",
    "libffi8-devel",
    "libyaml-devel",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Ruby scripting language"
license = "Ruby OR BSD-2-Clause"
url = "https://www.ruby-lang.org/en"
source = (
    f"https://cache.ruby-lang.org/pub/ruby/{pkgver[:-2]}/ruby-{pkgver}.tar.xz"
)
sha256 = "7b3a905b84b8777aa29f557bada695c3ce108390657e614d2cc9e2fb7e459536"
# until verified; gonna need removing arch prefix from compiler name
# tests mostly pass but there are some portability issues in the test
# suite (stat usage) + chown not working in the sandbox + locale issues
options = ["!cross", "!check"]

match self.profile().arch:
    case "aarch64" | "x86_64":
        # yjit only has backends here
        configure_args += ["--enable-yjit"]
        hostmakedepends += ["rust"]
        makedepends += ["rust-std"]
    case "ppc64":
        # just ELFv2
        configure_args += ["--with-coroutine=ppc64le"]

if self.profile().cross:
    hostmakedepends += ["ruby"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("ruby-devel")
def _(self):
    return self.default_devel(extra=[f"usr/lib/ruby/{pkgver[:-2]}.0/mkmf.rb"])


@subpackage("ruby-ri")
def _(self):
    self.depends += [self.parent]

    return ["usr/bin/ri"]
