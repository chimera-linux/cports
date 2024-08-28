from cbuild.util import gnu_configure, make


def _get_libtool(self):
    if (self.bldroot_path / "usr/bin/slibtool").exists():
        return ["LIBTOOL=rlibtool"]
    return []


def configure(self):
    gnu_configure.replace_guess(self)
    gnu_configure.configure(self)


def build(self):
    self.make.build(_get_libtool(self))


def check(self):
    self.make.check(_get_libtool(self))


def install(self):
    self.make.install(_get_libtool(self))


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
