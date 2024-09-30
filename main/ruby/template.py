pkgname = "ruby"
pkgver = "3.3.5"
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
    "libffi-devel",
    "libyaml-devel",
    "openssl-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Ruby scripting language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Ruby OR BSD-2-Clause"
url = "https://www.ruby-lang.org/en"
source = (
    f"https://cache.ruby-lang.org/pub/ruby/{pkgver[:-2]}/ruby-{pkgver}.tar.xz"
)
sha256 = "51aec7ea89b46125a2c9adc6f36766b65023d47952b916b1aed300ddcc042359"
patch_style = "patch"
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
    # FIXME: in ruby 3.3.5 there are .lock stamp files installed for some reason
    self.uninstall("usr/bin/*.lock", glob=True)


@subpackage("ruby-devel")
def _(self):
    return self.default_devel(extra=[f"usr/lib/ruby/{pkgver[:-2]}.0/mkmf.rb"])


@subpackage("ruby-ri")
def _(self):
    self.depends += [self.parent]

    return ["usr/bin/ri"]
