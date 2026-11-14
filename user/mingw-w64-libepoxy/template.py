pkgname = "mingw-w64-libepoxy"
pkgver = "1.5.10"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["xorg-util-macros"]
makedepends = ["libglvnd-devel", "libx11-devel"]
depends = []
pkgdesc = "OpenGL function pointer handling for Windows development"
license = "MIT"
url = "https://github.com/anholt/libepoxy"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "a7ced37f4102b745ac86d6a70a9da399cc139ff168ba6b8002b4d8d43c900c15"
# TODO run check stage with wine
options = ["empty", "!check"]

_targets = ["x86_64", "i686", "aarch64", "armv7"]

for _an in _targets:
    hostmakedepends += [
        f"clang-mingw-w64-{_an}",
        f"mingw-w64-meson-{_an}",
        f"mingw-w64-pkg-config-{_an}",
    ]


def init_configure(self):
    for an in _targets:
        self.mkdir(f"build-{an}")


def configure(self):
    for an in _targets:
        at = f"{an}-w64-mingw32"
        self.do(
            f"{at}-meson",
            ".",
            f"build-{an}",
            "--default-library=both",
            env=self.configure_env,
        )


def build(self):
    from cbuild.util import meson

    for an in _targets:
        meson.invoke(self, "compile", f"build-{an}", env=self.make_build_env)


def install(self):
    from cbuild.util import meson

    for an in _targets:
        meson.install(self, f"build-{an}", env=self.make_install_env)


def post_install(self):
    for an in _targets:
        self.install_license("COPYING", name=f"{an}.COPYING")


def _gen(an, at):
    @subpackage(f"mingw-w64-libepoxy-{an}")
    def _(self):
        self.subdesc = f"{an} support"
        self.options = ["!strip"]
        self.depends = [f"mingw-w64-crt-{an}"]
        return [f"usr/{at}"]

    depends.append(self.with_pkgver(f"mingw-w64-libepoxy-{an}"))


for _an in _targets:
    _at = _an + "-w64-mingw32"
    _gen(_an, _at)
