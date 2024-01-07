# FIXME: cross support

from cbuild.util import make


def do_configure(self):
    from cbuild.core import paths

    pf = self.profile()

    perlpfx = self.statedir / f"perlprefix-{pf.arch}"
    perlpfx.mkdir(parents=True)

    perlpathroot = "usr/lib/perl5/core_perl"
    perlpath = paths.bldroot() / pf.sysroot.relative_to("/") / perlpathroot

    if not perlpath.is_dir():
        perlpath = paths.bldroot() / perlpathroot

    if perlpath.is_dir():
        for f in perlpath.glob("Config*"):
            self.cp(f, perlpfx)
        self.cp(perlpath / "Errno.pm", perlpfx)

    pmkf = self.cwd / "Makefile.PL"
    if not pmkf.exists():
        self.error(f"could not find {pmkf}")

    cct = self.get_tool("CC")
    cflags = self.get_cflags(shell=True)
    ldflags = self.get_ldflags(
        ["-L" + str(self.profile().sysroot / "usr/lib"), "-lperl"], shell=True
    )

    incp = self.profile().sysroot / "usr/include"

    cenv = dict(self.configure_env)
    cenv.update(
        {
            "PERL5LIB": str(
                self.chroot_builddir / perlpfx.relative_to(self.builddir)
            ),
            "PERL_MM_USE_DEFAULT": "1",
            "GCC": cct,
            "CC": cct,
            "LD": cct,
            "CFLAGS": f"-I{incp} " + cflags,
            "OPTIMIZE": cflags,
            "LDFLAGS": ldflags,
            "LDDLFLAGS": "-shared " + ldflags,
        }
    )

    self.do(
        "perl",
        "-I.",
        "Makefile.PL",
        "INSTALLDIRS=vendor",
        *self.configure_args,
        wrksrc=self.make_dir,
        env=cenv,
    )


def do_build(self):
    cflags = self.get_cflags(shell=True)
    ldflags = self.get_ldflags(
        ["-L" + str(self.profile().sysroot / "usr/lib"), "-lperl"], shell=True
    )

    # by default, pass various stuff directly rather than through env
    tool_args = [
        "CC=" + self.get_tool("CC"),
        "LD=" + self.get_tool("CC"),
        "CFLAGS=" + cflags,
        "OPTIMIZE=" + cflags,
        "LDFLAGS=" + ldflags,
        "LDDLFLAGS=-shared " + ldflags,
    ]

    self.make.build(tool_args)


def do_check(self):
    self.make.check()


def do_install(self):
    self.make.install()


def use(tmpl):
    tmpl.do_configure = do_configure
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install

    tmpl.make = make.Make(tmpl)

    tmpl.build_style_defaults = [
        ("make_cmd", "gmake"),
        ("make_check_target", "test"),
    ]
