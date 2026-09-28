from cbuild.util import gnu_configure, make


def _get_eargs(self):
    eargs = []
    if (self.bldroot_path / "usr/bin/slibtool").exists():
        eargs += ["LIBTOOL=rlibtool"]
    if self.verbose:
        eargs += ["V=1"]
    return eargs


def configure(self):
    gnu_configure.replace_guess(self)
    gnu_configure.configure(self)


def build(self):
    self.make.build(_get_eargs(self))


def check(self):
    self.make.check(_get_eargs(self))


def install(self):
    self.make.install(_get_eargs(self))


def use(tmpl):
    tmpl.configure = configure
    tmpl.build = build
    tmpl.check = check
    tmpl.install = install

    tmpl.make = make.Make(tmpl, env=gnu_configure.get_make_env())
    tmpl.build_style_defaults = [
        ("make_dir", "build"),
        ("configure_gen", ["autoreconf", "-if", "-W", "none"]),
    ]
