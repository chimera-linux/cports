pkgname = "ncurses"
version = "6.2"
revision = 0
configure_args = ["--enable-big-core"]
make_cmd = "gmake"
short_desc = "System V Release 4.0 curses emulation library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
homepage = "http://www.gnu.org/software/ncurses/"
distfiles = [f"$(GNU_SITE)/ncurses/{pkgname}-{version}.tar.gz"]
checksum = ["30306e0c76e0f9f1f0de987cf1c82a5c21e1ce6568b9227f7da5b71cbea86c9d"]
options = ["bootstrap"]

if not current.bootstrapping:
    hostmakedepends = ["gmake"]

depends = [f"ncurses-base={version}-r{revision}"]

CFLAGS = ["-fPIC"]

def do_configure(self):
    from cbuild.util import gnu_configure

    with self.profile("host"):
        bcflags = self.get_cflags(shell = True)

    import os
    os.makedirs(self.cwd / "ncurses-build", exist_ok = True)
    os.makedirs(self.cwd / "ncursesw-build", exist_ok = True)

    # widec build
    gnu_configure.configure(
        self, build_dir = "ncursesw-build", extra_args = [
            "--enable-widec", "--with-shared", "--without-debug",
            "--with-manpage-symlinks", "--with-manpage-format=normal",
            "--without-ada", "--enable-ext-colors", "--without-tests",
            "--enable-pc-files", "--with-pkg-config-libdir=/usr/lib/pkgconfig",
            "ac_cv_path_ac_pt_PKG_CONFIG=/usr/bin/pkg-config",
            "BUILD_CFLAGS=" + bcflags
        ]
    )

    # non-widec build
    gnu_configure.configure(
        self, build_dir = "ncurses-build", extra_args = [
            "--with-shared", "--without-debug", "--without-ada",
            "--without-tests", "--enable-pc-files",
            "--with-pkg-config-libdir=/usr/lib/pkgconfig",
            "ac_cv_path_ac_pt_PKG_CONFIG=/usr/bin/pkg-config",
            "BUILD_CFLAGS=" + bcflags
        ]
    )

def init_build(self):
    from cbuild.util import make
    self.make = make.Make(self)

def do_build(self):
    self.make.build(wrksrc = "ncursesw-build")
    self.make.build(wrksrc = "ncurses-build")

def do_install(self):
    self.install_license("COPYING")

    self.make.install(wrksrc = "ncursesw-build")

    # fool packages looking to link to non-wide-character ncurses libraries
    for lib in ["curses", "ncurses", "form", "panel", "menu"]:
        libp = self.destdir / "usr/lib" / f"lib{lib}.so"
        libp.unlink(missing_ok = True)
        libp.with_suffix(".a").unlink(missing_ok = True)
        with open(libp, "w") as f:
            f.write(f"INPUT(-l{lib}w)\n")
        libp.chmod(0o755)
        self.install_link(f"lib{lib}w.a", f"usr/lib/lib{lib}.a")

    self.rm(self.destdir / "usr/lib/libncurses++.a", force = True)
    self.install_link("libncurses++w.a", "usr/lib/libncurses++.a")

    # some packages look for -lcurses during build
    self.rm(self.destdir / "usr/lib/libcursesw.so", force = True)
    with open(self.destdir / "usr/lib/libcursesw.so", "w") as f:
        f.write(f"INPUT(-lncursesw)\n")
    (self.destdir / "usr/lib/libcursesw.so").chmod(0o755)

    self.rm(self.destdir / "usr/lib/libcurses.so", force = True)
    self.rm(self.destdir / "usr/lib/libcursesw.a", force = True)
    self.rm(self.destdir / "usr/lib/libcurses.a", force = True)

    self.install_link("libncurses.so", "usr/lib/libcurses.so")
    self.install_link("libncursesw.a", "usr/lib/libcursesw.a")
    self.install_link("libncurses.a", "usr/lib/libcurses.a")

    # non-widec compatibility library
    self.install_lib(f"ncurses-build/lib/libncurses.so.{version}")
    self.install_link(
        f"libncurses.so.{version}",
        f"usr/lib/libncurses.so.{version[0:version.find('.')]}"
    )

    # create libtinfo symlinks
    self.install_link("libncursesw.so", "usr/lib/libtinfo.so")
    self.install_link(
        f"libncursesw.so.{version}", f"usr/lib/libtinfo.so.{version}"
    )
    self.install_link(
        f"libtinfo.so.{version}",
        f"usr/lib/libtinfo.so.{version[0:version.find('.')]}"
    )
    self.install_link("ncursesw.pc", "usr/lib/pkgconfig/tinfo.pc")

    # remove broken symlink
    self.rm(self.destdir / "usr/lib/terminfo", force = True)

    # FIXME for cross remove cross base from /usr/bin/ncursesw6-config

@subpackage("ncurses-libs")
def _libs(self):
    self.short_desc = short_desc + " - shared libraries"

    return [
        "usr/lib/libform*.so.*",
        "usr/lib/libmenu*.so.*",
        "usr/lib/libncurses*.so.*",
        "usr/lib/libpanel*.so.*",
    ]

@subpackage("ncurses-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = [f"ncurses-libs={version}-r{revision}"]

    return [
        "usr/bin/ncurses*-config",
        "usr/include",
        "usr/lib/pkgconfig/ncursesw.pc",
        "usr/lib/pkgconfig/formw.pc",
        "usr/lib/pkgconfig/menuw.pc",
        "usr/lib/pkgconfig/ncurses++w.pc",
        "usr/lib/pkgconfig/panelw.pc",
        "usr/lib/*.a",
        "usr/lib/libcurses*.so",
        "usr/lib/libform*.so",
        "usr/lib/libmenu*.so",
        "usr/lib/libncurses*.so",
        "usr/lib/libpanel*.so",
        "usr/share/man/man3",
        "usr/share/man/man1/ncursesw6-config.1",
    ]

@subpackage("ncurses-base")
def _base(self):
    self.short_desc = short_desc + " - base terminfo files"

    flist = []
    with (self.rparent.files_path / "base-files").open() as f:
        for fn in f:
            flist.append(fn.strip()[1:])

    return flist

@subpackage("ncurses-term")
def _term(self):
    self.short_desc = short_desc + " - full terminal descriptions"
    self.depends = [f"ncurses-base={version}-r{revision}"]

    return [
        "usr/share/tabset",
        "usr/share/terminfo",
    ]

@subpackage("ncurses-libtinfo-libs")
def _tinfo(self):
    self.short_desc = short_desc + " - libtinfo.so symlink"
    self.depends = [f"ncurses-libs={version}-r{revision}"]

    return ["usr/lib/libtinfo*.so.*"]

@subpackage("ncurses-libtinfo-devel")
def _tdevel(self):
    self.short_desc = short_desc + " - libtinfo.so symlink - development files"
    self.depends = [
        f"ncurses-devel={version}-r{revision}",
        f"ncurses-libtinfo-libs={version}-r{revision}"
    ]

    return [
        "usr/lib/libtinfo.so",
        "usr/lib/pkgconfig/tinfo.pc",
    ]