from cbuild.util import gnu_configure, make


def _get_libtool(self):
    if (self.bldroot_path / "usr/bin/slibtool").exists():
        return ["LIBTOOL=rlibtool"]
    return []


def do_configure(self):
    gnu_configure.replace_guess(self)
    gnu_configure.configure(self)


def do_build(self):
    self.make.build(_get_libtool(self))


def do_check(self):
    self.make.check(_get_libtool(self))


def do_install(self):
    self.make.install(_get_libtool(self))


def use(tmpl):
    tmpl.do_configure = do_configure
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install

    tmpl.make = make.Make(tmpl, env=gnu_configure.get_make_env())
    tmpl.build_style_defaults = [
        ("make_dir", "build"),
        ("configure_gen", ["autoreconf", "-if"]),
    ]
