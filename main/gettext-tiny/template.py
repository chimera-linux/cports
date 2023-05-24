pkgname = "gettext-tiny"
pkgver = "0.3.2"
pkgrel = 0
pkgdesc = "Tiny replacement for GNU gettext suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/sabotage-linux/gettext-tiny"
source = f"https://github.com/sabotage-linux/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "29cc165e27e83d2bb3760118c2368eadab550830d962d758e51bd36eb860f383"
tool_flags = {"CFLAGS": ["-fPIC"]}
# no test suite; do not LTO (pointless and better not have libintl be bitcode)
options = ["!check", "!lto"]


# build manually as we can't depend on gmake during this point in bootstrap
def do_build(self):
    from cbuild.util import compiler

    cc = compiler.C(self)

    # main tools
    cc.invoke(
        ["src/msgfmt.c", "src/poparser.c", "src/StringEscape.c"], "msgfmt"
    )
    cc.invoke(
        ["src/msgmerge.c", "src/poparser.c", "src/StringEscape.c"], "msgmerge"
    )

    # other tools
    self.cp("src/xgettext.sh", "xgettext")
    with open(self.cwd / "autopoint", "w") as ap:
        with open(self.cwd / "src/autopoint.in") as iap:
            for ln in iap:
                ap.write(ln.replace("@datadir@", "/usr/share/gettext-tiny"))

    # libintl
    cc.invoke(["libintl/libintl-musl.c"], "libintl-musl.o", obj_file=True)


def do_install(self):
    self.install_license("LICENSE")

    # compiled tools
    self.install_bin("msgfmt")
    self.install_bin("msgmerge")

    # scripts
    self.install_bin("xgettext")
    self.install_bin("autopoint")

    # library
    self.install_dir("usr/lib")
    self.do(
        self.get_tool("AR"),
        "rcs",
        self.chroot_destdir / "usr/lib/libintl.a",
        "libintl-musl.o",
    )

    # m4 scripts
    self.install_dir("usr/share/gettext-tiny/m4")
    for f in (self.cwd / "m4").glob("*.m4"):
        self.install_file(f, "usr/share/gettext-tiny/m4")

    # aclocal symlinks
    self.install_dir("usr/share/aclocal")
    for f in (self.cwd / "m4").glob("*.m4"):
        self.install_link(
            f"../gettext-tiny/m4/{f.name}", f"usr/share/aclocal/{f.name}"
        )

    # data
    self.install_dir("usr/share/gettext-tiny/data")
    for f in (self.cwd / "data").glob("*"):
        self.install_file(f, "usr/share/gettext-tiny/data")


@subpackage("gettext-tiny-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.options = ["!splitstatic"]

    return self.default_devel(
        extra=[
            "usr/share/gettext-tiny",
            "usr/bin/autopoint",
        ]
    )
